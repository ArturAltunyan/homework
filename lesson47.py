import random
user_deck = []
dealer_deck = []
numbers = ["ace", "king", "queen", "jack", 10, 9, 8, 7, 6, 5, 4, 3, 2]
suit = ["heart", "diamond" , "club", "spade"]


# for i in range(0, len(numbers)):
# 	for j in range(0, len(suit)):
		# suit = {"heart": numbers[i],"diamond": numbers[i] , "club": numbers[i], "spade":numbers[i] }
a = f"{suit[random.randint(0, len(suit))]} of {numbers[random.randint(0, len(numbers))]}"
print(a)
suit["heart"] = numbers[random.randint(0,len(numbers)-1)]
suit["diamond"] = numbers[random.randint(0,len(numbers)-1)]
suit["club"] = numbers[random.randint(0,len(numbers)-1)]
suit["spade"] = numbers[random.randint(0,len(numbers)-1)]

for key in suit.keys():
	k = random.randint(key)
	print(suit[k])


print(random.randint(suit["diamond"]))

deck = []

for i in range(0, len(numbers)):
	deck.append(numbers[random.randint(0,len(numbers)-1)])
for j in range(0, len(suit)):
	deck.append(suit[random.randint(0,len(suit)-1)])


print(numbers[random.randint(0,len(numbers)-1)])
random.shuffle(deck)

print(deck)




# random.shuffle(random)


# b = []
# f = []
# a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# # def random_alpha():
# # 	random.randint(0,9)

# # random_alpha()
# c = int(input("write any number"))
# d = int(input("write any number for word"))
# for i in range(0,c):
# 	if i < c:
		
# 		b.append(random.randint(0,9))
			
			
# for j in range(d):
# 	if j < d:
# 		b.append(a[random.randint(0,len(a))])
# for k in range(len(b)):
# 	if k < (c + d):
# 		f.append(b[random.randint(0,len(b))])


# print(b)
# print(b[0])
# print(len(b))
# print(f)


