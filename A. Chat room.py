a=input()
if a.count("h")<1 or a.count("e")<1 or a.count("l")<2 or a.count("o")<1:
    print("NO")
    exit()
a=a[a.index("h")+1::]
if a.count("e") < 1 or a.count("l") < 2 or a.count("o") < 1:
    print("NO")
    exit()
a=a[a.index("e")+1::]
if a.count("l") < 2 or a.count("o") < 1:
    print("NO")
    exit()
a=a[a.index("l")+1::]
if a.count("l") < 1 or a.count("o") < 1:
    print("NO")
    exit()
a=a[a.index("l")+1::]
if a.count("o") < 1:
    print("NO")
else:
    print("YES")