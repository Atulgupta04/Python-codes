#https://www.codechef.com/problems/SINS
def NumberChoclatesLeft(a, b):
    if a == b:
        return 2*a
    elif a>b:
        return NumberChoclatesLeft(b,a)
    else:
        if b%a == 0:
            return 2*a
        else:
            return NumberChoclatesLeft(b-int(b/a)*a, a)
t = int(raw_input())
for i in range(0, t):
    x,y = [int(N) for N in raw_input().split(" ")]
    n = NumberChoclatesLeft(x, y)
    print(n
