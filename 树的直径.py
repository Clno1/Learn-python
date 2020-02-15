
def dfs(G,x,fa,d1):
    for y in G[x]:
        if y==fa:
            continue
        d1[y]=d1[x]+1
        dfs(G,y,x,d1)

def main():
    n=int(input())
    G=[]
    for _ in range(n+1):
        G.append([])
    for _ in range(n-1):
        x,y=map(int,input().split())
        G[x].append(y)
        G[y].append(x)
    d1=[0]*(n+1)
    d1[1]=1
    dfs(G,1,0,d1)
    
    p=0
    for i in range(1,n+1):
        if d1[i]>d1[p]:
            p=i
    
    d2=[0]*(n+1)
    d2[p]=1
    dfs(G,p,0,d2)

    q=0
    for i in range(1,n+1):
        if d2[i]>d2[q]:
            q=i
    
    print("树的直径两端：%d  %d，长度：%d\n" % (p,q,d2[q]))

if __name__=="__main__":
    main()