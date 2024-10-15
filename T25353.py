n,d=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
while len(a)>0:
    ans=[]
    rank=[]
    mam=a[0]
    mim=a[0]
    for i in range(len(a)):
        if mam-a[i]<=d and a[i]-mim<=d:
            ans.append(a[i])
            rank.append(i)
        mam=max(mam,a[i])
        mim=min(mim,a[i])
    ans.sort()
    rank.sort(reverse=True)
    for i in range(len(ans)):
        print(ans[i])
        a.pop(rank[i])