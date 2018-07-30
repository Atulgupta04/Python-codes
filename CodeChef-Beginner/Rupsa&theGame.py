T = int(input())
div = 10**9 + 7
for _ in range(T):
    N = int(input())
    arr = [int(i) for i in input().split()]
    c = 2 * arr[0]
    b = 1
    total = 0
    for i in range(1, N+1):
        b = (b * 2) % div
        total = (2 * total + arr[i] * c) % div
        print("total:",total,"\n")
        c = (c + b * arr[i]) % div
        print("c:",c,"\n")
    print(total)
