import threading
import time

# def thread_function():
# 	for i in range(0,10):
# 		print(i)
# 		time.sleep(1)
# def insert_function():
# 	return "Hello world"
# # threading_function()
# x = threading.Thread(target=thread_function)


# x.start()

# print("asdasd")


def thread_function():
	for i in range(-10,0):
		print(i)
		time.sleep(0.5)
# def thread_function2():
# 	for i in range(0,100):
# 		print(i)
# 		time.sleep(1)
# threading_function()

def thread_function1():
	for i in range(0,10):
		print(i)
		time.sleep(0.2)

x = threading.Thread(target=thread_function)
 
x.start()
# y.start()


thread_function1()