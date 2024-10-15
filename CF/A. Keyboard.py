a=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",";","z","x","c","v","b","n","m",",",".","/"]
com=input()
list=list(input())
k=1
if com=="R":
    k=-1
for i in range(len(list)):
    list[i]=a[a.index(list[i])+k]
print("".join(list))