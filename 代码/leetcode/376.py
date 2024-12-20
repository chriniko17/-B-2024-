nums=list(map(int,input().split()))
if len(nums)==0 or len(nums)==1:
    print(len(nums))
else:
    sub=[0]*(len(nums)-1)
    for i in range(len(nums)-1):
        sub[i]=nums[i]-nums[i+1]
    if sub.count(0)==len(sub):
        print(1)
        exit()
    ans=[1]*(len(nums)-1)
    for i in range(len(nums)-1):
        for j in range(i):
            if sub[j]*sub[i]<0:
                ans[i]=max(ans[i],ans[j]+1)
    print(max(ans)+1)