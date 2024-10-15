k=int(input())
a=input()
ans=[]
down=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
up=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(a)):
    if a[i] in set(down):
        ans.append(down[(down.index(a[i])-k)%26])
    elif a[i] in set(up):
        ans.append(up[(up.index(a[i]) - k) % 26])
print("".join(ans))