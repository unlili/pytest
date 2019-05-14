'''
凯撒密码

移动三位
明文字母表：a b c d e f g h i j k l m n o p q r s t u v w x y z 
密文字母表：d e f g h i j k l m n o p q r s t u v w x y z a b c 
明文字母表：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
密文字母表：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
love --加密-->  oryh

'''

class KaiSa():
	def __init__(self,n):
		self.n = n
	def _create(self):
		#小写a到z
		rr = r = [chr(i) for i in range(97,123)]
		#大写A到Z
		rr_ = r_ = [chr(i) for i in range(65,91)] 

		#向后移动n位，后面的往前补
		rn = r[self.n:] + r[0:self.n]
		r_n = r_[self.n:] + r_[0:self.n]

		qw = rr + rr_
		wq = rn + r_n
		wr = {}
		for q,w in zip(qw,wq):
			wr[q] = w
		wr[' '] = ' '
		return wr
	#传入一个字符串，进行解密  love 加密--->  ilsb
	def parse(self,string):
		if isinstance(string,str):
			c = []
			for i in string : #len(string)
				for r,g in self._create().items(): #53
					if i == g:
						c.append(r)
			return ''.join(c)
		else:
			print('！！！请输入一个字符串！！！')

	#传入一个字符串，进行加密
	def encryption(self,string):
		if isinstance(string,str):
			c = []
			for i in string : #len(string)
				for r,g in self._create().items(): #53
					if i==r:
						c.append(g)
			return ''.join(c)
		else:
			print('！！！请输入一个字符串！！！')

#---------------------------------------------------------------------------------------------
ks = KaiSa(3)
a = ks.encryption('i love lzf')
b = ks.parse('oryh')
print(a)
print(b)

