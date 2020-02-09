def gsort(a):
    if (len(a)==1):
        return a
    mid=len(a) // 2
    left=a[:mid]
    right=a[mid:]
    left=gsort(left)
    right=gsort(right)
    return merge(left,right)

def merge(left,right):
    ret=[]
    lidx,ridx=0,0
    while lidx<len(left) and ridx<len(right):
        if (ridx==len(right) or left[lidx]<right[ridx]):
            ret.append(left[lidx])
            lidx+=1
        else:
            ret.append(right[ridx])
            ridx+=1
    ret+=left[lidx:]
    ret+=right[ridx:]
    return ret

n=int(input())
a=list(map(int,input().split()))
a=gsort(a)
for i in range(n):
    print(a[i],end =' ')
print()
