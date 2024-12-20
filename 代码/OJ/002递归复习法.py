m=int(input())
review=[0]*26
review[1],review[2]=1,2
for i in range(3,26):
    review[i]=review[i-1]+review[i-2]+i
for _ in range(m):
    n=int(input())
    print(review[n])