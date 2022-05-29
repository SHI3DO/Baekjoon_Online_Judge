import sys

for i in range(3):
    n = int(sys.stdin.readline())
    A = []
    for j in range(n):
        A.append(int(sys.stdin.readline()))

    s = sum(A)

    if s > 0:
        print("+")

    elif s == 0:
        print("0")
    else:
        print("-")