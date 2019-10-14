fruits = {"apple": 5, "pineapple": 15, "orange": 36, "bananas": 2}


print(fruits.keys())
print(fruits.values())
for i in fruits.values():
	print(i, end=" ")
for key in fruits.keys():
	if fruits[key] > 5:
		print(key)
