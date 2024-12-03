# Assignment #2: 语法练习



2024 fall, Complied by 俞天麒 物理学院



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：就一个个搜索过去。。。因为毕竟最大5*5，所以也不会超时



##### 代码

```python
for i in range(5):
    line=list(map(int,input().split()))
    for j in range(5):
        if line[j]==1:
            a,b=i,j
        else:continue
print(abs(a-2)+abs(b-2))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240925192147185](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925192147185.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：这题只要不要真的去让a一个个+1就好了，可以直接用b-a%b解决，要不然会超时



##### 代码

```python
n=int(input())
ans=[]
for i in range(n):
    a,b=map(int,input().split())
    if a%b==0:
        ans.append(0)
    else:
        ans.append(b-a%b)
for i in range(n):
    print(ans[i])


```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240925192215995](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925192215995.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：一个个遍历过去，题目怎么说怎么来，还挺直接的。因为只用一个for循环，所以时间复杂度还好



##### 代码

```python
n=int(input())
a=list(map(int,input().split()))
p=0
ans=0
for i in range(n):
    if a[i]==-1 and p<=0:
        ans=ans+1
    elif a[i]==-1 and p>0:
        p=p-1
    else:
        p=p+a[i]
print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240925192426821](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925192426821.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：用0和1标记树还在不在，反正赋值多次0还是0，所以就每来一个数据，就把对应点赋值成0，最后取数1的个数就好了



##### 代码

```python
l,m=map(int,input().split())
tree=[1]*(l+1)
for i in range(m):
    be,en=map(int,input().split())
    for j in range(be,en+1):
        tree[j]=0
print(tree.count(1))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240925192713553](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925192713553.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：把数字转化为字符串，这样就可以很方便的读取每一个位数了。虽然这道题反正100-999内水仙花数就那几个，枚举也不是问题（（



##### 代码

```python
def judge(x):
    a=str(x)
    for i in range(len(a)):
        x-=int(a[i])**3
    if x==0:
        return 0
    else:
        return 1
a,b=map(int,input().split())
ans=[]
for i in range(a,b+1):
    if judge(i)==0:
        ans.append(i)
if len(ans)==0:
    print("NO")
else:
    print(" ".join(map(str,ans)))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240925192854775](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925192854775.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：挺难想的。。。但只要注意到他一定和一个人一起到就行了，所以他的到达时间就是他能赶得上的最快的那位同学的



##### 代码

```python
import math
while True:
    n=int(input())
    if n==0:
        break
    ans=float("inf")
    for i in range(n):
        v,t=map(int,input().split())
        if t>=0:
            ans=min(ans,t+math.ceil(4.5/v*3600))
    print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240925194209240](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240925194209240.png)



## 2. 学习总结和收获

目前还在跟进每日练习题（加油！）

难度有所上升，有时候挺吃力才能拿下的，不过看着accepted挺有成就感的，所以就除了每日选做之外很少做其他了

现在面临的问题基本不是语法或者特殊函数了，是在于一些简化的思路和算法了，这个问题只能靠多做一点题目来积累，希望之后的每日选做能带给我新的灵感





