n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]%2==0:
        print(int(a[i]/2-1))
    else:
        print(int((a[i]-1)/2))