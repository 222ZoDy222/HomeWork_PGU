from random import randint

Arr = []
Max = 0
Min = 100
for i in range(10):
	Arr.append(randint(0,100))
	print(Arr[i])
	if(Arr[i] > Max):
		Max = Arr[i]
	if(Arr[i] < Min):
		Min = Arr[i]
print(Arr[1])
print('\n',Max-Min)
input()