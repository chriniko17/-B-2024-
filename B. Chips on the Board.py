t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(min(sum(a)+n*min(b),sum(b)+n*min(a)))