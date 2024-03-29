from collections import deque

n,L,R=list(map(int,input().split()))


for i in range(n):
    graph=list(map(int,input().split()))



dx=[0,0,-1,1]
dy=[1,-1,0,0]

result = 0
def process(x,y,index):
    united=[]
    united.append(x,y)

    q=deque()
    q.append((x,y))
    union[x][y]=index
    count =1
    summary = graph[x][y]

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            if 0<= nx < n and 0<= ny<n and union[nx][ny] == -1:
                if L <= abs(graph[nx][ny]-graph[x][y]) <= R:
                    q.append((nx,ny))
                    union[nx][ny]=index
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx,ny))
    for i,j in united:
        graph[i][j]=summary//count
    return count

total_count = 0

while True:
    union=[[-1]*n for _ in range(n)]
    index =0
    for i in range(n):
        for j in range(n):
            if union[i][j]== -1:
                process(i,j,index)
                index+=1
