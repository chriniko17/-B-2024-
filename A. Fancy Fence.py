n=int(input())
for _ in range(n):
    a=int(input())
    x=360/(180-a)
    if x==int(x):
        print("YES")
    else:
        print("NO")