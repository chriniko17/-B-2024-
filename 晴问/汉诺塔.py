def solve(x,a,b,c):
    if x==1:
        print(a+"->"+b)
    else:
        solve(x-1,a,c,b)
        print(a+"->"+b)
        solve(x-1,c,b,a)
def count(x):
    if x==1:
        return 1
    else:
        return 1+2*count(x-1)
n=int(input())
print(count(n))
solve(n,"A","C","B")