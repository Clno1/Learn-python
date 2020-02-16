
def exgcd(a,b,x,y):
    if b==0:
        return [a,1,0]
    else:
        t=exgcd(b,a%b,y,x)
        y,x=t[1],t[2]
        y-=x*(a//b)
        return [t[0],x,y]

def work(n,m,a):
    res,x,y=0,0,0
    lcm=1
    for i in range(1,n+1):
        lcm*=m[i]
    for i in range(1,n+1):
        M=lcm//m[i]
        gcd,x,y=exgcd(M,m[i],x,y)
        x=(x%m[i]+m[i])%m[i]
        res=(res+a[i]*x*M)%lcm
    return res

def main():
    n=int(input())
    m,a=[0]*(n+1),[0]*(n+1)
    for i in range(1,n+1):
        m[i],a[i]=map(int,input().split())
    print(work(n,m,a))
    

if __name__=="__main__":
    main()