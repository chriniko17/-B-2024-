import math
for i in range(5):
    line=list(map(int,input().split()))
    for j in range(5):
        if line[j]==1:
            a,b=i,j
        else:continue
print(abs(a-2)+abs(b-2))