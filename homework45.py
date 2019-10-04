while True:
	try:
		x = int(input("Enter a number"))
		y = int(input("Enter another number"))
		print(x,"/", y , "=", x/y)
		break
	except ZeroDivisionError:
		print("Cant' divide by zero")
	except ValueError:
		print("That doesn't look like a number!")
	except:
		print("Something unexpected happend!")