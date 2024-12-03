t=int(input())
for _ in range(t):
    e,f=map(int,input().split())
    g=f-e
    ans=[float("inf")]*(g+1)
    ans[0]=0
    n=int(input())
    for i in range(n):
        p,w=map(int,input().split())
        for j in range(w,g+1):
            ans[j]=min(ans[j],ans[j-w]+p)
        #print(ans)
    if ans[g]==float("inf"):
        print("This is impossible.")
    else:
        print("The minimum amount of money in the piggy-bank is "+str(ans[g])+".")