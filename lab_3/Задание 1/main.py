import random
M1 = []
M2 = []
N1 = int(input("First Matrix: "))
N2 = int(input("Second Matrix: "))
chance = [0,0,0,1,1,1,1,1,1,1]
#Шанс 1 - 70%
#Шанс 0 - 30%

#Создание 2 матриц смежности неориентированных помеченных графов 
# № 1
for i in range(N1):
	M1.append([])
	for j in range(N1):
		M1[i].append(random.choice(chance))
		if(i == j):
			M1[i][j] = 0
		
for i in range(N1):
	for j in range(N1):
		M1[i][j] = M1[j][i]
		print(M1[i][j],end='\t')
	print('\n')
print('\n'*3)
# № 2
'''
for i in range(N2):
	M2.append([])
	for j in range(N2):
		M2[i].append(random.choice(chance))
		if(i == j):
			M2[i][j] = 0
		
for i in range(N1):
	for j in range(N2):
		M2[i][j] = M2[j][i]
		print(M2[i][j],end='\t')
	print('\n')
print('\n'*3)
'''
'''
# Преобразование в список смежности
List_S1 = []
print("Первый список смежности:\n")
for i in range(N1):
	List_S1.append([])
	for j in range(N1):
		if(M1[i][j] == 1):
			List_S1[i].append(j+1)

for i in range(N1):
	print(i+1,' -- ',end='')
	for j in range(len(List_S1[i])):
		print(List_S1[i][j],end=' ')
	print('\n')
print("\n"*2)
List_S2 = []
print("Второй список смежности:\n")
for i in range(N2):
	List_S2.append([])
	for j in range(N2):
		if(M2[i][j] == 1):
			List_S2[i].append(j+1)

for i in range(N2):
	print(i+1,' -- ',end='')
	for j in range(len(List_S2[i])):
		print(List_S2[i][j],end=' ')
	print('\n')	
print('\n'*3)
'''
'''------------------------------------------------------ 2 задание
№ 1 - Отождествление вершин
'''
a1 = int(input('Первая вершина')) - 1
a2 = int(input('Вторая вершина')) - 1

print(M1[a1])
print(M1[a2])
Col = []
for i in range(N1):
	print(M1[a1][i],M1[a2][i])
	if(M1[a1][i] == 1 or M1[a2][i] == 1):
		Col.append(1)
	else:
		Col.append(0)
print(Col)

for i in range(N1):
	for j in range(N1):
		print(M1[i][j],end='\t')
	print('\n')
print('\n'*3)













