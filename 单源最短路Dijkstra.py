from queue import Queue,PriorityQueue

class pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __lt__(self, other):     
        return self.y<other.y

class edge:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


def Dijkstra(n,s,edges):
    pq = PriorityQueue()
    vis=[0]*(n+1)
    dis=[0x3f3f3f3f]*(n+1)
    dis[s]=0
    pq.put(pair(s,0))
    while not pq.empty():
        now=pq.get()
        if vis[now.x]==1:
            continue
        vis[now.x]=1
        for e in edges[now.x]:
            if dis[now.x]+e.z<dis[e.y]:
                dis[e.y]=dis[now.x]+e.z
                pq.put(pair(e.y,dis[e.y]))
    INF=(1<<31)-1
    for i in range(1,n+1):
        print(dis[i] if dis[i]!=0x3f3f3f3f else INF,end=' ')

def main():
    n,m,s=map(int,input().split())
    edges=[]
    for _ in range(n+1):
        edges.append([])
    for _ in range(m):
        x,y,z=map(int,input().split())
        edges[x].append(edge(x,y,z))
    Dijkstra(n,s,edges)


if __name__=="__main__":
    main()