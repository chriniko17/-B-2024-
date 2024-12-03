# Assignment #1: 自主学习

2024 fall, Complied by 俞天麒 物理学院

## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：按照闰年定义即可



##### 代码

```python
n=int(input())
if (n%4==0 and n%100!=0) or n%400==0:
    print("Y")
else:
    print("N")

```



代码运行截图

![image-20240910164628611](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910164628611.png)

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：向上取整；注意奇数只脚的情况不存在



##### 代码

```python
import math
a=int(input())
if a%2==1:
    print("0 0")
else:
    print(math.ceil(a/4),math.ceil(a/2))

```



代码运行截图 

![image-20240910165643495](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910165643495.png)

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：自己脑海里对每条边是奇数还是偶数每种情况想过去，发现只要有1条边是偶数就能铺满，全是奇数会空一个格子



##### 代码

```python
a,b=map(int,input().split())
print((a*b)//2)

```



代码运行截图

![image-20240910170106620](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910170106620.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：每条边铺满就是最小需求量



##### 代码

```python
import math
m,n,a=map(int,input().split())
print(math.ceil(m/a)*math.ceil((n/a)))

```



代码运行截图 

![image-20240910170415585](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910170415585.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：python对字符串的大小比较就是按照字典顺序比较



##### 代码

```python
a=input()
b=input()
a=a.lower()
b=b.lower()
if a>b:
    print("1")
elif a<b:
    print("-1")
else:
    print("0")

```



代码运行截图 

![image-20240910170610094](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910170610094.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：暴力对每种情况枚举即可



##### 代码

```python
n=int(input())
ans=0
for i in range(n):
    a,b,c=map(int,input().split())
    if (a==1 and b==1) or (a==1 and c==1) or (b==1 and c==1) or (a==1 and b==1 and c==1):
        ans=ans+1
    else:continue
print(ans)

```



代码运行截图 

![image-20240910170804448](C:\Users\21612\AppData\Roaming\Typora\typora-user-images\image-20240910170804448.png)



## 2. 学习总结和收获

这次作业还是很简单的，只考察了最基本的语法，还有很多每日选做题的原题。

有按时完成，或者超前完成每日选做题，把每日选做题全部完成后做这个压力不是很大。

每日选做题前期压力挺大的，因为不了解语法，什么都得从0开始。慢慢地通过gpt的帮助，懂得了基础的语法和有用的函数，之后就能跟得上每日选做题的节奏了，甚至有时间还能超前完成前面的。



