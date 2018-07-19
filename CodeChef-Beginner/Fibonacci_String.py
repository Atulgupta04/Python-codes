#https://www.codechef.com/problems/CLFIBD
t = int(input())
for _ in range(t):
    S = input()
    d = dict()
    for c in S:
        d[c] = d.get(c, 0) + 1
    counts = sorted(d.values())

    if len(counts) < 3:
        print("Dynamic")
    elif len(counts) == 3:
        if counts[2] == counts[0] + counts[1]:
            print("Dynamic")
        else:
            print("Not")
    else:
        if counts[3] != counts[1] + counts[2]:
            temp = counts[0]
            counts[0] = counts[1]
            counts[1] = temp
        flag = True
        for j in range(3, len(counts)):
            if counts[j] != counts[j - 1] + counts[j - 2]:
                flag = False
                break
        if flag:
            print("Dynamic")
        else:
            print("Not")
