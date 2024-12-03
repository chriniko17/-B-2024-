class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        if target not in set(nums):
            return [-1,-1]
        else:
            i,j=0,len(nums)
            while i<j:
                mid=(i+j)//2
                if target>nums[mid]:
                    i=mid+1
                else:
                    j=mid
            a=[i]
            i,j=0,len(nums)
            while i<j:
                mid=(i+j)//2
                if target<nums[mid]:
                    j=mid
                else:
                    i=mid+1
            a.append(i-1)
            return a
