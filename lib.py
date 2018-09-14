import tools
from tools import *

#################################################################################################
spDict = {
	"repEncoder": ["i am a student ", "iamstudenhcroxygwpbfjklqvz"],
	"repDecoder": ["NF LIB MYKTPTS LNFE VTRRYL.", "iamstudenhcroxygwpbfjklqvz"],
	"repCracker": ["ER", "uh"],
	"LFSRAnalyzer": ["110", "101"],
	"LFSRCracker": ["111010", 3],
	"rabinEncoder": [59, 87, 994],
	"rabinDecoder": [59, 87, 2500],
	"RSAEncoder": [37, 73, 11, 1234],
	"RSADecoder": [2773, 157, 2015],
	"dividePrime": [473],
	"signMsg": [83, 41, 4, 10, 21, 40],
	"verifyMsg": [83, 41, 4, 37, 40, 40, 19],
	"remainDivider": [47, 3, [7, 9, 13]],
	"remainRecoverer": [[(3, 4, 308),(5, 7, 308),(3, 11, 308)]],
	"ShamirRecoverer": [3, 23, [(0,1), (1,4), (3, 81)]]
}

#################################################################################################
def repEncoder():
	sample(spDict["repEncoder"])
	print("请提供明文和字典(长为26的置换字符串)")
	str = input("请输入明文:\n")
	dict = input("请输入字典:\n")
	rs = tools.repEncoder(str, dict)
	print("你生成的密码是:\n%s" % (rs))

def repDecoder():
	sample(spDict["repDecoder"])
	print("请提供密文和字典(长为26的置换字符串)")
	str = input("请输入密文:\n")
	dict = input("请输入字典:\n")
	rs = tools.repDecoder(str, dict)
	print("你请求的明文是:\n%s" % (rs))

def repCracker():
	sample(spDict["repCracker"])
	print("请确保您破解的密码体制是非分组的仿射变换，并提供密文和明文")
	c = input("请输入密文:\n")
	m = input("请输入明文:\n")
	rs = tools.repCracker(c, m)

#################################################################################################
def LFSRAnalyzer():
	sample(spDict["LFSRAnalyzer"])
	print("请提供初始状态和递归函数系数(均为等长的01字符串)")
	init = input("请输入初始状态:\n")
	principle = input("请输入递归函数系数:\n")
	rs = tools.LFSRAnalyzer(init, principle)
	print("反馈移位寄存器的周期是:\n%d" % (rs))

def LFSRCracker():
	sample(spDict["LFSRCracker"])
	print("请提供反馈移位寄存器的一段实例(01字符串)和阶数")
	stream = input("请输入实例:\n")
	rank = int(input("请输入阶数:\n"))
	rs = tools.LFSRCracker(stream, rank)
	print("递归函数系数是:\n", rs)

#################################################################################################
def rabinEncoder():
	sample(spDict["rabinEncoder"])
	print("请提供加密素数对和消息")
	p = int(input("请输入第一个素数:\n"))
	q = int(input("请输入第二个素数:\n"))
	m = int(input("请输入消息:\n"))
	rs = tools.rabinEncoder(p, q, m)
	print("Rabin加密后的消息是:")
	print(rs)

def rabinDecoder():
	sample(spDict["rabinDecoder"])
	print("请提供素数对和密文")
	p = int(input("请输入第一个素数:\n"))
	q = int(input("请输入第二个素数:\n"))
	c = int(input("请输入密文:\n"))
	rs = tools.rabinDecoder(p, q, c)
	print("Rabin解密后的消息是:")
	print(rs)

#################################################################################################
def RSAEncoder():
	sample(spDict["RSAEncoder"])
	print("请提供素数对，密钥和消息")
	p = int(input("请输入第一个素数:\n"))
	q = int(input("请输入第二个素数:\n"))
	e = int(input("请输入密钥:\n"))
	m = int(input("请输入消息:\n"))
	rs = tools.RSAEncoder(p, q, e, m)
	print("RSA加密后的消息是:")
	print(rs)

def RSADecoder():
	sample(spDict["RSADecoder"])
	print("请提供n，密钥和密文")
	n = int(input("请输入n:\n"))
	e = int(input("请输入密钥:\n"))
	c = int(input("请输入密文:\n"))
	rs = tools.RSADecoder(n, e, c)
	print("RSA解密后的消息是:")
	print(rs)

#################################################################################################
def dividePrime():
	sample(spDict["dividePrime"])
	print("请提供待分解的数")
	n = int(input("请输入待分解的数:\n"))
	rs = tools.dividePrime(n)
	print("分解结果是:")
	print(rs)

#################################################################################################
def signMsg():
	sample(spDict["signMsg"])
	print("请提供素数对,g(=α),x,随机数k,消息m以生成签名")
	p = int(input("请输入第一个素数:\n"))
	q = int(input("请输入第二个素数:\n"))
	g = int(input("请输入g:\n"))
	x = int(input("请输入x:\n"))
	k = int(input("请输入随机数:\n"))
	m = int(input("请输入消息:\n"))
	rs = tools.signMsg(p, q, g, x, k, m)
	print("签名信息是:")
	print(rs)

def verifyMsg():
	sample(spDict["verifyMsg"])
	print("请提供素数对,g(=α),y(=β),消息m和签名r,s以验证签名")
	p = int(input("请输入第一个素数:\n"))
	q = int(input("请输入第二个素数:\n"))
	g = int(input("请输入g(或α):\n"))
	y = int(input("请输入y(或β):\n"))
	m = int(input("请输入消息:\n"))
	r = int(input("请输入签名r:\n"))
	s = int(input("请输入签名s:\n"))
	rs = tools.verifyMsg(p, q, g, y, m, r, s)
	if rs:
		print("验证通过")
	else:
		print("验证不通过")

#################################################################################################
def remainDivider():
	sample(spDict["remainDivider"])
	print("请提供s, n和生成子密钥的列表")
	s = int(input("请输入母密钥s:\n"))
	n = int(input("请输入n:\n"))
	m = eval(input("请输入生成子密钥的列表:\n"))
	rs = tools.remainDivider(s, n, m)
	print("生成的子密钥是")
	print(rs)

def remainRecoverer():
	sample(spDict["remainRecoverer"])
	print("请提供生成子密钥列表")
	m = eval(input("请输入子密钥列表:\n"))
	rs = tools.remainRecoverer(m)
	print("原密钥是")
	print(rs)

def ShamirRecoverer():
	sample(spDict["ShamirRecoverer"])
	print("请提供k, q和样本点(点列表)")
	k = int(input("请输入k:\n"))
	q = int(input("请输入q:\n"))
	pts = eval(input("请输入点列表:\n"))
	rs = tools.ShamirRecoverer(k, q, pts)
	print("原密钥是")
	print(rs)

#################################################################################################
def sample(list):
	print("sample:")
	for msg in list:
		print("→", msg)
	print("\n-----------------------------------------\n")