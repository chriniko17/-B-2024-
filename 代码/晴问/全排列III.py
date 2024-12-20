from itertools import permutations

n=int(input())
a=sorted(list(map(int,input().split())))
term=sorted(list(set(permutations(a))))
for i in range(len(term)):
    print(" ".join(map(str,term[i])))