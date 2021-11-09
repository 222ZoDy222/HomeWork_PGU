import random
G = []
c = []
N1 = int(input("First Matrix: "))
chance = [0,0,0,1,1,1,1,1,1,1]
for i in range(N1):
	G.append([])
	for j in range(N1):
		G[i].append(random.choice(chance))
		if(i == j):
			G[i][j] = 0
			
for i in range(N1):
	for j in range(N1):
		G[i][j] = G[j][i]
		print(G[i][j],end='\t')
	print('\n')
print('\n'*3)

print("---список смежности---")

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')



def BFSD(v):
	Vis[v] = 1
	queue.append(v)
	while(bool(queue)):
		s = queue[0]
		
		queue.pop(0)
		for i in range(len(G)):
			if(G[s][i] == 1 and Vis[i] == -1):
				queue.append(i)
				Vis[i] = 1 + Vis[s]


queue = []
Vis = []
for i in range(len(G)):
	Vis.append(-1)

v = int(input('\nВершина : ')) - 1
print("\n")
BFSD(v)

for i in range(len(Vis)):
	print(i+1 ,' : ' , Vis[i])


























