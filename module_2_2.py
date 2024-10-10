first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
a = first
b = second
c = third
if a == b == c:
    print(3)
elif a != b != c:
    print(0)
elif a == b or c:
    print(2)