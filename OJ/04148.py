k=1
while True:
    p,e,i,d=map(int,input().split())
    if p+e+i+d==-4:
        break
    d0=d+1
    while True:
        if abs(d0-p)%23==0 and abs(d0-e)%28==0 and abs(d0-i)%33==0:
            print("Case "+str(k)+": the next triple peak occurs in "+str(d0-d)+" days.")
            break
        else:
            d0+=1
    k+=1