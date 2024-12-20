t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(enumerate(map(int,input().split())))
    b=list(map(int,input().split()))
    sorted_a=list(enumerate(sorted(a,key=lambda x:x[1])))
    a1=sorted(sorted_a,key=lambda x:x[1][0])
    sorted_b=sorted(b)
    for i in range(n):
        print(sorted_b[a1[i][0]],end=" ")