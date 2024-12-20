from traceback import print_tb

a=input()
letter=["I","V","X","L","C","D","M"]
respond=[1,5,10,50,100,500,1000]
if a[0] in set(letter):
    a=list(a)
    ans=0
    i=0
    while len(a)>1:
        r=1
        if a[0]=="M":
            ans+=1000
        elif a[0]=="D":
            ans+=500
        elif a[0]=="L":
            ans+=50
        elif a[0]=="V":
            ans+=5
        elif a[0]=="C":
            if a[1]=="M":
                ans+=900
                r=2
            elif a[1]=="D":
                ans+=400
                r=2
            else:
                ans+=100
        elif a[0]=="X":
            if a[1]=="C":
                ans+=90
                r=2
            elif a[1]=="L":
                ans+=40
                r=2
            else:
                ans+=10
        elif a[0]=="I":
            if a[1]=="X":
                ans+=9
                r=2
            elif a[1]=="V":
                ans+=4
                r=2
            else:
                ans+=1
        if r==1:
            a.pop(0)
        else:
            a.pop(0)
            a.pop(0)
    if len(a)>0:
        ans+=respond[letter.index(a[0])]
    print(ans)
else:
    a=int(a)
    thousand=a//1000
    hundred=(a-thousand*1000)//100
    ten=(a-thousand*1000-hundred*100)//10
    one=a-thousand*1000-hundred*100-ten*10
    if thousand>0:
        for i in range(thousand):
            print("M",end="")
    if hundred>0:
        if hundred==9:
            print("CM",end="")
        elif hundred==4:
            print("CD",end="")
        else:
            if hundred>=5:
                print("D",end="")
                hundred-=5
            for i in range(hundred):
                print("C",end="")
    if ten>0:
        if ten==9:
            print("XC",end="")
        elif ten==4:
            print("XL",end="")
        else:
            if ten>=5:
                print("L",end="")
                ten-=5
            for i in range(ten):
                print("X",end="")
    if one>0:
        if one==9:
            print("IX",end="")
        elif one==4:
            print("IV",end="")
        else:
            if one>=5:
                print("V",end="")
                one-=5
            for i in range(one):
                print("I",end="")

