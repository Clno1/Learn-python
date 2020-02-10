import random

def qsort(a,l,r,cmp=lambda x,y : x<y):
    if r-l<=1:
        return
    #随机化选取基准:
    ram=random.randint(l,r-1)
    a[ram],a[r-1]=a[r-1],a[ram]

    std=a[r-1]
    idx=l
    for i in range(l,r-1):
        if (cmp(a[i],std)):
            a[idx],a[i]=a[i],a[idx]
            idx+=1
    a[idx],a[r-1]=a[r-1],a[idx]
    idx+=1
    qsort(a,l,idx-1)
    qsort(a,idx,r)


def main():
    n=int(input())
    a=list(map(int,input().split()))
    qsort(a,0,n)
    for val in a:
        print(val,end=" ")
    print()

if __name__=='__main__':
    main()
