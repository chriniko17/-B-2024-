s=input()
start,end=0,0
def expand(i,j):
    global s
    while i>=0 and j<=len(s)-1 and s[i]==s[j]:
        i-=1
        j+=1
    return i+1,j-1
for i in range(len(s)-1):
    left,right=expand(i,i)
    if right-left>end-start:
        start,end=left,right
    left,right=expand(i,i+1)
    if right - left > end - start:
        start, end = left, right
print(s[start:end+1])
