while True:
    try:
        n=int(input())
        a=sorted(list(map(int,input().split())))
        if sum(a)/2>=a[n-1]:
            print("{:.1f}".format(sum(a)/2))
        else:
            print("{:.1f}".format(sum(a)-a[n-1]))
    except EOFError:
        break