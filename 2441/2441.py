import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = ""
    for j in range(i):
        a+=" "
    for j in range(n - i):
        a += "*"
    print(a)
