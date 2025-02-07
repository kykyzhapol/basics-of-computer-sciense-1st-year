playlist = []
print('Введите плей-лист папы:')
for i in range(0,5):
    playlist.append(input())
    print(end='\n')
print('Плей-лист мамы:', end='\n\n')
for i in sorted(range(0,5), reverse = True): #or we can use reversed()
    print(playlist[i], end='\n\n')