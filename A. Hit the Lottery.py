n=int(input())
a=n//100
n=n-100*a
b=n//20
n=n-20*b
c=n//10
n=n-10*c
d=n//5
n=n-5*d
print(a+b+c+d+n)