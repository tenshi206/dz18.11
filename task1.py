with open ('text.txt', 'r') as f:
    lines = 0
    words = 0
    symbols = 0
    for line in f:
        lines += 1
        words += len(line.split())
        symbols += len(line)
print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)