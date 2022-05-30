import sys

n = int(sys.stdin.readline())

k = 1
count = 0
while True:
    if n - k >= 0:
        n = n - k
    else:
        k = 1
        n = n - k
    k += 1
    count += 1

    if n == 0:
        break

print(count)
