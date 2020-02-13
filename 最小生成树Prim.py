
def Prim(n,m,mp):
    dis=[0x3f3f3f3f]*(n+1)
    vis=[0]*(n+1)
    dis[1]=0
    for _ in range(n):
        Min=0
        for i in range(1,n+1):
            if vis[i]==0 and (Min==0 or dis[Min]>dis[i]):
                Min=i
        if (dis[Min]==0x3f3f3f3f):
            return 0
        vis[Min]=1
        for i in range(1,n+1):
            if (vis[i]==1 or i==Min):
                continue
            dis[i]=min(dis[i],mp[i][Min])
    ret=0
    for i in range(1,n+1):
        ret+=dis[i]
    return ret

def main():
    n,m=map(int,input().split())
    mp=[[0x3f3f3f3f for _ in range(n+1)] for _ in range(n+1)]
    
    for _ in range(m):
        x,y,z=map(int,input().split())
        mp[x][y]=mp[y][x]=min(mp[x][y],z)
    
    ans=Prim(n,m,mp)
    if ans>0:
       print(ans) 
    else:
       print("orz")

if __name__=="__main__":
    main()