while True:
  a = input('Введите слово: ')
  if a == '':
    break
  else:
    a = a.lower() 
    a = a.strip("-.,:;!")
    part = a[0:len(a)//2] 
    print(part)
