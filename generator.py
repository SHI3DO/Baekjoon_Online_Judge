import os
import sys
from get_baekjoon import get_baekjoon

print("문제 번호?")
n = sys.stdin.readline().rstrip()

if not os.path.isdir(f"./{n}"):
    print("정말 만드시겠습니까? Y/N")
    a = sys.stdin.readline().rstrip()
    if a.lower() == 'y':
        os.mkdir(n)
        f = open(f"./{n}/{n}.py", 'w', encoding='UTF-8')
        f.close()
        print(f"{n}.py 생성완료")
        f = open(f"./{n}/{n}.md", 'w', encoding='UTF-8')
        f.write(get_baekjoon(n))
        f.close()
        print(f"{n}.md 생성완료")
    else:
        print("최소합니다.")
        sys.exit()
else:
    print("파일이 이미 있습니다.")
