while True:
    try:
        a, b = input().split()
        ans = [[0] * len(a) for i in range(len(b))]
        for i in range(len(a)):
            if a[i] == b[0]:
                for j in range(i, len(a)):
                    ans[0][j] = 1
                break
        for i in range(len(b)):
            if b[i] == a[0]:
                for j in range(i, len(b)):
                    ans[j][0] = 1
                break
        for i in range(1, len(b)):
            for j in range(1, len(a)):
                if b[i] == a[j]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])
        print(ans[len(b) - 1][len(a) - 1])
    except EOFError:
        exit()