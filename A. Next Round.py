import sys
n,k=map(int,input().split())
score=list(map(int,input().split()))
ans=0
if score[0]==0:
    print("0")
elif score[k-1]!=0:
    for i in range(k-1,n):
        if score[i]>=score[k-1] and score[i]>0:
            ans=ans+1
        else: break
    print(ans+k-1)
else:
    for i in range(k):
        if score[i]!=0 and score[i+1]==0:
            print(i+1)
            sys.exit()
