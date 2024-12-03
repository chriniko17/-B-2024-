# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>俞天麒 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

把n个塔从A搬到C，等效于解决把n-1个搬到B，再把第n个搬到C，再把B上的n-1个搬到C，所以这里定义solve函数，意思是把x个从a指标搬到b指标，c是储存另一个塔的指标的东西。

代码：

```python
def solve(x,a,b,c):
    if x==1:
        print(a+"->"+b)
    else:
        solve(x-1,a,c,b)
        print(a+"->"+b)
        solve(x-1,c,b,a)
def count(x):
    if x==1:
        return 1
    else:
        return 1+2*count(x-1)
n=int(input())
print(count(n))
solve(n,"A","C","B")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030085625465](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030085625465.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

全排列思路就是在每个位置遍历一遍能用的数，如果能用就进一步研究下一个位置，所以这里拿了一个used列表标记每个数有没有用，注意用完了给他复原。当已经把1-n都放进去的时候，即指标为n+1时进行输出。

代码：

```python
import math
n=int(input())
used=[True]*(n+1)
ans=[0]*(n+1)
count=0
def find(x):
    global count
    if x==n+1:
        count+=1
        print(" ".join(map(str,ans[1:n+1])),end="")
        if count!=math.factorial(n):
            print()
    else:
        for i in range(1,n+1):
            if used[i]:
                ans[x]=i
                used[i]=False
                find(x+1)
                used[i]=True
find(1)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241030092140491](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030092140491.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

本质就是求最长的降序子序列，用ans[i]标记以i结尾的最长子序列的长度，对于每一个i，应该要去遍历前面的每个数，如果a[j]比a[i]大，那么ans[i]就在自己的值和ans[j]+1中取极大值，最后求这些ans的极大值就好了

代码：

```python
k=int(input())
a=list(map(int,input().split()))
ans=[1]*k
for i in range(k):
    for j in range(i):
        if a[j]>=a[i]:
            ans[i]=max(ans[i],ans[j]+1)
print(max(ans))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030092415530](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030092415530.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

一个01背包问题，我先看了01背包的模板之后才会的

代码：

```python
n,b=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
ans=[0]*(b+1)
for i in range(n):
    for j in range(b,w[i]-1,-1):
        ans[j]=max(ans[j],ans[j-w[i]]+p[i])
    #print(ans)
print(ans[b])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030092520755](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030092520755.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

我打算一口气把92个解都生成了，然后看输入那个数调用哪个解。具体方法和全排列差不多，只不过遍历的时候要附加一个与之前的数的条件，即不能相等，也不能差等于位置指标的差。还要注意放入ans的时候深浅拷贝的问题，被这个坑了。复制数组的时候不要乱等于等过去，用列表推导式实现深拷贝。

代码：

```python
ans=[]
sol=[0]*9
used=[True]*9
def find(x):
    global ans
    if x==9:
        temp=[sol[i+1] for i in range(8)]
        ans.append(temp)
    else:
        for i in range(1,9):
            if used[i]:
                mark=True
                for j in range(1,x):
                    if i==sol[j] or abs(i-sol[j])==abs(x-j):
                        mark=False
                        break
                if mark:
                    sol[x]=i
                    used[i]=False
                    find(x+1)
                    used[i]=True
                #print(sol,x)
find(1)
#print(ans)
n=int(input())
for _ in range(n):
    b=int(input())
    print("".join(map(str,ans[b-1])))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030125710599](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030125710599.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

用ans表示切到i时最大的段落数。然后推导式大概是ans[i]=max(ans[i-a],max[i-b],max[i-c])+1，但是要注意这三个不能为0，否则意味切不到（实际上我这里好像可以更简单，初始赋值的时候全部弄成负无限大），然后给初值为ans[a]=ans[b]=ans[c]=1就行了。然后还要注意n是否会小于a,b,c的情况，单独判断一下。实际代码好像有点麻烦，但是能过就算了。

代码：

```python
n,a,b,c=map(int,input().split())
ans=[0]*(n+1)
for i in range(n+1):
    if i>=a and ans[i-a]!=0:
        ans[i]=max(ans[i],ans[i-a]+1)
    elif i==a:
        ans[i]=max(ans[i],1)
    if i>=b and ans[i-b]!=0:
        ans[i]=max(ans[i],ans[i-b]+1)
    elif i==b:
        ans[i]=max(ans[i],1)
    if i>=c and ans[i-c]!=0:
        ans[i]=max(ans[i],ans[i-c]+1)
    elif i==c:
        ans[i]=max(ans[i],1)
    #print(ans)
print(ans[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030130129328](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241030130129328.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉dp还是很神奇，见了更多的模型，也有了更深层次的思路，慢慢开始适应计算机思维吧。希望之后的题目能让我收获更多。马上期中周了，每日选做希望适时降低一点量，好给我们备考。



