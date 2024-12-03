s=input()
if len(s)==0:
    print(0)
    exit()
i,j=0,1
ans=1
a=set(s[0])
while j<len(s):
    if s[j] not in a:
        a.add(s[j])
        j+=1
    else:
        a.remove(s[i])
        i+=1
    ans=max(ans,j-i)
print(max(ans,j-i))