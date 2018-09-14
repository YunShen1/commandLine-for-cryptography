import lib
from lib import *

########################################################################################

index = []

########################################################################################

def clear():
	os.system('cls')
	os.system('clear')

def select(path):
	option = c2n(input("请输入选项: "))
	while option < 0 or option >= len(path):
		option = c2n(input("输入错误，请重新选择: "))
	return option

def enter(path, option):
	key = list(path.keys())[option]
	value = path[key]
	if type(value) == type({}):
		index.append(option)
	else:
		clear()
		try:
			value()
		except Exception as e:
			print("发生了异常:")
			print(e) 
		if value.__name__ != "yy":
			pause = input("请输入回车键继续")

def updatePath(index):
	path = menu
	for i in range(len(index)):
		keys = list(path.keys())
		path = path[keys[index[i]]]
	return path
	
def disp(path):
	clear()
	print("Input a letter for continue..")
	if type(path) == type({}):
		keys = list(path.keys())
		i = 0
		for k in keys:
			print("%s. %s" % (n2c(i), k))
			i += 1
	else:
		print(path)

def yy():
	index.pop()

def zz():
	exit()

def c2n(c):
	return alpha.find(c.lower())

def n2c(n):
	return alpha[n]

########################################################################################

menu = {
	"替换密码":{
		"加密变换": repEncoder, 
		"解密变换": repDecoder, 
		"字典破解": repCracker,
		"..":yy
	},
	"移位寄存器":{
		"周期计算": LFSRAnalyzer,
		"机制分析": LFSRCracker,
		"..":yy
	},
	"Rabin加密":{
		"Rabin加密工具": rabinEncoder,
		"Rabin解密工具": rabinDecoder,
		"..":yy
	},
	"RSA加密":{
		"RSA加密工具": RSAEncoder,
		"RSA解密工具": RSADecoder,
		"..":yy
	},
	"素数分解": {
		"素数分解": dividePrime,
		"..":yy
	},
	"数字签名":{
		"消息签名": signMsg,
		"签名验证": verifyMsg,
		"..":yy
	},
	"密钥分配":{
		"中国剩余定理分配密钥": remainDivider,
		"中国剩余定理还原密钥": remainRecoverer,
		"Shamir还原密钥": ShamirRecoverer,
		"..":yy
	},
	"退出": zz
}

def init():
	path = menu
	while True:
		disp(path)
		option = select(path)
		enter(path, option)
		path = updatePath(index)

init()
