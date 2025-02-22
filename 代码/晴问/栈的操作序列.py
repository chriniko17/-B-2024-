from collections import deque
a=deque([])
n=int(input())
for i in range(n):
    s=input()
    if s[1]=="o":
        if a:
            print(deque.pop(a))
        else:
            print("-1")
    else:
        num=int(s[5::])
        deque.append(a,num)
