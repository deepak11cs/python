def func():
	print('function in one.py')

print('this is main level in one.py')

if __name__ == "__main__":
	print('one.py is being executed directly')
else:
	print('one.py is being imported in another module')