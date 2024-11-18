with open('part1.txt', 'r') as f1:
    content1 = f1.read()
with open('part2.txt', 'r') as f2:
    content2 = f2.read()

full_content = content1 + content2

with open('full_text.txt', 'w') as f3:
    f3.write(full_content)

