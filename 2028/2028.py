import sys

n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())
    if str(k**2)[len(str(k**2)) - len(str(k)):] == str(k):
        print("YES")
    else:
        print("NO")