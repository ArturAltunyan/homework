# my_int1 = 1
# my_int2 = 2
# my_int3 = 3

# out_put_file = open("outputfile.txt", "w")
# out_put_file.write(str(my_int1) + "\n")
# out_put_file.write(str(my_int2) + "\n")
# out_put_file.write(str(my_int3) + "\n")

# out_put_file.close()

# my_ints_list = ["home", "home", "home", "home"]
# out_put_file = open("outputfile.txt", "w")
# out_put_file.writelines(my_ints_list)
# out_put_file.close()


# my_ints_list = ["home", "home", "home", "home"]
# out_put_file = open("outputfile.txt", "w")

# for line in my_ints_list:
# 	line += "\n"
# out_put_file.writelines(my_ints_list)

# for i in range(len(my_ints_list)):
# 	my_ints_list[i] += "\n"
# out_put_file.writelines(my_ints_list)

# out_put_file = open("outputfile.txt", "a")
# for i in range(len(my_ints_list)):
# 	my_ints_list[i] += "\n"
# out_put_file.writelines(my_ints_list)

# out_put_file = open("outputfile.txt", "r")
# print(out_put_file.readline(), end="")
# print(out_put_file.readline(), end="")
# out_put_file.close()


name_list =[]
out_put_file = open("outputfile.txt", "r")

for line in out_put_file:
	name_list.append(line)
out_put_file.close()
print(name_list)

