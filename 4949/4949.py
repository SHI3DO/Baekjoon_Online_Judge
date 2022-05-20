# Silver IV
while True:
    stack = []
    c = input()
    if c == ".":
        break

    for i in c:
        if i == '(':
            stack.append(1)
        if i == '[':
            stack.append(2)
        if i == ')':
            if len(stack) != 0 and stack[-1] == 1:
                stack.pop()
            else:
                stack.append(3)
                break
        if i == ']':
            if len(stack) != 0 and stack[-1] == 2:
                stack.pop()
            else:
                stack.append(3)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
