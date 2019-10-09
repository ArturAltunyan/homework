# a = (1,2)

# print(a[0], a[1])
def average(in_list):
	sum  = 0
	for number in in_list:
	 	sum += number
	return sum/len(in_list)
in_list1 = [12, 5647584, 47, 415]
in_list2 = [12, 54, 478, 78]
print("Average:" ,  average(in_list1))
print("Average 2", average(in_list2))

def two_D_average(in_2d_list):
	result = []

	for num_list in in_2d_list:
		sum = 0
		for number in num_list:
			sum += number

		result.append(sum / len(num_list))
	return result
my_2d_list = [[61, 56, 645, 4], [56, 5, 6, 8], [7, 10, 143, 4]]
print("average:", two_D_average(my_2d_list))



	
list1 = [12, 56456, 78, 45, 5]
big = 0
for i in list1:
	if i > big:
		big = i
print(big)




	