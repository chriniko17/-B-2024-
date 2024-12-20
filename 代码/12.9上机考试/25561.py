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