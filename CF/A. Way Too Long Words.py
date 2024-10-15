n=int(input())
for _ in range(n):
    a=input()
    if len(a)<=10:
        print(a)
    else:
        print(a[0]+str(len(a)-2)+a[len(a)-1])