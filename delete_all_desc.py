import os


fp = []
for i in os.listdir():
    if i.isdigit():
        fp.append(i)

for i in fp:
    if os.path.isfile(f"./{i}/{i}.md"):
        os.remove(f"./{i}/{i}.md")
        print(f"{i}.md 삭제완료")
