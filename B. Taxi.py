import math
n=int(input())
a=list(map(int,input().split()))
one=a.count(1)
two=a.count(2)
three=a.count(3)
ans=a.count(4)
if three>=one:
    print(ans+three+math.ceil(two/2))
else:
    ans+=three
    one-=three
    if two%2==0:
        print(ans+two//2+math.ceil(one/4))
    else:
        ans+=two//2
        print(ans+math.ceil((one-2)/4)+1)