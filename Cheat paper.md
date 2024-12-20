# Cheat paper

### dijkstra模板

```python
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
```

利用heapq简化存入取出的过程！

### Dilworth's theorem

最常见的应用：最小完整覆盖全数组的上升子序列数等于最长非上升子序列的长度，这类的！

### 二分查找模板

bisect_left:

```python
while lo < hi:
	mid = (lo + hi) // 2
    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid
```

bisect_right:

```python
while lo < hi:
    mid = (lo + hi) // 2
    if x < a[mid]:
        hi = mid
    else:
        lo = mid + 1
```

### python中用format保留小数位数的用法

```python
# 保留两位小数
number = 3.14159
formatted_number = "{:.2f}".format(number)
print(formatted_number)  # 输出: 3.14
```
