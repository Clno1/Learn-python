class edge:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __lt__(self,rhs):
        return self.z<rhs.z

def getfa(fa,x):
    if x==fa[x]:
        return x
    else:
        fa[x]=getfa(fa,fa[x])
        return fa[x]

def Kruskal(n,m,edges):
    edges.sort()
    fa=[0]*(n+1)
    for i in range(1,n+1):
        fa[i]=i
    num,ret=0,0
    for e in edges:
        fx=getfa(fa,e.x)
        fy=getfa(fa,e.y)
        if fx==fy:
            continue
        num+=1
        fa[fx]=fa[fy]
        ret+=e.z
    return ret if num==n-1 else 0
    
def getedge():
    x,y,z=input().split()
    return edge(int(x),int(y),int(z))

def main():
    n,m=input().split()
    n=int(n) 
    m=int(m)
    edges=[]
    for i in range(m):
        edges.append(getedge())
    ans=Kruskal(n,m,edges)
    if ans>0:
       print(ans) 
    else:
       print("orz")

if __name__=="__main__":
    main()