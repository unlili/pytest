import random

r = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)] 

lis = []
for b in range(200):
	c = ''
	for i in range(16):
		if i%4==0 and i != 0:
			c += ' '
		c += random.choice(r)

	lis.append(c)

print(lis)
print(len(lis))
