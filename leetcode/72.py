class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a=[[0]*(len(word2)+1) for i in range(len(word1)+1)]
        pre=list(i for i in range(len(word2)+1))
        cur=[0]*(len(word2)+1)
        for i in range(1,len(word1)+1):
            cur[0]=i
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    cur[j]=pre[j-1]
                else:
                    cur[j]=min(pre[j],pre[j-1],cur[j-1])+1
            cur,pre=pre,cur
        return pre[len(word2)]