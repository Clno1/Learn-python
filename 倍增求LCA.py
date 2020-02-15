from queue import Queue,LifoQueue,PriorityQueue

class Tree:
    def __init__(self,n,rt):
        self.n=n
        self.rt=rt
        self.G,self.fa=[],[]
        for _ in range(n+1):
            self.G.append([])
            self.fa.append([0]*21)
        self.dep=[0]*(n+1)
   
    def bfs(self):
        self.dep[self.rt]=1
        q=Queue()
        q.put(self.rt)
        while not q.empty():
            x=q.get()
            for y in self.G[x]:
                if self.dep[y]>0:
                    continue
                self.dep[y]=self.dep[x]+1
                self.fa[y][0]=x
                for i in range(1,20):
                    self.fa[y][i]=self.fa[self.fa[y][i-1]][i-1]
                q.put(y)

    def LCA(self,x,y):
        if self.dep[x]<self.dep[y]:
            x,y=y,x
        for i in range(20,-1,-1):
            if self.dep[self.fa[x][i]]>=self.dep[y]:
                x=self.fa[x][i]
        if x==y:
            return x
        for i in range(20,-1,-1):
            if self.fa[x][i]!=self.fa[y][i]:
                x,y=self.fa[x][i],self.fa[y][i]
        return self.fa[x][0]


def main():
    n,m,rt=map(int,input().split())
    tree=Tree(n,rt)
    for _ in range(n-1):
        x,y=map(int,input().split())
        tree.G[x].append(y)
        tree.G[y].append(x)
    tree.bfs()
    for _ in range(m):
        x,y=map(int,input().split())
        print(tree.LCA(x,y))


if __name__=="__main__":
    main()