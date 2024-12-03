import bisect
n,t=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)<t:
    print(0)
else:
    judge=set()
    for element in a:
        temp=set()
        for element2 in judge:
            temp.add(element2+element)
        judge.add(element)
        judge=judge|temp
    judge=sorted(list(judge))
    #print(judge)
    print(judge[bisect.bisect_left(judge,t)])
