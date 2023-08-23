import os

def print_hello_world():
	name = os.getenv("USERNAME")
	print("Hi {} from GitHub!".format(name))

if __name__ == '__main__':
	print_hello_world()
