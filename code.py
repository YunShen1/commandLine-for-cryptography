# 模块
import re
import os
import math
from numpy import *
import numpy as np

# 全局变量
alpha = "abcdefghijklmnopqrstuvwxyz" #字母表

#################################################################################################
# 替换密码工具
# 编码者
# str:明文;dict:映射规则（长度为26的字符串）
def repEncoder(str, dict):
	result = ""
	str = str.lower()

	for s in str:
		if alpha.find(s) < 0:
			result += s
		else:
			result += dict[alpha.find(s)]

	return result

# 解码者
# str:密文;dict:映射规则（长度为26的字符串）
def repDecoder(str, dict):
	result = ""
	str = str.lower()

	for s in str:
		if dict.find(s) < 0:
			result += s
		else:
			result += alpha[dict.find(s)]

	return result

# 破解者(线性加密公式)
# 注：密文与明文至少应该都两个字母以上
def repCracker(c, m):
	c, m = c.lower(), m.lower()
	c, m = re.sub(r'[^a-z]', "", c),re.sub(r'[^a-z]', "", m)

	n1, n2, n3, n4 = alpha.find(c[0]), alpha.find(c[1]), alpha.find(m[0]), alpha.find(m[1])
	A = eqSolver(n1, n2, n3, n4)
	B = eqSolver(n3, n4, n1, n2)

	dict = dictGenerator(A[0], A[1])

	print("加密函数: %dx%+d" % (A[0], A[1]))
	print("解密函数: %dx%+d" % (B[0], B[1]))
	print("置换字典: %s" % (dict))

	return dict

#################################################################################################
# 移位密码工具
# 周期分析器
# init: 初始状态, principle: 转移法则(数组)
def LFSRAnalyzer(init, principle):
	staList = [init]
	curSta = init

	while(True):
		temp = 0
		for i in range(len(principle)):
			temp += int(curSta[i]) * int(principle[i])
		curSta = curSta[1:] + str(temp % 2)

		if curSta not in staList:
			staList.append(curSta)
		else:
			T = len(staList) - staList.index(curSta)
			break

	print(T)

# 破解工具
def LFSRCracker(stream, rank):

	head = list(stream[:rank])
	a = mat(toInt(head))
	for i in range(1, rank):
		r = list(stream[i : rank + i])
		r = mat(toInt(r))
		a = vstack((a, r))

	tail = list(stream[len(stream)-3:])
	tail = mat(toInt(tail)).T
	result = (a.I * tail % 2).tolist()
	result = [int(x) for j in result for x in j]
	
	return result

#################################################################################################
# Rabin密码
# 加密工具
def rabinEncoder(p, q, m):
	n = p * q
	c = m * m % n
	return int(c)

# 解密工具
# 注意： 涉及大指数运算，可能误差
def rabinDecoder(p, q, c):
	n = p * q

	y1 = rev(q, p)
	y2 = rev(p, q)
	z1 = math.pow(c, (p+1)/4) % n
	z2 = math.pow(c, (q+1)/4) % n
	a1 = y1 * z1 * q
	a2 = y2 * z2 * p

	result = []
	result.append((a1 + a2) % n)
	result.append((a1 - a2) % n)
	result.append((-a1 + a2) % n)
	result.append((-a1 - a2) % n)

	print("涉及指数运算: %d的%d次方\n%d" % (c, (p+1)/4), math.pow(c, (p+1)/4))
	print("涉及指数运算: %d的%d次方\n%d" % (c, (q+1)/4), math.pow(c, (q+1)/4))
	return toInt(result)

#################################################################################################
# RSA密码
# 加密工具
# 注意： 涉及大指数运算，可能误差
def RSAEncoder(p, q, e, m):
	n = p * q
	c = math.pow(m, e) % n
	print("涉及指数运算: %d的%d次方\n%d" % (m, e, math.pow(m, e)))
	return int(c)

# 解密工具
# 注意： 涉及大指数运算，可能误差
def RSADecoder(n, e, c):
	pq = dividePrime(n)
	p = pq[0]
	q = pq[1]

	el = (p - 1) * (q - 1)
	d = rev(e, el)
	m = math.pow(c, d) % n

	print("涉及指数运算: %d的%d次方\n%d" % (c, d, math.pow(c, d)))
	return int(m)

#################################################################################################
# 大素数分解工具
def dividePrime(n):
	a = math.ceil(math.sqrt(n))

	while a < n:
		b = math.sqrt(a * a - n)
		if(b == int(b)):
			break
		else:
			a += 1

	result = []
	result.append(a + b)
	result.append(a - b)
	return toInt(result)


