import sys

a, b = map(int, sys.stdin.readline().split())

que = []
pr = []
for i in range(1, a + 1):
    que.append(i)

num = 0
while len(que) > 0:
    num += b-1
    if num >= len(que):
        num = num % len(que)
    pr.append(que.pop(num))
    
print(f"<{str(pr)[1:-1]}>")
