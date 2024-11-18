with open('story.txt', 'r') as f:
    content = f.read()
a = content.replace('Python', 'Java')
with open('new_story.txt', 'w') as o:
    o.write(a)
