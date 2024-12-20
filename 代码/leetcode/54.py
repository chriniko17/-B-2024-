matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
i,j=0,0
ans=[]
used=[[True]*len(matrix[0]) for i in range(len(matrix))]
mark=1
while True:
    mark1=True
    for k in range(len(matrix)):
        for l in range(len(matrix[0])):
            if used[k][l]==True:
                mark1=False
    if mark1:
        break
    #print(i,j)
    ans.append(matrix[i][j])
    used[i][j]=False
    if mark==1:
        if j==len(matrix[0])-1:
            mark=2
            i+=1
        else:
            if used[i][j+1]==False:
                mark=2
                i+=1
            else:
                j+=1
    elif mark==2:
        if i==len(matrix)-1:
            mark=-1
            j-=1
        else:
            if used[i+1][j]==False:
                mark=-1
                j-=1
            else:
                i+=1
    elif mark==-1:
        if j==0:
            mark=-2
            i-=1
        else:
            if used[i][j-1]==False:
                mark=-2
                i-=1
            else:
                j-=1
    else:
        if used[i-1][j]==False:
            mark=1
            j+=1
        else:
            i-=1
print(ans)