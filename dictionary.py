# Answer for all classmates' totals for homework1.txt

answer_key = {}
with open('homework.txt') as homework_file:
    for line in homework_file:
        name, number_string = line.split()
        if name in answer_key:
            answer_key[name] += int(number_string)
        else:
            answer_key[name] = int(number_string)

for key, value in answer_key.items():
    print(f'{key} - {value}')
