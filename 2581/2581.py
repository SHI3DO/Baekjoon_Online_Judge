a = int(input())
b = int(input())


def is_prime_num(o):
    if o == 1:
        return False
    for k in range(2, int(o ** 0.5) + 1):
        if o % k == 0:
            return False

    return True


c = []
for i in range(a, b + 1):
    if is_prime_num(i):
        c.append(i)

if len(c) > 0:
    print(f"{sum(c)}\n{min(c)}")
else:
    print("-1")
