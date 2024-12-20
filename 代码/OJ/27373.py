m=int(input())
n=int(input())
a=list(map(int,input().split()))
def sort_key(x):
    return x/(10**(len(str(x)))-1)
a.sort(key=sort_key,reverse=True)
a=list(map(str,a))
#print(a)
dp=[0]*(m+1)
for i in range(n):
    for j in range(m,len(a[i])-1,-1):
        dp[j]=max(dp[j],int(str(dp[j-len(a[i])])+a[i]))
    #print(dp)
print(max(dp))