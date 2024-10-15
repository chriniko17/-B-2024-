n=int(input())
i=0
while n>=2:
    if i%2==0:
        print("I hate that",end=" ")
    else:
        print("I love that",end=" ")
    i+=1
    n-=1
if i%2==0:
    print("I hate it",end=" ")
else:
    print("I love it",end=" ")