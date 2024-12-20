n=int(input())
a=[]
for i in range(n):
    c,d=map(int,input().split())
    a.append([c,d])
a.sort(key=lambda x:x[0])
#print(a)
for i in range(n-1):
    if a[i][1]>a[i+1][1]:
        print("Happy Alex")
        exit()
print("Poor Alex")