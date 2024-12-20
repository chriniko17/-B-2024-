def judge(x):
    if x%13==0:
        return 13
    else:
        return x%13
haab=['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax','zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin=[ 'ahau','imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk','ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac']
n=int(input())
print(n)
for _ in range(n):
    a,b,c=input().split()
    day=int(a[0:len(a)-1])
    year=int(c)
    month=haab.index(b)
    daytot=year*365+month*20+day+1
    #print(day,year,month,daytot)
    print(str(judge(daytot))+" "+str(tzolkin[daytot%20])+" "+str((daytot-1)//260))