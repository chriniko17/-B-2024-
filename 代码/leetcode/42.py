height=list(map(int,input().split()))
left,right=0,len(height)-1
maxl,maxr=0,0
ans=0
while left<right:
    if height[left]<height[right]:
        if height[left]>=maxl:
            maxl=height[left]
        else:
            ans+=maxl-height[left]
        left+=1
    else:
        if height[right]>=maxr:
            maxr=height[right]
        else:
            ans+=maxr-height[right]
        right-=1
print(ans)