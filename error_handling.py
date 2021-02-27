# strang = '3210'
strang = 'I like pizza'

try:
    number = int(strang)
except ValueError:
    pass # pass means "keep going"
else:
    print(5 + number)
finally:
    print('huh.')

