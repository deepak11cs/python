import one

one.func()

print('this is main level in two.py')

if __name__ == "__main__":
	print("two.py is being ran directly")
else:
	print("two.py is imported in another module")