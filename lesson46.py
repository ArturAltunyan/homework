import random
b = []
f = []
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# def random_alpha():
# 	random.randint(0,9)

# random_alpha()
c = int(input("write any number"))
d = int(input("write any number for word"))
for i in range(0,c):
	if i < c:
		
		b.append(random.randint(0,9))
			
			
for j in range(d):
	if j < d:
		b.append(a[random.randint(0,len(a))])
for k in range(len(b)):
	if k < (c + d):
		f.append(b[random.randint(0,len(b))])


print(b)
print(b[0])
print(len(b))
print(f)


