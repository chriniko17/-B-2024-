q=int(input())
seg=dict()
cur=set()
min_right,max_left=float("inf"),float("-inf")
for _ in range(q):
    s,l,r=input().split()
    l,r=int(l),int(r)
    if s=="+":
        min_right=min(min_right,r)
        max_left=max(max_left,l)
        if (l,r) in seg:
            seg[(l,r)]+=1
        else:
            seg[(l,r)]=1
    else:
        if seg[(l,r)]>1:
            seg[(l,r)]-=1
        else:
            seg.pop((l,r))
            if r==min_right:
                min_right=float("inf")
                for key in seg.keys():
                    min_right=min(min_right,key[1])
            if l==max_left:
                max_left=float("-inf")
                for key in seg.keys():
                    max_left=max(max_left,key[0])
    if max_left>min_right:
        print("YES")
    else:
        print("NO")