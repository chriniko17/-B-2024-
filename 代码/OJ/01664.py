t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    ans=set()
    temp=[]
    def put(p, q):
        if q==1:
            ans.add(tuple(sorted(temp+[p])))
            return
        else:
            for i in range(p+1):
                temp.append(i)
                put(p-i,q-1)
                temp.pop()
    put(m,n)
    #print(ans)
    print(len(ans))