#################################################################################################
# 数字签名
# 签名工具
# 假设H(m) = m
# g: α; x: H(m); k: 随机数;
def signMsg(p, q, g, x, k, m):
	r = math.pow(g, k) % p % q
	revK = rev(k, q)
	s = revK * (m + x * r) % q

	print("涉及指数运算: %d的%d次方\n%d" % (g, k, math.pow(g, k)))
	result = [r, s]
	return toInt(result)

# Dss签名验证工具
# 假设H(m) = m
# g: α; x: H(m); k: 随机数; y: β
def verifyMsg(p, q, g, y, m, r, s):
	w = rev(s, q)
	u1 = (m * w) % q
	u2 = (r * w) % q
	R = (math.pow(g, u1) * math.pow(y, u2)) % p % q

	print("涉及指数运算: %d的%d次方\n%d" % (g, u1, math.pow(g, u1)))
	print("涉及指数运算: %d的%d次方\n%d" % (y, u2, math.pow(y, u2)))
	return R == r

#################################################################################################
# 密钥分割与还原
# 中国剩余定理分割密钥
# m: 子密钥生成列表
def remainDivider(s, n, m):
	M = 1
	for i in range(len(m)):
		M *= m[i]

	rs = [(s % x, x, M) for x in m]
	return rs

# 中国剩余定理还原密钥
# m: 子密钥列表
def remainRecoverer(m):
	N = 1
	for i in range(len(m)):
		N *= m[i][1]
	M = m[0][2]

	MList, NList, YList = [], [], []
	for i in range(len(m)):
		MList.append(M / m[i][1])
		NList.append(rev(MList[i], m[i][1]))
		YList.append(MList[i] * NList[i] * m[i][0])

	rs = sum(YList) % N
	return int(rs)

# Shamir还原密钥
# pts: 点列表
def ShamirRecoverer(k, q, pts):
	x = [x[0] for x in pts]
	y = [x[1] for x in pts]

	rs = 0
	for i in range(len(x)):
		x2 = [(-y) for y in x]
		x2[i] = 1
		a = prod(x2)
		x3 = [(x[i] - y) for y in x]
		x3[i] = 1
		b = prod(x3)

		rs += y[i] * a / b

	return rs

#################################################################################################
def init():	
	clear()
	print("Input a letter for continue..")
	print("a. 替换密码工具")
	print("b. 移位密码工具")
	print("c. rabin加密解密工具")
	print("d. RSA加密解密工具")
	print("e. 大素数分解")
	print("f. 数字签名与验证")
	print("g. 密钥分割与还原")

	option = input("请输入选项: ")
	enter(option)	# 清屏之后显示内容




#################################################################################################
# 工具函数
# 乘法逆元函数
def rev(x, y):
	for i in range(1,1000000):
		if (x * i -1) % y == 0:
			return i
	return 0

# 二元一次模方程求解器
def eqSolver(n1, n2, n3, n4):
	a = ((n4 - n3) % 26) / (n2 - n1)
	b = n3 - n1 * a
	return [a, b]

# 列表批量转整型
def toInt(list):
	return [int(i) for i in list]

# 字典生成器(仿射公式)
def dictGenerator(a, b):
	dict = ""
	for i in range(26):
		temp = int((a * i + b) % 26)
		dict += alpha[temp]
	return dict

# 连乘器
def prod(list):
	p = 1
	for i in list:
		p *= i
	return p

# 展示子菜单
def enter(option):
	clear()
	print("Input a letter for continue..")
	print("a. 替换密码工具")
	print("b. 返回")
	option = input("请输入选项: ")
	init()

# 清屏
def clear():
	os.system('cls')
	os.system('clear')

#################################################################################################
def main():
	# code = repEncoder("i am a student","iamsstudenhcroxygwpbfjklqvz")
	# print(repEncoder("it was covered with yellow.", "iamstudenhcroxygwpbfjklqvz"))
	# print(repDecoder("NF LIB MYKTPTS LNFE VTRRYL.", "iamstudenhcroxygwpbfjklqvz"))
	# dict = repCracker("ER", "uh")
	# LFSRAnalyzer("110", "101")
	# rs = LFSRCracker("111010", 3)
	# print(rs)
	# print(rabinEncoder(59, 87, 994))
	# print(rabinDecoder(59, 87, 2500))
	# print(dividePrime(2773))
	# print(RSAEncoder(37, 73, 11, 1234))
	# print(RSADecoder(2773, 157, 2015))
	# print(signMsg(83, 41, 4, 10, 21, 40))
	# print(verifyMsg(83, 41, 4, 37, 40, 40, 19))
	# c = remainDivider(47, 3, [7, 9, 13])
	# print(c)
	# print(remainRecoverer(c))
	# print(ShamirRecoverer(3, 23, [(1, 5), (2, 8), (3, 15)]))
	init()

main()