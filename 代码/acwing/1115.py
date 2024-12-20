def solve(a,b,who):
    if a>=b*2 or a==b:
        return who
    else:
        a-=b
        return solve(max(a,b),min(a,b),who+1)
while True:
    a,b=map(int,input().split())
    if a+b==0:
        break
    else:
        if solve(max(a,b),min(a,b),0)%2==0:
            print("win")
        else:
            print("lose")
