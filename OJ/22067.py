pig=[]
min_stack=[]
cur_min=float("inf")
while True:
    try:
        s=input()
        if s[0]=="p" and s[1]=="o":
            if len(pig):
                removed=pig.pop()
                min_stack.pop()
                if min_stack:
                    cur_min=min_stack[-1]
                else:
                    cur_min=float("inf")
        if s[0]=="m":
            #print(pig)
            if len(pig)>0:
                print(cur_min)
        if s[0]=="p" and s[1]=="u":
            num=int(s[5::])
            pig.append(num)
            if num<cur_min:
                cur_min=num
                min_stack.append(num)
            else:
                min_stack.append(cur_min)
    except EOFError:
        break