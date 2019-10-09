# a = (1,2)

# print(a[0], a[1])

my_list = [1, 2, 3, 4, 45, 878, 897898, 4]

my_list.append(6)
print(my_list, ": After appending five")

new_list = [10,7,8]
my_list.extend(new_list)
print(my_list, ": After extending")

a = [45, 85, 456]

my_list.insert(5, a)
print(my_list, ": After inserting zero")