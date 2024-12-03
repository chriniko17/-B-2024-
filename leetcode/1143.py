class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pre,cur=[0]*(len(text2)+1),[0]*(len(text2)+1)
        ans=0
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    cur[j]=max(cur[j],pre[j-1]+1)
                else:
                    cur[j]=max(pre[j],cur[j-1])
                if cur[j]>ans:
                    ans=cur[j]
            pre,cur=cur,pre
        return ans