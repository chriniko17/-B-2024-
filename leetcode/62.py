m=int(input())
n=int(input())
a = [1] * n
for i in range(1, m):
    for j in range(1, n):
        a[j] = a[j - 1] + a[j]
print(a[n-1])