# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>俞天麒 物理学院</mark>



**说明：**

1）⽉考： 没参加<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

拿一个数组储存自这天之后的数的最大值，则答案就是max_rec-a的最大值

代码：

```python
a=list(map(int,input().split()))
n=len(a)
max_rec=[float("-inf")]*(len(a))
max_rec[n-1]=a[n-1]
for i in range(n-2,-1,-1):
    max_rec[i]=max(max_rec[i+1],a[i])
ans=0
for i in range(n):
    ans=max(ans,max_rec[i]-a[i])
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241205202048477](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205202048477.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

题解的思路太天才了，先把一定能烤熟且还会剩下的鸡排就放进去占位置。剩下的一定怎么滴都能烤熟（不过为什么，我自己做的时候就是这一点没想明白，一直在思考要是没占位置的了剩下的怎么办，后面想了一下感觉只能意会？确实有点感觉可能是我自己思路不够活跃）

代码：

```python
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
s=sum(a)
while True:
    if a[-1]>s/k:
        s-=a.pop()
        k-=1
    else:
        print("{:.3f}".format(s/k))
        break
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241205211142446](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205211142446.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

好巧妙的解法，构造两个数组，一个都不放会，一个允许放回一次。这个思路可以多学习一下。在答案的基础上把空间复杂度优化到O(n)

代码：

```python
a=list(map(int,input().split(",")))
n=len(a)
dp1,dp2=a[0],a[0]
ans=0
for i in range(1,n):
    dp1,dp2=max(a[i],dp1+a[i]),max(dp1,dp2+a[i])
    ans=max(ans,dp2)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241205210642432](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205210642432.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

就是烦，数据范围估计告诉我暴力能过。利用递归来枚举所有可能情况，再定义一个函数来处理每种情况的价格，然后取极小值。利用字典可以简化操作。

代码：

```python
n,m=map(int,input().split())
price=[]
coupon=[]
ans=float("inf")
for i in range(n):
    s=input().split()
    dic={}
    for j in range(len(s)):
        shop,pri=map(int,s[j].split(":"))
        dic[shop]=pri
    price.append(dic)
#print(price)
for i in range(m):
    s=input().split()
    dic={}
    for j in range(len(s)):
        ori,now=map(int,s[j].split("-"))
        dic[ori]=now
    coupon.append(dic)
#print(coupon)
cho=[0]*n
def form(x):
    if x==n:
        #print(cho)
        find_price()
        return
    else:
        for key in price[x].keys():
            cho[x]=key
            form(x+1)
def find_price():
    global n,m,ans
    shop=[0]*(m+1)
    for i in range(n):
        shop[cho[i]]+=price[i][cho[i]]
    pri=sum(shop)-50*(sum(shop)//300)
    #print(shop)
    for i in range(1,m+1):
        cut=0
        for key,value in coupon[i-1].items():
            if shop[i]>=key:
                cut=max(cut,value)
        pri-=cut
    #print(pri)
    ans=min(ans,pri)
form(0)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241205234703683](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205234703683.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

这题时间卡的超极严。。。简直是不能做任何多的一点操作，要用dijsktra算法并且还要最简化。权值判断即为从1到1为0，1到0和0到0为1。

代码：

```python
import heapq
n=int(input())
land=[]
dir=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(n):
    land.append(input())
visited=[[True]*(len(land[i])) for i in range(len(land))]
def find(x1,y1):
    pos=[]
    heapq.heappush(pos,(0,x1,y1))
    visited[x1][y1]=False
    while pos:
        step,x,y=heapq.heappop(pos)
        #print(step,x,y)
        if land[x][y]=="1" and step!=0:
            return step
        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<len(land[nx]) and visited[nx][ny]:
                visited[nx][ny]=False
                if land[nx][ny]==land[x][y] and land[x][y]!="0":
                    heapq.heappush(pos,(step,nx,ny))
                else:
                    heapq.heappush(pos,(step+1,nx,ny))
mark=False
for i in range(n):
    for j in range(len(land[i])):
        if land[i][j]=="1":
            print(find(i,j)-1)
            exit()




```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241205195056895](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205195056895.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

考虑最后一个大臣，其获得的钱数是所有人左手上的数的乘积（一个定值），除以自己左手和右手的乘积，所以要让他左手右手的乘积最大，所以就有了排序的key。不过这题很奇怪，用floor来取整会wa，用整除就可以。

代码：

```python
import math
n=int(input())
x,y=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:x[0]*x[1])
#print(a)
ans,cur=0,x
for i in range(n):
    #print(cur/a[i][1])
    ans=max(ans,(cur//a[i][1]))
    cur*=a[i][0]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241205201727761](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241205201727761.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

天哪，这次月考怎么这么难，很害怕期末考如果这么考，可能只有AC1-2.但是还是学到了很多，比如又复习了一下dijkstra算法，把模板记得更清楚了一下。但是感觉应对非模板的贪心和动规还是力不从心，思路怎么就这么死。希望期末考难度能正常一点。



