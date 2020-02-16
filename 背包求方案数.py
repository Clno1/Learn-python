
def Dp(n,m,a):
    dp=[]
    for _ in range(n+1):
        dp.append([0]*(m+1))
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(0,m+1):
            dp[i][j]=dp[i-1][j]
            if a[i]<=j:
                dp[i][j]+=dp[i-1][j-a[i]]
    return dp[n][m]

def main():
    n,m=map(int,input().split())
    a=[]
    a=list(map(int,input().split()))
    a[1:]=a[0:]
    print(a)
    print(Dp(n,m,a))

if __name__=="__main__":
    main()