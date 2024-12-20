import sys
sys.setrecursionlimit(300000000)
def count(x,left,right):
    if left<right:
        middle=(left+right)//2
        return count(x,left,middle)+count(x,middle+1,right)+judge(x[left:middle+1],x[middle+1:right+1])
    else:
        return 0
def judge(a,b):
    c=sorted(a)
    d=sorted(b)
    i,j=0,0
    ans=0
    while i<len(c):
        if j<len(d):
            if d[j]<c[i]:
                j+=1
            else:
                i+=1
                ans+=j
        else:
            i+=1
            ans+=j
    return ans
n=int(input())
a=list(map(int,input().split()))
#print(judge(a[0:(n-1)//2+1],a[(n-1)//2+1:n]),a[0:(n-1)//2+1],a[(n-1)//2+1:n])
print(count(a,0,n-1))