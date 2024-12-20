ans=[]
sol=[0]*9
used=[True]*9
def find(x):
    global ans
    if x==9:
        temp=[sol[i+1] for i in range(8)]
        ans.append(temp)
    else:
        for i in range(1,9):
            if used[i]:
                mark=True
                for j in range(1,x):
                    if i==sol[j] or abs(i-sol[j])==abs(x-j):
                        mark=False
                        break
                if mark:
                    sol[x]=i
                    used[i]=False
                    find(x+1)
                    used[i]=True
                #print(sol,x)
find(1)
#print(ans)
n=int(input())
for _ in range(n):
    b=int(input())
    print("".join(map(str,ans[b-1])))