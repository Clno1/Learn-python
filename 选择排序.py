def ssort(a,comp=lambda x, y: x > y):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if comp(a[i],a[j]) :
                a[i],a[j]=a[j],a[i]
    return a



n=int(input())
a=list(map(int,input().split()))
a=ssort(a)
for i in range(n):
    print(a[i],end =' ')
print()
