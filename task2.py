with open('data.txt', 'r') as file:
    content = file.read().strip()  
    numbers = content.split()  
    even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
print("Четные числа:", even_numbers)