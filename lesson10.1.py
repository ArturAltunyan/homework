# a = (1,2)

# print(a[0], a[1])

my_list = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]

my_list.remove(4)
print(my_list, ": After removing 23")

my_list.sort()
print(my_list, ": After sorting")

my_list.reverse()
print(my_list, ": After reversinging")

my_list.pop()
print(my_list, ": After reversinging")

del my_list[-5:]
print(my_list, ": After deleting the last five items")