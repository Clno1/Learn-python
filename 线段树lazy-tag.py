class segtree:
    def __init__(self,n):
        self.n=n
        self.sum=[0]*(n<<2)
        self.tag=[0]*(n<<2)

    def pushup(self,rt):
        self.sum[rt]=self.sum[rt<<1]+self.sum[rt<<1|1]

    def pushdown(self,rt,l,r):
        if self.tag[rt]==0:
            return
        lc,rc=rt<<1,rt<<1|1
        mid=(l+r)//2
        self.sum[lc]+=self.tag[rt]*(mid-l+1)
        self.tag[lc]+=self.tag[rt]
        self.sum[rc]+=self.tag[rt]*(r-mid)
        self.tag[rc]+=self.tag[rt]
        self.tag[rt]=0

    def buildtree(self,rt,l,r,a):
        if l==r:
            self.sum[rt]=a[l]
            self.tag[rt]=0
            return
        mid=(l+r)//2
        self.buildtree(rt<<1,l,mid,a)
        self.buildtree(rt<<1|1,mid+1,r,a)
        self.tag[rt],self.sum[rt]=0,0
        self.pushup(rt)

    def update(self,rt,l,r,ql,qr,v):
        if ql<=l and r<=qr:
            self.sum[rt]+=(r-l+1)*v
            self.tag[rt]+=v
            return
        self.pushdown(rt,l,r)
        mid=(l+r)//2
        if ql<=mid:
            self.update(rt<<1,l,mid,ql,qr,v)
        if qr>mid:
            self.update(rt<<1|1,mid+1,r,ql,qr,v)
        self.pushup(rt)

    def query(self,rt,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.sum[rt]
        self.pushdown(rt,l,r)
        mid=(l+r)//2
        ret=0
        if ql<=mid:
            ret+=self.query(rt<<1,l,mid,ql,qr)
        if qr>mid:
            ret+=self.query(rt<<1|1,mid+1,r,ql,qr)
        return ret


def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a[1:]=a[:]
    s=segtree(n)
    s.buildtree(1,1,n,a)
    for _ in range(m):
        opt=[]
        opt=list(map(int,input().split()))
        if opt[0]==1:
            s.update(1,1,n,opt[1],opt[2],opt[3])
        else:
            print(s.query(1,1,n,opt[1],opt[2]))

if __name__=="__main__":
    main()