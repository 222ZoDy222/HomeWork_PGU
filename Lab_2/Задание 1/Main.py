import time
from random import randint
start_time = time.time() 
# Задаём время начала выполнения программы


def Main():
	A = []
	B = []
	C = []
	for i in range(SIZE_MATRIX):
		A.append([])
		B.append([])
		for j in range(SIZE_MATRIX):
			A[i].append(randint(0,100))
			B[i].append(randint(0,100))

	for i in range(SIZE_MATRIX):
		C.append([])	
		for j in range(SIZE_MATRIX):
			C[i].append(A[i][j] * B[i][j])

	print("--- %s seconds ---" % (time.time() - start_time))


SIZE_MATRIX = 100
Main()
SIZE_MATRIX = 200
Main()
SIZE_MATRIX = 400
Main()
SIZE_MATRIX = 1000
Main()
SIZE_MATRIX = 2000
Main()
SIZE_MATRIX = 4000
Main()
SIZE_MATRIX = 10000
Main()
SIZE_MATRIX = 100000
Main()








