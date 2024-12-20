n=int(input())
a=list(map(int,input().split()))
aco={}
nums=sorted(list(set(a)))
for num in a:
    if num in aco:
        aco[num]+=1
    else:
        aco[num]=1
#print(aco,nums)
ch,no=aco[nums[0]]*nums[0],0
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]==1:
        ch,no=no+aco[nums[i]]*nums[i],max(no,ch)
    else:
        ch,no=max(no,ch)+aco[nums[i]]*nums[i],max(no,ch)
print(max(ch,no))