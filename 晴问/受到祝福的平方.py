n=input()
mark=False
def cut(i):
    #print(i)
    global n,mark
    if i==len(n):
        mark=True
        return
    else:
        for j in range(i,len(n)):
            #print(n[i:j+1],i,j)
            if int(n[i:j+1])**0.5==int(int(n[i:j+1])**0.5) and int(n[i:j+1])!=0:
                cut(j+1)
cut(0)
if mark:
    print("Yes")
else:
    print("No")