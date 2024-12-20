n,k=map(int,input().split())
a=list(map(int,input().split()))
vote=dict()
for i in range(n):
    if a[2*i] not in vote:
        vote[a[2*i]]=[a[2*i+1]]
    else:
        vote[a[2*i]].append(a[2*i+1])
s=set(map(int,input().split()))
can=dict()
times=sorted(list(vote.keys()))
ans=0
#print(vote)
cur_min,cur_max=0,0
for i in range(len(times)-1):
    for element in vote[times[i]]:
        if element in can:
            can[element]+=1
        else:
            can[element]=1
        if element in s and can[element]-1==cur_min:
            cur_min=float("inf")
            for si in s:
                if si not in can:
                    cur_min=0
                    break
                else:
                    cur_min=min(cur_min,can[si])
        elif element not in s and can[element]-1==cur_max:
            cur_max+=1
    if cur_min>cur_max:
        ans+=times[i+1]-times[i]
print(ans)