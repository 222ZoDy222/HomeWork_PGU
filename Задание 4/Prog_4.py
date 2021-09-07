from random import randint

Arr = []
count = 0
Col = []
for i in range(6):
	Arr.append([])
	for j in range(6):
		Arr[i].append(randint(0,4))
		count += Arr[i][j]
		print(Arr[i][j],end='  ')
	print('\t',count,'\n')
	count = 0
print('\n')

for i in range(6):
	for j in range(6):
		count += Arr[j][i]
	print(count,end=' ')
	count = 0



input()