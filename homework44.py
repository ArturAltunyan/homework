try:
	input_file = open("Numberfil.txt", mode = "r")
	try:
		for line in input_file:
			print(int(line))
	except ValueError:
		print("A value error occured")
	else:
		print("No error occured")
	finally:
		input_file.close()
except IOError:
	print("File can't open error")
