total = 0

def sum_numbers(total):
    with open('homework.txt') as homework:
        my_name = [name for name in homework if 'Roy' in name]
        for line in my_name:
            names_numbers = line.split()
            total += int(names_numbers[1].strip())
    print(total)

sum_numbers(total)

