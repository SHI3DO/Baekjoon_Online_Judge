import os
from get_baekjoon import get_baekjoon

fp = []
for i in os.listdir():
    if i.isdigit():
        fp.append(i)

for i in fp:
    if not os.path.isfile(f"./{i}/{i}.md"):
        f = open(f"./{i}/{i}.md", 'w', encoding='UTF-8')
        f.write(get_baekjoon(i))
        f.close()
        print(f"{i}.md 생성완료")
