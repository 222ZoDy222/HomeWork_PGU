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


def BFS(v):
	Vis[v] = 1
	queue.append(v)
	while(bool(queue)):
		s = queue[0]
		print(s+1)
		queue.pop(0)
		for i in range(len(M1)):
			if(M1[s][i] == 1 and Vis[i] == 0):
				queue.append(i)
				Vis[i] = 1



print("---список смежности---")

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')

def BFS1(v1):
	Vis1[v1] = 1
	queue1.append(v1)
	while(bool(queue1)):
		l = queue1[0]
		print(l+1)
		queue1.pop(0)
		for i in range(len(c[l])):
			if(Vis1[c[l][i]] == 0):
				queue1.append(c[l][i])
				Vis1[c[l][i]] = 1



v = int(input('Вершина : ')) - 1

Vis = []
for i in range(len(M1)):
	Vis.append(0)


queue = []

BFS(v)


print('\n')

v1 = int(input('Вершина : ')) - 1

Vis1 = []
for i in range(len(c)):
	Vis1.append(0)

queue1 = []

BFS1(v1)

input()

