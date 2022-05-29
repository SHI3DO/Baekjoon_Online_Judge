N = int(input())

for i in range(N, 0, -1):
    b = ' ' * (N - i) + '*' * ((2 * i) - 1)

    print(b)
