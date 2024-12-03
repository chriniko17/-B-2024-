# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by 俞天麒 物理学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：

先排序，然后顺着从最小的开始买，注意买到单价为0时停止

代码

```python
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
k=n
for i in range(n):
    if a[i]>=0:
        k=i
        break
print(-sum(a[0:min(m,k)]))


```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241015101654328](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015101654328.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：

从最大的开始拿，到价格超过总数一半为止

代码

```python
n=int(input())
m=list(sorted(map(int,input().split()),reverse=True))
tot=sum(m)
o=0
#print(m,tot)
for i in range(n):
    o=o+m[i]
    if o>tot/2:
        print(i+1)
        exit()

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241015101831918](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015101831918.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

最小的情况肯定是要么全堆在最小的那一行然后列都取过去，要么全堆在列最小的那一行然后所有行取过去

代码

```python
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(min(sum(a)+n*min(b),sum(b)+n*min(a)))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015102012886](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015102012886.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

4个人的组肯定要一辆车，3人组也肯定要一辆车，接着对1人组能不能全部塞进3人组的车进行分类。若能，那就只用考虑2人组，不能再对2人组的组数奇偶进行分类，决定1人组能不能塞2组进2人组的车

代码

```python
import math
n=int(input())
a=list(map(int,input().split()))
one=a.count(1)
two=a.count(2)
three=a.count(3)
ans=a.count(4)
if three>=one:
    print(ans+three+math.ceil(two/2))
else:
    ans+=three
    one-=three
    if two%2==0:
        print(ans+two//2+math.ceil(one/4))
    else:
        ans+=two//2
        print(ans+math.ceil((one-2)/4)+1)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015102407491](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015102407491.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

若一个整数只有3个整除数，意味着其一定是一个完全平方数，且其平方根为质数。这题数据量很大，若每个数据都走一遍判断质数流程会超时，所以要先把范围内的所有质数生成出来。

代码

```python
m=1000000
a=[i for i in range(m+1)]
for i in range(2,int(m**0.5)+1):
    if a[i]!=0:
        k=i
        while k+i<=m:
            k+=i
            a[k]=0
s=set(a)
s.remove(0)
s.remove(1)
n=int(input())
b=list(map(int,input().split()))
for j in range(n):
    if b[j]**0.5!=int(b[j]**0.5):
        print("NO")
    elif int(b[j]**0.5) in s:
        print("YES")
    else:
        print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015102425322](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015102425322.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

难点在于前几位相同但是位数不同的排序，排序规则应该是将位数较小的数字重复自身直到与较大的位数相同时再排序。所以我选择直接将全部的数字循环至最大位数，然后统一排序。

10.15下午更新：理论上排序的过程应该要循环无数次，只循环1次不严谨，根据助教的提示利用除以999……变成无限循环小数后进行比较，这个思路太天才了

代码

```python
n=int(input())
a=list(input().split())
a.sort()
lmax=max(len(a[i]) for i in range(n))
c=[]
for i in range(n):
    temp=a[i]*int(lmax/len(a[i])+1)
    c.append([a[i],temp[0:lmax:]])
c.sort(key=lambda x:x[1])
#print(c)
b=c[::-1]
for i in range(n):
    print(b[i][0],end="")
print(" ",end="")
for i in range(n):
    print(c[i][0],end="")

#10.15下午更新版本：
def make(x):
    if x==0:
        return 9
    else:
        return 9*10**x+make(x-1)
n=int(input())
a=list(input().split())
c=[]
for i in range(n):
    c.append([a[i],int(a[i])/make(len(a[i])-1)])
c.sort(key=lambda x:x[1])
b=c[::-1]
for i in range(n):
    print(b[i][0],end="")
print(" ",end="")
for i in range(n):
    print(c[i][0],end="")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015110112903](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20241015110112903.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

贪心算法还是很难的，特别是如何贪心这一点的思维。我不认为我有很好的计算机思维，所以可能还需要更多的练习来满足课程的需要。目前一直在跟进每日选做，收获还是很大的，很多比较简单的贪心都能有思路并且做出来了。



