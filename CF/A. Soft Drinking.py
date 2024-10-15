n,k,l,c,d,p,nl,np=map(int,input().split())
tot=min(k*l//nl,c*d,p//np)
print(int(tot//n))