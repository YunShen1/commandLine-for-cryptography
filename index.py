import os

########################################################################################

index = []
alpha = "abcdefghijklmnopqrstuvwxyz"

########################################################################################

def clear():
	os.system('cls')
	os.system('clear')

def select():
	option = c2n(input("请输入选项: "))
	while option < 0 or option >= len(menu):
		option = c2n(input("输入错误，请重新选择"))
	return option

def enter(path, option):
	key = list(path.keys())[option]
	value = path[key]
	if type(value) == type({}):
		index.append(option)
	else:
		value()

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

def xx():
	print("执行方法")

def yy():
	index.pop()

def c2n(c):
	return alpha.find(c.lower())

def n2c(n):
	return alpha[n]

########################################################################################

menu = {
	"替换":{
		"加密变换":xx, 
		"解密变换":xx, 
		"字典破解":xx,
		"..":yy
	},
	"移位":{
		"周期计算":xx,
		"机制分析":xx,
		"..":yy
	},
	"rabin":{
		"加密工具":xx,
		"解密工具":xx,
		"..":yy
	},
	"RSA":{
		"加密工具":xx,
		"解密工具":xx,
		"..":yy
	},
	"素数分解": {
		"素数分解":xx,
		"..":yy
	},
	"数字签名":{
		"消息签名":xx,
		"签名验证":xx,
		"..":yy
	},
	"密钥分配":{
		"中国剩余定理分配密钥":xx,
		"中国剩余定理还原密钥":xx,
		"Shamir还原密钥":xx,
		"..":yy
	}
}

def init():
	path = menu
	while True:
		disp(path)
		option = select()
		enter(path, option)
		path = updatePath(index)

init()
