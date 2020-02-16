
def mul(a,b,P):
    ret=[[0 for _ in range(3)] for _ in range(3)]
    for i in range(1,3):
        for j in range(1,3):
            for k in range(1,3):
                ret[i][j]=(ret[i][j]+a[i][k]*b[k][j]%P)%P
    return ret

def main():
    n=int(input())
    P=int(1e9+7)
    a=[[0 for _ in range(3)]for _ in range(3)]
    b=[[0 for _ in range(3)]for _ in range(3)]
    a[1][1],a[1][2]=0,1
    b[1][1],b[1][2],b[2][1],b[2][2]=0,1,1,1
    while n:
        if n&1:
            a=mul(a,b,P)
        b=mul(b,b,P)
        n>>=1
    print(a[1][1])

if __name__=="__main__":
    main()