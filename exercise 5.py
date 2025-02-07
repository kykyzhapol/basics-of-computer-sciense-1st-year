great = ['Привет', 'Hello', 'Bonjour', 'Hej', 'Hola']
for i in great:
    if great.index(i) == 2:
        print(f'{i} Python!', end=' ')
    else:
        print(f'{i}, Python!', end=' ')