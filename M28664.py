correct=["1","0","X","9","8","7","6","5","4","3","2"]
multiply=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
def judge(num,a):
    if a==correct[num]:
        return True
    else:
        return False
n=int(input())
for _ in range(n):
    a=input()
    ans=0
    for i in range(17):
        ans+=int(a[i])*multiply[i]
    if judge(ans%11,a[17])==True:
        print("YES")
    else:
        print("NO")