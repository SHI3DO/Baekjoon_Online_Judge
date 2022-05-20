# Silver III
import sys

n = int(sys.stdin.readline())

stack = []
sign = []
joo = 1
w = 0
for i in range(n):
    num = int(sys.stdin.readline())
    while joo <= num:
        stack.append(joo)
        sign.append("+")
        joo += 1

    if stack[-1] == num:
        stack.pop()
        sign.append("-")
    else:
        w = 1

if w == 0:
    for j in sign:
        print(j)
else:
    print("NO")
