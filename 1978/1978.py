a = input()
c = input().split()

def is_prime_num(o):
    if o == 1:
        return False
    for k in range(2, int(o ** 0.5) + 1):
        if o % k == 0:
            return False

    return True

couter = 0
for i in c:
    if is_prime_num(int(i)):
        couter+=1

print(couter)