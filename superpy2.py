def superPy2():
	from superpy1 import superPy1
	from superpy3 import superPy3
	fibos = [0]
	a = 1
	b = 0
	c = 0
	while True:
		c = a + b
		a = b
		b = c
		fibos += [c]
		try:
			superPy1()
		except RecursionError:
			print("Error")
			superPy3()