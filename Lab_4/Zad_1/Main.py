import random
M1 = []
N1 = int(input("First Matrix: "))
chance = [0,0,0,1,1,1,1,1,1,1]
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



def DFS(v):
	print(v + 1)
	Vis[v] = 1
	for i in range(N1):
		if(M1[v][i] == 1 and Vis[i] == 0):
			DFS(i)
	



v = int(input("Вершина: ")) - 1
Vis = []
for i in range(len(M1)):
	Vis.append(0)
DFS(v)

