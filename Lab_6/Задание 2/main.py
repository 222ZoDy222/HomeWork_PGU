import random
import time
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

'''
G = [
[0,1,1,1,0],
[1,0,0,1,0],
[1,0,0,1,1],
[1,1,1,0,1],
[0,0,1,1,0]
]
'''

for i in range(len(G)):
    for j in range(len(G[i])):
        G[i][j] = G[j][i]
        print(G[i][j],end='\t')
    print('\n')
print('\n'*3)

def BFSD(v):
    Vis[v] = 0
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

print("---список смежности---")

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')



'''
def DFS(v):
    global count
    count += 1
    vis[v] = 1
    for i in range(len(G)):
        if(G[v][i] == 1 and vis[i] == 0):
            DFS(i)

        if(G[v][i] == 1):

            res[i] = count
    count -= 1
    if(count > res[i]):
        return
    res[v] = count
    #print(" in")


def DFS1(v):
    global count
    count += 1
    vis[v] = 1
    for i in range(len(c[v])):
        if(vis[c[v][i]] == 0):
            DFS(c[v][i])
        res[c[v][i]] = count

    count -= 1
    if(count > res[c[v][i]]):
        return
    res[v] = count

'''
def DFS(v, count):
    vis[v] = count
    for i in range(len(G)):
        if(G[v][i] == 1 and vis[i] == -1):
            DFS(i,count + 1)
        if(G[v][i] == 1 and vis[i] > count):
            DFS(i,count + 1)
    
            
v = int(input("\nВершина: ")) - 1
vis = []
for i in range(len(G)):
    vis.append(-1)

count = 0           
DFS(v,count)
print("\n")

for i in range(len(vis)):
    print(i+1,' : ' , vis[i])

#------------------------------------------------#


def DFS1(v,count):
    vis[v] = count
    for i in range(len(c[v])):
        if(vis[c[v][i]] == -1):
            DFS(c[v][i],count + 1)
        if(vis[c[v][i]] > count):
            DFS(c[v][i],count + 1)




v = int(input("\nВершина: ")) - 1

for i in range(len(vis)):
    vis[i] = -1
count = 0           


DFS1(v,count)

print("\n")
for i in range(len(vis)):
    print(i+1,' : ' , vis[i])


