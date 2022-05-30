import sys

n = int(sys.stdin.readline())

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]

s = 0
d = n - 1
while d % 2 == 0:
    d = d / 2
    s += 1

d = int(d)
print(s, d)

oi = 0
for i in prime_list:
    for j in range(0, s - 1):
        if (i ** d) % n != 1 and i ** (2 ** j * d) % n != n - 1:
            oi += 1

print(oi)
