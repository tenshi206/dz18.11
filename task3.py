with open('input.txt', 'r') as infile:
    text = infile.read()
uppercase_text = text.upper()
with open('output.txt', 'w') as outfile:
    outfile.write(uppercase_text)