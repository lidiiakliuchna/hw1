b = []
k=0
while True:
    a = input('Введите слово: ')
    if not a:
        break
    else:
        b.append(a)

for i in b:
    k += 1
    print(i[k:len(i)]) #если слово короче удаления, то считаем, что выводим пустую строк
  

