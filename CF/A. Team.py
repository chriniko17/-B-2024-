n=int(input())
ans=0
for i in range(n):
    a,b,c=map(int,input().split())
    if (a==1 and b==1) or (a==1 and c==1) or (b==1 and c==1) or (a==1 and b==1 and c==1):
        ans=ans+1
    else:continue
print(ans)