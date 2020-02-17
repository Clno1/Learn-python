from queue import Queue,PriorityQueue

class Dinic:
    def __init__(self,n,m,s,t):
        self.n,self.s,self.t=n,s,t

        self.cnt=1
        self.head=[0]*(n+1)
        self.nxt=[0]*(m<<2)
        self.to=[0]*(m<<2)
        self.cap=[0]*(m<<2)
        self.cur,self.dep=[0]*(n+1),[0]*(n+1)

    def add_edge(self,x,y,z):
        self.cnt+=1
        self.nxt[self.cnt]=self.head[x]
        self.to[self.cnt]=y
        self.cap[self.cnt]=z
        self.head[x]=self.cnt

    def bfs(self):
        self.dep=[0]*(self.n+1)
        q=Queue()
        self.dep[self.s]=1
        q.put(self.s)
        while not q.empty():
            x=q.get()
            i=self.head[x]
            while i>0:
                if self.dep[self.to[i]]==0 and self.cap[i]>0:
                    self.dep[self.to[i]]=self.dep[x]+1
                    q.put(self.to[i])
                i=self.nxt[i]
        return self.dep[self.t]

    def dfs(self,x,lim):
        if x==self.t or lim==0:
            return lim
        ret=0
        i=self.cur[x]
        while i:
            if self.dep[x]+1==self.dep[self.to[i]] and self.cap[i]>0:
                flow=self.dfs(self.to[i],min(lim,self.cap[i]))
                if flow>0:
                    self.cap[i]-=flow
                    self.cap[i^1]+=flow
                    ret+=flow
                    lim-=flow
                    if lim==0:
                        break
            self.cur[x]=i
            i=self.nxt[i]
        return ret

    def dinic(self):
        maxflow=0
        while self.bfs()>0:
            for i in range(0,self.n+1):
                self.cur[i]=self.head[i]
            while 1:
                flow=self.dfs(self.s,0x3f3f3f3f)
                maxflow+=flow
                if flow<=0:
                    break
        return maxflow

def main():
    n,m,s,t=map(int,input().split())
    mp=Dinic(n,m,s,t)
    for _ in range(m):
        x,y,z=map(int,input().split())
        mp.add_edge(x,y,z)
        mp.add_edge(y,x,0)
    print(mp.dinic())

if __name__=="__main__":
    main()