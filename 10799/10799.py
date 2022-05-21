# Silver III
import sys

stt = list(sys.stdin.readline().rstrip())

stack = []
res = 0
for i in range(len(stt)):
    if stt[i] == '(':
        stack.append('(')

    else:
        stack.pop()
        if stt[i-1] == '(':
            res += len(stack)
        else:
            res += 1

print(res)
