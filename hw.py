a = int(input('Введите число '))
b = int(input('Введите число ' ))
c = int(input('Введите число ' ))
if a + b == c:
    print('a и b в сумме дают c')
if a * b == c:
    print('a умножить на b равно c')
if b!=0 and a%b==c:
    print('a даёт остаток c при делении на b')
if b==0:
    print('на 0 делить нельзя')
if b!=0 and a / b == c:
    print('a разделить на b равно c')
else:
    print('введённые числа не обладают свойствами')
