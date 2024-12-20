# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>俞天麒 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：

跟着提示走，不过提示好像有一点没有说全，就是如果a=b的情况也是先手获胜，这个加以判断一下就好了。我更关心的是提示是怎么想出来的。

有一个不太严谨的想法，就是如果a<2b的话没话说，只有一种选择；如果a>=2b的话，假设nb<=a<(n+1)b，先手既可以取nb，变成a-nb，b，然后对面继续，也可以取(n-1)b，变成a-(n-1)b，b，此时对面只能往原本是a的那里取b，又变成a-nb，b但是是自己先手，这两种情况一定有一种自己能获胜，或许可以这么解释。

代码：

```python
def solve(a,b,who):
    if a>=b*2 or a==b:
        return who
    else:
        a-=b
        return solve(max(a,b),min(a,b),who+1)
while True:
    a,b=map(int,input().split())
    if a+b==0:
        break
    else:
        if solve(max(a,b),min(a,b),0)%2==0:
            print("win")
        else:
            print("lose")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210124821334](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210124821334.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：

遍历每一层的数字，然后求和。

代码：

```python
n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
ans=float("-inf")
for i in range((n+1)//2):
    temp=0
    if n%2==1 and i==(n-1)/2:
        temp=a[i][i]
    else:
        temp=sum(a[i][i:n-i])+sum(a[n-i-1][i:n-i])
        #print(a[i][i:n-i],a[n-i-1][i:n-i],temp)
        for j in range(i+1,n-i-1):
            temp+=a[j][i]+a[j][n-i-1]
            #print(a[j][i],a[j][n-i-1])
    ans=max(temp,ans)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241210125320192](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210125320192.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

利用贪心，如果此时血量能喝，那就喝。如果不能，看看这瓶药提供的血量比之前和过的最差的比，如果现在的效果更好，那就换掉之前的。

代码：

```python
import heapq
 
n=int(input())
a=list(map(int,input().split()))
ans=[]
blood=0
for i in range(n):
    if blood+a[i]>=0:
        blood+=a[i]
        heapq.heappush(ans,a[i])
    elif ans and a[i]>ans[0]:
        temp=heapq.heappop(ans)
        heapq.heappush(ans,a[i])
        blood+=a[i]-temp
print(len(ans))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210125411956](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210125411956.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：

拿一个栈来储存放入每只猪时对应的最小值。

代码：

```python
pig=[]
min_stack=[]
cur_min=float("inf")
while True:
    try:
        s=input()
        if s[0]=="p" and s[1]=="o":
            if len(pig):
                removed=pig.pop()
                min_stack.pop()
                if min_stack:
                    cur_min=min_stack[-1]
                else:
                    cur_min=float("inf")
        if s[0]=="m":
            #print(pig)
            if len(pig)>0:
                print(cur_min)
        if s[0]=="p" and s[1]=="u":
            num=int(s[5::])
            pig.append(num)
            if num<cur_min:
                cur_min=num
                min_stack.append(num)
            else:
                min_stack.append(cur_min)
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210125705851](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210125705851.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

标准的dijkstra模板

代码：

```python
import heapq

m,n,p=map(int,input().split())
a=[[float("inf")]*(n+2) for i in range(m+2)]
dir=[[0,1],[1,0],[0,-1],[-1,0]]
for i in range(m):
    s=list(input().split())
    for j in range(len(s)):
        if s[j]!="#":
            a[i+1][j+1]=int(s[j])
def dijkstra(x1,y1,x2,y2):
    pq=[(0,x1,y1)]
    dist=[[float("inf")]*(n+2) for i in range(m+2)]
    dist[x1][y1]=0
    while pq:
        cost,x,y=heapq.heappop(pq)
        if x==x2 and y==y2:
            return cost
        else:
            for i in range(4):
                nx,ny=x+dir[i][0],y+dir[i][1]
                if dist[nx][ny]>dist[x][y]+abs(a[nx][ny]-a[x][y]):
                    dist[nx][ny]=dist[x][y]+abs(a[nx][ny]-a[x][y])
                    heapq.heappush(pq,(cost+abs(a[nx][ny]-a[x][y]),nx,ny))
    return float("inf")
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    x1,y1,x2,y2=x1+1,y1+1,x2+1,y2+1
    if a[x1][y1]==float("inf") or a[x2][y2]==float("inf"):
        print("NO")
        continue
    ans=dijkstra(x1,y1,x2,y2)
    if ans==float("inf"):
        print("NO")
    else:
        print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210125902102](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210125902102.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：

这题只要能走到都好说，最难的是走不到的情况。查了gpt才知道可以在visited标记数组上加一个时间维度。

代码：

```python
from collections import  deque
t=int(input())
dir=[[-1,0],[0,-1],[1,0],[0,1]]
for _ in range(t):
    r,c,k=map(int,input().split())
    a=[[0]*(c) for i in range(r)]
    x1,y1,x2,y2=0,0,0,0
    for i in range(r):
        s=input()
        for j in range(c):
            if s[j]=="S":
                x1,y1=i,j
            elif s[j]=="#":
                a[i][j]=1
            elif s[j]=="E":
                x2,y2=i,j
    visit=[[[True]*c for i in range(r)] for j in range(k)]
    def find(x1,y1,x2,y2,k):
        pos=deque([(0,x1,y1)])
        visit[0][x1][y1]=False
        while pos:
            t,i,j=pos.popleft()
            if i==x2 and j==y2:
                return t
            nt=t+1
            for di in dir:
                nx,ny=i+di[0],j+di[1]
                if 0<=nx<r and 0<=ny<c:
                    if a[nx][ny]==1 and nt%k!=0:
                        continue
                    if visit[nt%k][nx][ny]:
                        pos.append((nt,nx,ny))
                        visit[nt%k][nx][ny]=False
        return "Oop!"
    print(find(x1,y1,x2,y2,k))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241210130123014](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241210130123014.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

就先完成每日选做吧，毕竟这也不是什么善茬，很多都要去看题解或者询问gpt，能力还是有点欠缺。等每日选做到200了我们也快期末了刚好就此收手。



