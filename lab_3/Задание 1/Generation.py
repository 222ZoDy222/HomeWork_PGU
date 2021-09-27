import random

def main():
	#	1 - 2 Задания
	M1 = []
	M2 = []
	for i in range(5):
		M1.append([])
		M2.append([])
		for j in range(5):
			M1[i].append(random.randint(0,1))
			M2[i].append(random.randint(0,1))
			if(i == j):
				M1[i][j] = 0
				M2[i][j] = 0
	for i in range(5):
		for j in range(5):
			print(M1[i][j],end='\t')
		print('\n')
	print('\n')
	print('\n')
	print('\n')
	for i in range(5):
		for j in range(5):
			print(M2[i][j],end='\t')
		print('\n')

	# 3 задание
	# Отождествление вершин

	a1 = int(input('Первая вершина')) - 1
	a2 = int(input('Вторая вершина')) - 1







main()