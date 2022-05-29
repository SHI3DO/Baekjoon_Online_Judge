import sys

n = sys.stdin.readline().rstrip()
b = []


def buy():
    for i in range(0, 10):
        b.append(i)


buy()
k = 1
for h in n:
    if b.count(int(h)) > 0:
        b.remove(int(h))
    else:
        if int(h) == 6:
            if b.count(9) > 0:
                b.remove(9)
            else:
                buy()
                k += 1
                b.remove(int(h))

        elif int(h) == 9:
            if b.count(6) > 0:
                b.remove(6)
            else:
                buy()
                k += 1
                b.remove(int(h))
        else:
            buy()
            k += 1
            b.remove(int(h))

print(k)
