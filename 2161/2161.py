n = int(input())

queue = []
for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 1:
    print(queue[0])
    queue.pop(0)
    queue.append(queue.pop(0))

print(queue[0])