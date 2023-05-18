# city =input().split()
# if 'Москва' in city:
#    city.remove('Москва')
# print(*city)

# number = list(map(int, input()))
# if sum(number[0:3]) == sum(number[3:]):
#   print('ДА')
# else:
#    print('НЕТ')

# m = int(input())
# if m == 1:
#    print('1. Введение в Python')
# elif m == 2:
#    print('2. Строки и списки')
# elif m == 3:
#    print('3. Условные операторы')
# elif m == 4:
#    print('4. Циклы')
# elif m == 5:
##    print('5. Словариб кортежи и множества')
# elif m == 6:
#    print('6. Выход')

# a, b, c = list(map(int, input().split()))
# if a <= b:
#    if a <= c:
#        print(a)
#    else:
#        print(c)
# else:
#    if b <= c:
#        print(b)
#    else:
#        print(c)

# w = float(input())
# if w <= 60:
#    print('1')
# elif 60.1 <= w <= 64:
#    print('2')
# elif 64.1 <= w <= 69:
#    print('3')
# elif w >= 69.1:
#    print(4)

# num = int(input())
# if num == 1:
#    print('понедельник')
# elif num == 2:
#    print('вторник')
# elif num == 3:
#    print('среда')
# elif num == 4:
#    print('четверг')
# elif num == 5:
#    print('пятница')
# elif num == 6:
#    print('суббота')
# elif num == 7:
#    print('воскресенье')

# month = int(input())
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#   print(31)
# else:
# if month == 4 or month == 6 or month == 9 or month == 11:
#    print(30)
# else:
#      if month == 2:
#           print(28)

# a = float(input())
# b = float(input())
# d = a if a > b else b
# print(d)

# num = int(input())
# msg = 'кратно 3' if num % 3 == 0 else 'не кратно 3'
# print(msg)

# палиндром
# word = input().lower()
# msg = 'палиндром' if word == word[::-1] else 'не палиндром'
# print(msg)

# num = int(input())
# s = 'False' if num == 0 else 'True'
# print(s)

# n, m = map(int, input().split())
# while n <= m:
#    print(n**2, end=' ')
#   n += 1

# book = float(input())
# x = book
##while x < book * 10:
#    x += book
#    print(round(x, 1), end=' ')

# s = float(input())
# i = 2
# while i <= 10 :
#    print(round(s*i,1), end = ' ')
#   i += 1

# print('Hello, Artem')
# print(19 + 3.0)

# На год старше
# Напишите программу, которая принимает на вход возраст человека (количество полных лет) и выводит сколько лет ему
# исполнится в следующем году
# age = int(input())
# c = age + 1
# print(c)


# num = int(input())
# print(num * 2)
##print(num / 2)

# s = float(input())
# print(s ** 2)
# a = abs(int(input()))
# b = abs(int(input()))
# print(a + b)

# a = float(input())
# b = float(input())
# s = a * b
# p = 2 *(a + b)
# print(s, p)

# f = float(input())
# c = ((f - 32) * 5) / 9
# print(c)

# x1 = float(input())
# x2 = float(input())
# print(abs(x2 - x1))

# num = float(input())
# print(round(num, 2), round(num, 3))
# a = int(input())
# b = int(input())
# c = int(input())
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# t = a * 3600 + b * 60 + c
# t1 = a1 * 3600 + b1 * 60 + c1
# print(t1 - t)

# a = int(input())
# b = int(input())
# c = int(input())
# p = a + b + c
# p1 = a * b * c
# p2 = a * b + c
# p3 = a + b * c
# p4 = (a + b) * c
# p5 = a * (b + c)
# print(max(p, p1, p2, p3, p4, p5))

# a, b, c, d = map(int, input().split())
# s = ((a + b + c + d) / 4)
# print(s)

# a, b, c, d, s = map(int, input().split())
# print(max(a, b, c, d, s))

# n, a, b = map(int, input().split())
# s = ((a * b) * n) * 2
# print(s)

# s = int(input())
# x = s // 6
# print(x, x* 4, x)

# x , y , z = map(int, input().split())
# print(x * 3 + x * 5 + z * 12)

# a, b = map(int, input().split())
# s = a + b - 1
# print(s - a, s -ample Output:

# a, b, c = map(int, input().split())
# print(a, b, c, sep=',')

# s = input()
# s1 = input()
# s2 = input()
# print(s, s1, s2, sep='---')
# print(1, 2, 3, 4, 5, sep=st)

# print(input(), end=' - Сказала она!')
# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# gram = int(input())
# a = gram // 1000
# b = gram // 100 % 10
# c = gram // 10 % 10
# d = gram % 10
# print(a)

# n = int(input())
# r = int(input())
# k = n // r
# print(k)

# print(int(input()) % 10)
# print(int(input()) // 100 % 10)
# num = int(input())
# a = num // 100 % 10
# b = num // 10 % 10
# c = num % 10
# print(a + b + c)

# a = int(input())
# a += 1
# print(a)

# x = float(input())
# x *= 1.5
##print(x)

# x = input()
# z = input()
# print(x == "awesome" or z == "awesome")

# a, b, c = map(int, input().split())
# print(a == b or a == c or b == c)

# a = int(input())
# print(9 < a <100)

# a, b, c = map(int, input().split())
# print(a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a)

# import math
# k = n / 4
# print(math.ceil(k))
# import math
##a = int(input())
# b = int(input())
# c = int(input())
# print(math.ceil(a + b + c) / 2 )

# print("""Я стану крутым программистом!
# Я стану крутым программистом!
# Я стану крутым программистом!""")
# print('Лев Николаевич Толстой написал "Война и мир"')

# a = input()
# b = input()
# print(b + a)

# a, b, c = input().split()
# a1 = str(ord(a))
# b1 = str(ord(b))
# c1 = str(ord(c))
# print('Simvol code', a, 'is', a1 + '.', end='\n')
# print('Simvol code', b,'is', b1 + '.', end='\n')
# print('Simvol code', c, 'is', c1 + '.', end='\n')

# s = input()
# s1 = s[0:3].upper() + s[3:-3].lower() + s[-3::].upper()
# print(s1)

# s = input()
##s1 = s.lower().replace('a','').replace('o', '').replace('y','').replace('e', '').replace('u', '').replace('i', '')
# '.'.join(s1)
# print(s1)

# s = input()
# print(s.title().swapcase())
# s = input()
# s = len(s.split())
# print(s)

# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# print('-'.join(list_strings))

# postfix = input()
# print(s.endswith(postfix))

# s = input()
# prefix = input()
# postfix = input()
# print(s.startswith(prefix) and s.endswith(postfix))

# s = input().zfill(10)
# print(s)

# s = input().strip('-_!?')
# print(s)

# s = input().rstrip('-_!?')
# print(s)

# word = input()
# print("Что Вы сказали? {0}? Какое интересное слово".format(word))

# name = input()
# sur_name = input()
# print('Здравствуйте, {0} {1}!'.format(sur_name,name))

# num = int(input())
# num1 = num - 1
# num2 = num + 1
# s = '''Для числа {0} предыдущим будет число {n}.\nДля числа {0} следующим будет число {1}.'''.format(num, num2, n = num1)
# print(s)

# num = input()
# print(f'Мое имя {num}!')

# num = input().upper()
# age = input()
# print(f'Hello {num}. You are {age} years old.')

# num = input()
# year = int(input()) + 77
# print(f'{num}, вам исполнится 77 лет в {year}') или {year + 77}

# num = int(input())
# print(f'{num} сек - это {num // 60} мин. {num % 60} сек.')

# width, height = map(int,input().split())
# print(f'''Разрешение экрана: {width} x {height}.\nОбщее количество пикселей = {width * height}.''')

# num = int(input())
# num1= int(input())
# print(f'{num} / {num1} = {num / num1}\n{num} // {num1} = {num // num1}\n{num} % {num1} = {num % num1}')

# x = int(input())
# y = int(input())
# z = int(input())
# #print(f'Vector A{x, y, z}\nVector B{x + 5, y + 5, z + 5}')

# course = float(input())
# buy =int(input())
# print(f'Current dollar rate is {course}. You want to buy {buy} dollars\nYou must pay {course * buy}')

# x = int(input())
# y = int(input())
# print(f'Точка({x = }, {y = })')

# py = float(input())
# print(f'{py:.2f}')

# num = int(input())
# print(f'{num:010d}')
# num = int(input())
# print(f'{num:-^15}')

# s = input()
# print(f'|{s:&^20}|')
# print(f'|{s:&>20}|')
# print((f'|{s:&<20}|'))

# my_list = [1] * 77
# print(my_list)
# my_list = ['q', 'w', 't'] * 15
# print(my_list)

# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# print(min(my_list), max(my_list))

# my_list = list(map(int, input().split()))
# print(777 in my_list)

# num = list(map(int, input().split()))
# print(sum(num))
# list_numbers = list(map(int, input().split()))
# print(sum(list_numbers) / len(list_numbers))
# a = list(map(int, input().split()))
# print(a[1])

# a = list(map(int, input().split()))
# print(a[2:5])

# a = list(map(int, input().split()))
# print(a[-3:])

# a = list(map(int, input().split()))
# print(a[1::3])

# a = list(map(int, input().split()))
# print(a[::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[6] = "Сверхъестественное"
# top[2] = 'Настоящий детектив'
##print(top)
# 111, 222, 789 и 201
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# num = int(input())
# print(months[num - 1])

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.insert(5, 111)
# numbers.insert(8, 222)
# numbers.insert(0, 789)
# numbers.insert(11, 201)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
#
# extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
# numbers.extend(extra)
# print(numbers)удалить элемент, стоящий на последней позиции;
# удалить элемент, стоящий на 0-й позиции;
# удалить элемент, стоящий на 12-й позиции;
# удалить элемент, стоящий на 7-й позиции;

# numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# numbers.remove(3)
# numbers.remove(5)
# numbers.remove(7)
# numbers.remove(9)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True)
# print(numbers)
# a = list(map(int, input().split()))
# a.reverse()
# print(a)
# a = list(map(int, input().split()))
# print(a.count(999))
# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# copy_numbers = numbers.copy(
# w = input().upper().split()
# s = list(w[0])
# s1 = list(w[1])
# print('-'.join(s), '-'.join(s1))

# name = input().split()
# n = name[0][0]
# name1 = name[1][0]
# name2 = name[2]
# print(f'{name2} {n}.{name1}.')

# s = input().split()
# print('\n'.join(s))
# s = input()
# if s == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# gain = int(input())
# if gain < 20000:
#     print(gain)
# else:
#     print(gain - gain / 100 * 13)

# num = int(input())
# num1 = int(input())
# if num > num1:
#     print(num)
# else:
#     print(num1)

# a, b, c = map(int, input().split())
# if a + b == c:
#     print('YES')
# else:
#     print('NO')
# a = list(map(int, input().split()))
# if 3 in a:
#     a.remove(3)
# if 5 in a:
#     a.remove(5)
# if 7 in a:
#     a.remove(7)
# if 9 in a:
#     a.remove(9)
# print(a)

# if (su := int(input())) <= 10000:
#     print(f'Сумма {su} не превышает лимит, проходите')
# if su > 10000:
#     print(f'Ого! {su}! Куда вам столько? Мы заберем {su - 10000}')

# if 'walrus' in (wo := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# s = input()
# t = input()
# if s == t[::-1]:
#     print('YES')
# else:
#     print('NO')
# n = int(input())
# n = str(n)
# if n == n[::-1]:
#     print('YES')
# else:
# print('NO')
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and c + b >a:
#     print(Y'SE')
# else:
#     print('NO')
# n = int(input())
# s = n // 100000
# s1 = n // 10000 % 10
# s2 = n // 1000 % 10
# s3 = n // 100 % 10
# s4 = n // 10 % 10
# s5 = n % 10
# if s +s1 +s2 == s3 + s4 + s5:
#     print('YES')
# else:
#     print('NO')
# text = int(input())
# text = 'Even' if text % 2 == 0 else 'Odd'
# print(text)

# minimum = int(input())
# maximum = int(input())
# print(minimum, maximum) if minimum < maximum else print(maximum, minimum)
#
# s = input()
# sentence = 'Вопросительное' if '?' in s[-1] else 'Обычное'
# print(sentence)

# sou = input()
# nort = input()
# experiment = 'Притягиваются' if sou != nort else 'Отталкиваются'
# print(experiment)

# A = int(input())
# B = int(input())
# if A < B:
#     print('<')
# else:
#     if A > B:
#         print('>')
#     else:
#         print('=')

# a = int(input())
# b = int(input())
# c = int(input())
# if c < a > b:
#     print(a)
# else:
#     if a < c > b:
#         print(c)
#     else:
#         print(b)

# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# elif n == 1:
#     print(0)
# else:
#     print(n)

# a, b, c = map(int, input().split())
# if c < a > b and a > c < b:
#      print(a - c)
# else:
#      if a < c > b and c > a < b:
#          print(c - a)
#      else:
#          if c < a > b and a > b < c:
#              print(a - b)
#          else:
#              if a < b > c and b > a <c:
#                  print(b - a)
#              else:
#                  if a < c > b and a > b < c:
#                      print(c - b)
#                  else:
#                      if a < b > c and a > c < b:
#                          print(b - c)

# s = input().lower()
# s1 = input().lower()
# if s < s1:
#     print('-1')
# else:
#     if s > s1:
#         print('1')
#     else:
#         if s == s1:
#             print('0')
#
# a, b = input().lower(), input().lower()
# print(int(a > b) - int(b > a))

# s, v1, v2, t1, t2 = map(int, input().split())
# time1 = s * v1 + 2 * t1
# time2 = s * v2 + 2 * t2
# if time1 < time2:
#     print('First')
# else:
#     if time1 > time2:
#         print('Second')
#     else:
#         print('Friendship')

# g = input().lower().strip('ьыъ')
# g1 = input().lower()
# if g[-1] == g1[0]:
#     print('Good')
# else:
#     print('Bad')

# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)

# a = input()
# b = input()
# c = input()
# if a == b == c:
#     print('3')
# elif a == b or b == c or a == c:
#     print('2')
# else:
#     print('0')

# n = int(input())
# if n == 1:
#     print('Январь')
# elif n == 2:
#     print('Февраль')
# elif n == 3:
#     print('Март')
# elif n == 4:
#     print('Апрель')
# elif n == 5:
#     print('Май')
# elif n == 6:
#     print('Июнь')
# elif n == 7:
#     print('Июль')
# elif n == 8:
#     print('Август')
# elif n == 9:
#     print('Сентябрь')
# elif n == 10:
#     print('Октябрь')
# elif n == 11:
#     print('Ноябрь')
# elif n == 12:
#     print('Декабрь')

# age = int(input())
# if age < 2:
#     print('Младенец')
# elif 2 <= age < 4:
#     print('Малыш')
# elif 4 <= age < 12:
#     print('Ребенок')
# elif 12 <= age < 19:
#     print('Подросток')
# elif 19 <= age < 65:
#     print('Взрослый человек')
# elif 65 <= age:
#     print('Пожилой человек')

# n = float(input())
# n1 = float(input())
# s = input()
# if s == '+':
#     print(n + n1)
# elif s == '-':
#     print(n - n1)
# elif s ==  '*':
#     print(n * n1)
# elif s == '/':
#     if n != 0 and n1 != 0:
#         print(n / n1)
#     else:
#         print('Неизвестно')
# else:
#     print('Неизвестно')

# pas = input()
# pas1 = input()
# if len(pas) < 7:
#     print('Short')
# elif pas != pas1:
#     print('Difference')
# elif pas == pas1 and len(pas) >= 7:
#     print('OK')

# num = int(input())
# match num:
#     case 1:
#         print('Совсем еще зеленый студентик')
#     case 2:
#         print('Джун-студент')
#     case 3:
#         print('Мидл-студент')
#     case 4:
#         print('Сеньер-студент')
#     case 5:
#         print('Босс качалки')
#     case _:
#         print('Неизвестный курс')

# n = int(input())
# match n:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print('31')
#     case 4 | 6 | 9 | 11:
#         print('30')
#     case 2:
#         print('28')

# s = input()
# match s:
#     case 'Овен' | 'Лев' | 'Стрелец':
#         print('Огненный')
#     case 'Телец' | 'Дева' | 'Козерог':
#         print('Земной')
#     case 'Близнецы' | 'Весы' | 'Водолей':
#         print('Воздушный')
#     case 'Рак' | 'Скорпион' | 'Рыбы':
#         print('Водный')

# n = 1000
# while 1000 <= n <= 2000:
#     print(n)
#     n += 1

# n = 6785
# while 195 <= n :
#         print(n)
#         n -= 5

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)

# st = input()
# while len(st) != 0:
#     st = st[:]
#     print(st)
#     st = st[1:-1]
#
# n = int(input())
# a = 1
# while a**2 <= n:
#     print(a**2)
#     a += 1

# x, y = map(int, input().split())
#  d = 1
#  while x <= y:
#      x *= 1.15
#      d += 1
#  print(d)
#
#  a, b = map(int, input().split())
#  i = 1
#  while a <= b:
#      j = a / 100 * 15
#      a = a + j
#      i += 1
#  print(i)
#
# nosci, m_dni = map(int, input().split())
# day = 0
# while nosci > 0:
#     nosci -= 1
#     day += 1
#     if day % m_dni == 0:
#         nosci += 1
# print(day)

# number = 999000112233
# count = 0
# while number > 0:
#     number = number // 10
#     count += 1
#     print(number)
# print(count)

# number = 1234567890
# count = 0
# while number > 0:
#     last_digit = number % 10
#     if last_digit < 3:
#         count = count + 1
#     number = number // 10
# print(count)
#
#
# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)
#
# num = int(input())
# while num > 0:
#     print(num % 10)
#     num = num // 10

# num = int(input())
# s = 0
# while num > 0:
#     s = s + num % 10
#     num = num // 10
# print(s)

# num = int(input())
# pr = 1
# while num > 0:
#     pr = pr * (num % 10)
#     num = num // 10
# print(pr)

# num = int(input())
# maxsim = 0
# minim = 9
# while num > 0:
#     l = num % 10
#     if l > maxsim:
#         maxsim = l
#     if l < minim:
#         minim = l
#     num = num // 10
# print(minim, maxsim, sep='\n')
#
# didg = int(input())
# count = 0
# while didg > 0:
#     if didg % 10 == 7:
#         count += 1
#     didg = didg // 10
# print(count)

# digit = int(input())
# while digit > 0:
#     print(digit % 2)
#     digit = digit // 2

# n = int(input())
# i = 1
# su = 0
# while i <= n:
#     if n % i == 0:
#         su = su + i
#     i += 1
# print(su)
# n = 345
# m = 555
# while m > 0:
#     n, m = m, n % m
# print(n)
# a, b = map(int, input().split())
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

# a, b = map(int, input().split())
# c = a * b
# while b > 0:
#     a, b = b, a % b
# nok = int(c / a)
# print(nok)

# t = 7
# while t > 1:
#     t -= 1
#     if t == 3 or t == 1:
#         continue
#     print(t)

# n = int(input())

# i = 1
# while i <= n:
#     i += 1
#     if n % i == 0:
#         break
# print(i)

# a = int(input())
# b = int(input())
# a -= 1
# while a < b:
#     a += 1
#     if a % 777 == 0:
#         break
#     if a % 2 == 0 or a % 3 == 0:
#         continue
#     print(a)

# word = input()
# ind = 0
# while len(word) > ind:
#     if word[ind] == 'e' or word[ind] == 'a':# «Текущая буква: <letter>».
#         print('Ага! Нашлась')
#         break
#     else:
#         print(f'Текущая буква: {word[ind]}')
#         ind += 1
# else:
#     print('Распечатали все буквы')

# elements = list(range(10, -1, -1))
# print(elements)

# print(list(range(1000, 499, -50)))

# n = int(input())
# for n in range(1, n+1):
#     print(n)

# for i in range(0, 501 , 5):
#     print(i)

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# bit = 'Надо было брать биткоин в 2012!'
# for i in range(13):
#     print(bit)

# wo = input()
# n = int(input())
# for i in range(n):
#     print(wo)
#
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)
#
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     sq = i * i
#     cub = i ** 3
#     print(f'Число {i}; его квадрат = {sq}; его куб = {cub}')
# #
# n = int(input())
# su = 0
# for i in  range(n - 1, 0, -1):
#     if i % 3 == 0 or i % 5 == 0:  # Сумма  переданного числа n этих чисел
#         su = su + i
# print(su)

# su = 0
# for i in range(50, 101): # найдет сумму кубов натуральных
#     cub = i ** 3
#     su += cub
# print(su)
#
# n = int(input())
# pr = 1
# for i in  range(1, n+1): # Факториал числа n!
#     pr = pr * i
# print(pr)

# n = int(input()) # Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
# for i in range(n):
#     st = input().lower()
#     if "рок" in st:
#         print(i + 1, st.find('рок') + 1)
#
# n = int(input()) # картофелин штук 3, картошку пожарить и поперчить, сварить суп
# a = []
# for i in range(n):
#     st = input().lower()
#     if 'соль' not in st:
#         a.append(st)
# print(', '.join(a))
#
# numbers = [99, 50, -16, 9, 47, -62, 5, -64, -68, 85, 11, -20, 16, 96, -43, 46, -25, 33, 81, -30, 64, 66, -11, 60, 3, -5, -1,
#  -80, 49, -12, -86, -40, -98, -92, -91, -71, 56, -76, -30, -82, 17, -2, -64, 47, 22, -28, 40, 55, 54, -3, -58, -10,
#  -35, -15, -2, -60, 70, 50, -77, 83, -49, 42, 27, -58, -79, -2, -100, -42, -18, 38, 95, 9, 98, -89, -46, 96, 64,
#  -35, 41, 94, 1, -90, 29, 23, 39, -3, 11, -65, -64, 52, -69, 32, -14, -49, -28, -11, 85, -75, -6, 15]
# for i in  numbers:
#     print(i) #

# words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
#            'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
#            'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
#            'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
#            'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
#            'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
#            'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
#            'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
#            'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']
# for i in words:
#     if len(i) > 6:
#         print(i)

# numbers = [-35, 68, -91, 23, -92, -82, -74, 32, 39, -30, -100, -29, 54, 26, 54, -45, 20, 53, -17, 68, -35, 11, 26, -17, 70, 89, -81, -4, 61, -45, 13, 63, -48, -66, -92, -15, -88, -87, -75, 44, -49, -81, 19, -33, -59, 85, -69, -60, 9, -98, 28, 11, 15, -35, -80, 5, -20, -52, -45, 26, 47, -16, 40, -14, -12, 15, 73, -16, 29, -98, 93, -77, 1, 85, 77, 73, 100, -71, 99, 39, 2, -38, 49, -31, 15, 43, 94, -39, -89, -46, -71, 39, -56, 41, -93, 4, -79, 48, 88, -51]
# b = len(numbers)
# for i in range(b):
#     numbers[i] *= 2
# print(numbers)

# n = int(input())  # Заполняем список
# a = []
# for i in range(n):
#     st = input()
#     a.append(st)
# print(a)

# sp = list(map(int, input().split()))
# for i in range(len(sp)):
#     if i > 0:
#         print(min(sp))
# a = int(input())
# print(a)
# for i in range(-1, a):
#     input()
#     if a >= 1:
#         print('жопа')
#     else:
#         print('пержа')

# n = list(map(int, input())) #  метод подсчета
# count = [0] * 10
# for i in  n:
#     count[i] += 1
# for i in range(10):
#     if count[i] > 0:
#         print(i, count[i])

# n = int(input())
# digit = list(map(int, input().split()))  # Сортировка подсчетом
# count = [0] * 201
# for i in digit:
#     count[i] += 1
# for i in range(-100, 101):
#     if count[i] > 0:
#         print( (str(i) + ' ') * count[i] , end='')
#

# su = 0
# for i in range(1000, 10000): # найти сумму всех четырехзначных натуральных чисел
#     count = 0
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s == 20:
#         su += i
#         print(i, su)
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1): # построить лесенку из чисел.
#         print(j , end=' ')
#     print()
#
# n = list(map(int, input().split()))  # горизонтальных столбчатых диаграмм
# for i in n:
#     for j in range(i):
#         print('*', end='')
#     print()
#
# n = int(input())
# mas = list(map(int, input().split()))  # сортировки пузырьком.
# count = 0
# for run in range(n - 1):
#     for i in range(n - 1 - run):
#         if mas[i] > mas[i + 1]:
#             count += 1
#             mas[i], mas[i + 1] = mas[i + 1], mas[i]
# print(*mas)
# print(count)
#
# n, m = map(int, input().split())
# count = 0
# a = 0
# while a ** 2 <= n:
#     b = n - a ** 2
#     if b >=0 and a + b ** 2 == m:
#         count += 1
#     a += 1
# print(count)
#
# a = []
# n = int(input())
# for i in  range(n):
#     a.append(list(map(int, input().split())))   # посчитать сумму элементов двумерного квадратного (NxN) списка
# sum = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             sum += a[i][j]
# print(sum)
#
# a = []
# n = int(input())             # Необходимо обойти элементы этой матрицы сверху вниз слева направо
# for i in  range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(n):
#         print(a[j][i], end=' ')
#     print()

# a = []
# n = int(input())    # элементы этой матрицы снизу вверх справа налево
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         print(a[j][i], end=' ')
#     print()
#
# n, m = map(int, input().split())
# a = []
# for i in range(n):
#         a.append(list(map(int, input().split())))  # cправа налево сверху вниз
# for j in range(n):
#     for i in range(m - 1, -1, -1):
#         print(a[j][i],end=' ')
#     print()

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#         a.append(list(map(int, input().split())))  #слева направо снизу вверх
# for j in range(n - 1, -1, -1):
#     for i in range(m):
#         print(a[j][i],end=' ')
#     print()
#
# zeroes = [0 for i in range(100)]  #  список из 100 нулей

# n = [i + 1 for i in range(int(input()))]  # При помощи генератора-списка создайте список [1, 2, 3, ..., n]
# print(n)

# n = int(input())
# a = [i for i in range(1, n + 1) if n % i == 0]  # из делителей введенного числа
# print(a)

# n = int(input())
# a = [i for i in range(n, n * n + 1) if i % 2] # нечетные натуральные числа в интервале
# print(a)

# a, b = map(int, input().split()) # Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b
# n = [i * i for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
# print(n) # Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно

# st = 'Create a list of the first letters of every word in this string'.split()
# n = [i[0] for i in st] # первых букв каждого слова из строки st
# print(n)
#
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # ['A', 'B', 'C'] 3
# n = int(input())
# s = [a[i] for i in range(n)]
# print(s)

# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # ['A', 'BB', 'CCC'] 3
# n = int(input())
# s = [a[i] * (i + 1) for i in range(n)]
# print(s)
#
# phrase = 'Take only the words that start with t in this sentence'.split()
# n = [i for i in phrase if i[0].lower() == 't'] # создайте список начинающихся с буквы 't' или 'T
# print(n)

# empty = None  # True False
# empty_too = None
# print(empty is empty_too, empty is not empty_too, sep='\n' )

# i_love_none = [None for i in range(50)]
# print(i_love_none)

# my_tuple =1, 'too', 3, [7]
# lonely = 777,
# print(lonely)

# my_tuple = ('zara', 'h&m', 'mcdonalds', 'visa', 'ikea')
# print(min(my_tuple), max(my_tuple))

# sum = 0
# count = 0
# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# for i in list(my_tuple):
#     count += 1
#     sum += i
# print(sum / count)                  # вывела среднее арифметическое всех элементов кортежа

# print(sum(my_tuple) / len(my_tuple))

# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# result = a * 3 + b * 5 + c * 8 + d * 5
# print(result)

# a = int(input())
# b = int(input())
# n = [i for i in range(a, b + 1)]  # натуральные числа в интервале [a; b]
# print(tuple(n))

# n =int(input())        # нечетные натуральные числа в интервале
# s = [i for i in range(n, n * n + 1) if i % 2 != 0]
# print(tuple(s))

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20:]    #При помощи среза сохраните
# slice_to_35 = my_tuple[:35]
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)
#
# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# my_tuple = list(my_tuple)[::-1]       #Развернуть(reverse)
# print(tuple(my_tuple))
#
# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple.count(50)) # Нужно посчитать и вывести на экран сколько раз встречается значение 50 в кортеже my_tuple
#
# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in range(len(words_tuple)):
#     for j in range(i):
#         print(f'Длина слова {j} = {words_tuple[i]}')
#
# sum = 0
# count = 0
# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# for i in list(my_tuple):
#      if i % 2 != 0:                #  среднее арифметическое всех нечетных значений
#         sum += i
#         count += 1
# print(sum / count)
#
# my_dict = {}   # Создайте пустой словарь
# print(my_dict)

# person = {
#     'name': 'Vasya',
#     'surname': 'Petrov',    # Создайте словарь ключ-значения
#     'age': 25
# }
# print(person)

# sweet = {
#     "id": "0001",
#     "type": "donut",     #  начение ключа name, потом calories и напоследок id
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# print(sweet['name'], sweet['calories'], sweet['id'], sep= '\n')

# n = int(input())
# days = {
#     1: 31,
#     2: 28,
#     3: 31,         #  Ваша задача по введеному номеру месяца вывести количество дней
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
# print(days[n])
#
# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# sweet['weight'] = 230
# sweet['have_topping'] = True
# sweet['name'] = 'SuperCake'
# sweet['calories'] = 350
# print(sweet)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,      # Удалите из него ключи ppu и type
# }
# del sweet['ppu']
# del sweet['type']
# print(sweet)

# n = int(input())
# d = []
# for i in range(1, n + 1): # от 1 до n, а значениями соответствующего ключа будет значение ключа в квадрате.
#     d.append([i, i * i])
# print(dict(d))

# account = {
#   "id": 5681,
#   "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
#   "account_number": "6733198878",
#   "iban": "GB79PNXF20678598570754",
#   "bank_name": "AAC CAPITAL PARTNERS LIMITED",  # dlina
#   "routing_number": "007398728",
#   "swift_bic": "AACCGB21"
# }
# print(len(account))

# w = input()
# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# if w in currencies:
#     print(currencies[w])
# else:
#     print(f'Нет данных по {w}')

# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948", # список из всех ключей словаря
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# keys = list(account)
# print(keys)

# d1 = {'India': 'Delhi',
#       'Canada': 'Ottawa',
#       'United States': 'Washington D. C.'}
#
# d2 = {'France': 'Paris',
#       'Malaysia': 'Kuala Lumpur'} # sliynie
# capitals = d1 | d2
# print(capitals)
# #
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17"
# }
# user['secret'] = user.pop('password')      # При помощи метода pop переименуйте в нем следующие ключи:
# user['surname'] = user.pop('last_name')
# print(user)
#
# my_set = set()     # Создайте пустое множество
# print(my_set)

# my_list = [56, 59, 53, 75, 62, 61, 75, 65, 59, 62, 64, 53,
#            54, 62, 69, 53, 55, 62, 54, 66, 55, 57, 58, 75,
#            72, 55, 51, 56, 71, 66, 57, 56, 59, 73, 68, 57,
#            50, 54, 62, 68, 59, 64, 59, 59, 71, 68, 57, 54, 53, 72]
# sum = 0
# count = 0
# my_set = set(my_list)   # среднее арифметическое всех элементов найденного множества my_set.
# for i in my_set:
#     sum += i
#     count += 1
# print(sum / count)

# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# s = set_a & set_b #  вывести на экран количество элементов, которое содержится в результате пересечения множеств
# print(len(s))

# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# s = set_a | set_b  #   вывести на экран количество элементов, которое содержится в результате объединения множеств
# print(len(s))

# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,              # разность множеств
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# s = set_a - set_b
# s1 = set_b - set_a
# print(len(s), len(s1),sep='\n')

# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,  # симитрическая разность
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# s = set_a ^ set_b
# print(len(s))

# s = []
# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
#          'control', 'value', 'few', 'generation', 'service', 'national',
#          'tradition', 'government', 'mention', 'proposal']
# for i in words:
#     if len(i) > 6:
#         s.append(i)             #  вывести на экран количество уникальных слов, длина которых больше 6.
# print(len(set(s)))

# my_set = {'government', 'control', 'winter', 'few', 'generation',
#           'service', 'national', 'tradition', 'government'}
# my_set.update(['concert', 'brown', 'jacket', 'value'])
# print(my_set)   #  добавить в него 4 строковых элемента:
#
# my_set = {
#     'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#     'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#     'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#     'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#     'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention',
#     'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
#     'government', 'control', 'value', 'few', 'generation', 'service', 'national',
#     'tradition', 'government', 'mention', 'proposal'
# }
# my_set.remove('government')  #  удалить из него 3 строковых элемента
# my_set.remove('national')
# my_set.remove('tease')
# print(my_set)
# my_set = {
#     'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#     'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'preference',
#     'fascinate', 'earthflax', 'meadow', 'bitter', 'march', 'feel', 'wind', 'location',
#     'need', 'adviser', 'error', 'pneumonia', 'concert', 'value', 'value', 'disclose',
#     'glasses', 'tank', 'national', 'soup', 'feel', 'few', 'concert', 'wrestle',
#     'proposal', 'soup', 'sail', 'brown', 'service', 'proposal', 'winter', 'jacket',
#     'mention', 'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
#     'government', 'control', 'value', 'few', 'generation', 'service', 'national', 'tradition',
#     'government', 'mention', 'proposal', 'sunrise', 'refund', 'formulate', 'despise', 'hobby',
#     'noble', 'parameter', 'update', 'serious', 'potential', 'entry', 'week',
#     'tenant', 'debut', 'dentist', 'explode', 'default', 'slam'
# }
# my_set.discard('noble')
# my_set.discard('offend')
# my_set.discard('error')
# my_set.discard('eagle')
# my_set.discard('sail')
# print(my_set)

# my_frozen = frozenset()  # Создайте пустой объект frozenset
# print(my_frozen)

# words_with_position = []
# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',  #  на основании создать список кортежей words_with_position
#          'drop', 'produce', 'acquisition', 'cheap', 'strength',
#          'master', 'perception', 'noise', 'strange', 'am']
# for ind in enumerate(words, start=1):
#     words_with_position.append(ind[::-1])
# print(words_with_position)

# def keanu_reeves():
#     print("YOU'RE BREATHTAKING")  # только определение функции keanu_reeves


# def summa_n(t):  #  которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t
#     sum = 0
#     for i in range(1, t + 1):
#         sum += i
#     print(f'Я знаю, что сумма чисел от 1 до {t} равна {sum}')
#
# summa_n(5)

# def exponentiation(n):  #  выводит на экран через пробел квадрат i куб этого числа.
#     print(f'{n * n} {n ** 3}')
#
#
# exponentiation(3)

# def repeat_please_n_times(n):
#     for i in range(n):  #  должна n раз распечатать фразу "Just do it" в отдельной строчке
#         print('Just do it')
# repeat_please_n_times(4)

# объявление функции
# def is_between(name, surname, middlename):
#     if b <= a <= c or b >= a >= c:
#         print(True)
#     else:
#         print(False)  # печатает True, если первое число находится между двумя вторыми включительно
#
# # считываем данные
# a, b, c = map(int, input().split())
#
# # вызываем функцию
# is_between(a, b, c)

# # объявление функции
# def count_letter(text, letter):
#     print(text.count(letter))
#
# # считываем данные    #  должна выводить на экран найденное количество букв  letter в тексте text
# text = input()
# symbol = input()
# # вызываем функцию
# count_letter(text, symbol)

# объявление функции
# def print_initials(name, surname, middlename):
#     n = name[0].upper()
#     m = middlename[0].upper()   #  фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной,
#     s = surname.capitalize()
#     print(f'{s} {n}.{m}.')
#
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
#
# # вызываем функцию
# print_initials(name, surname, middlename)

# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]  #  чтобы все проверки прошли
# assert sum([1, 3, 5]) == sum([6, 3])
# assert max(3, -1, 9) != -1
# print('Проверки пройдены')
# #
# def is_person_teenager(age): # принимает на вход возраст человека и возвращает True или False
#     return 12 <= age <= 17
#

# def factorial(n):
#     pr = 1
#     for i in  range(2, n + 1):  # возвращает значение факториала
#         pr *= i
#     return pr
#
#
# n=int(input())
# print(factorial(n))

# # объявление функции
# def count_args(*args):  #  возвращать количество переданных ей на вход аргументов
#     return len(args)
#
# print(count_args(1, 2, 3))
#
# def check_sum(*args):  # Данная функция должна выводить not enough, если сумма всех элементов меньше 50
#     if sum(args) < 50:
#         print('not enough')
#     else:
#         print('verification passed')
#
# print(check_sum(20, 20, 10))

# def multiply(*args):
#     pr = 1
#     for i in args:  # должна находить произведение всех переданных значений и возвращать его в качестве результата
#         pr *= i
#     return pr
#
# print(multiply(2, 2, 3))

# adding_10 = lambda x: x + 10  # lambda функцию, которая принимает одно число и увеличивает его на 10.
# print(adding_10(1))

# starts_with = lambda s: True if s[0] == 'W' else False
# print(starts_with('World'))   # lambda функцию, которая принимает строку и возвращает True переданная строка начинается с буквы W.

# sale_lambda = lambda x: x * 0.9  #  которая возвращает цену товара со скидкой 10%.
#
# print(sale_lambda(100))

# sale_lambda = lambda x: x * 0.9 if x > 50 else x
#
# print(sale_lambda(60.0))  #только для тех товаров, стоимость которых больше 50
#
# sq = lambda x, y:  x ** 2 + y ** 2   # возвести в квадрат два числа и сложить полученные результаты
#
# print(sq(8, 11))

# average = lambda *args: sum(args) / len(args)
#
# print(average(4, 5, 6))   # принимает произвольное количество числовых аргументов и выводит их среднее

# отсортирует список subject_marks по возрастанию оценок, распечатайте предметы и оценки
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
#
# s = sorted(subject_marks, key=lambda x: int(x[1]))
# for i in s:
#   print(*i)

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# s = sorted(subject_marks, key=lambda x: int(x[1]), reverse=True)
# for i in s:     #  по убыванию оценок.
#     print(*i)

# по убыванию оценок. Предметы, имеющие одинаковые оценки, должны быть отсортированы в алфавитном порядке
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# s = sorted(subject_marks, key=lambda x: (-int(x[1]), x[0]))
# for i in s:
#     print(*i)

# def outer() -> None:
#     def say_hello() -> None:
#         print('hello')
#
#     def say_bye() -> None:   # чтобы на экран вывело bye и hello
#         print('bye')
#
#     say_bye()
#     say_hello()
#
# outer()
#
# def calculate(x:float, y:float, operation:str='a') -> None:
#     def addition():
#         print(x + y)
#
#     def subtraction():        # Пользуясь вложенными функциями, реализуйте простой калькулятор.
#         print(x - y)
#
#     def division():
#         print('На ноль делить нельзя!' if y == 0 else x / y)
#
#     def multiplication():
#         print(x * y)
#
#     if operation == 'a':
#         addition()
#     elif operation == 's':
#         subtraction()
#     elif operation == 'd':
#         division()
#     elif operation == 'm':
#         multiplication()
#     else:
#         print('Ошибка. Данной операции не существует')
#
# calculate(2, 5) # Печатает 7.0
# calculate(2.2, 15, 'a') # Печатает 17.2
# calculate(22, 15, 's') # Печатает 7.0
# calculate(2, 3.2, 'm') # Печатает 6.4
# calculate(10, 0, 'd') # Печатает 25.0

# from os import environ  #  взглянуть на значение, которое хранится под ключом 'HOME'
# print(environ.get('HOME'))
#
# from string import Template
# values = {'one': 'Привет', 'copter': 'Квадракоптер'}
#
# t = Template("""
# Ну что, мои хорошие, всем $one      # Импортируйте имя Template из модуля string, чтобы код ниже заработал
# Это шаблонная строка
# В нее можно вставлять значения по ключам
# Хочу сюда вставлю слово $copter, хочу сюда $copter
# """)
#
# print(t.substitute(values))

# my_file = open(r'C:\Users\79119\PycharmProjects\задачи\my_text.txt', encoding='utf-8')
# print(my_file.read(2))

# def file_read(file_name):
#     my_file = open(file_name, encoding='utf-8')
#     print(my_file.read()) # Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.

# a = 6  # Сторона квадрата # Посчитайте площадь и периметр квадрата, сторона которого равна 6.
#
# perimeter = 4 * 6  # Расчёт периметра
# area = 6 ** 2  # Расчёт площади
#
# print('Периметр:', perimeter)
# print('Площадь:', area)

# a = 5  # Сторона A  # Посчитайте площадь и периметр прямоугольника 5×7.
# b = 7  # Сторона B
#
# perimeter = 2 * (5 + 7)  # Расчёт периметра
# area = 5 * 7  # Расчёт площади
#
# print('Периметр:', perimeter)
# print('Площадь:', area)

# Задание «Приложение для финансового планирования»

# salary = 100000  # Заработная плата
# percent_mortgag = 30  # Ипотека
# percent_life = 50  # На жизнь
#
# # Напишите свой код здесь
# salary_year = salary * 12
# mortgage = salary_year * percent_mortgag / 100
# expenses = salary_year * percent_life / 100
# result = salary_year - (mortgage + expenses)
#
# print('Ипотека:', mortgage)
# print('Накопления:', result)

# d = (randint(1, 20) for i in range(7))
# print(int(d))
# #print((dict(d)))
# #print(list(d))
# # print(set(d))
# # print(tuple(d))
# # print(sorted(d))

# d = (i**2 for i in range(1, 6))
# a = list(d)    # акое значение будет храниться в переменной b после выполнения данного кода?
# b = tuple(d)
# print(a, b)

# d = (i**2 for i in range(1, 6))
# a = max(d)   # Какое значение будет храниться в переменной b после выполнения данного кода?
# b = min(d)
# print(b)
#
# d = (i ** 2 for i in range(1, 6))
# print(9 in d, 4 in d)

# print('Здравствуй, мир!')
# print(4, 8, 15, 16, 23, 42)
# print(4, 8, 15, 16, 23, 42, sep='\n')
#
# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******')
# print('*******)

# name = input()   # которая выводит на экран приветствие в виде слова «Привет»
# print('Привет,', name)
#
# name = input()
# print(name, '- чемпион!')

# a = int(input())  # Программа должна вывести три последовательно идущих числа
# b = a + 1
# c = b + 1
# print(a, b, c, sep='\n')

# num = int(input())   # Программа должна вывести сумму введенных чисел.
# num1 = int(input())
# num2 = int(input())
# print(num + num1 + num2)
#
# len_a = int(input())  # Объём куба и площадь полной поверхности можно вычислить по формулам
# volume = len_a ** 3
# square = 6 * len_a ** 2
# print('Объем =', volume)
# print(f'Площадь полной поверхности = {square}')
#
# a = int(input())  # Напишите программу вычисления значения функции по введеным целым значениям a and b
# b = int(input())
# f = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
# print(f)

# a = int(input())  # которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число
# b = a - 1
# c = a + 1
# print('Следующее за числом', a, "число:", c)
# print('Для числа', a, "предыдущее число:", b )

# a = int(input())  #  которая считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и
# b = int(input())
# c = int(input())
# d = int(input())
# print((a + b + c + d) * 3)

# a = int(input())
# b = int(input())   #   в которой вычисляется сумма, разность и произведение двух целых чисел
# print(f'{a} + {b} =', a + b)
# print(f'{a} - {b} =', a - b)
# print(f'{a} * {b} =', a * b)

# a1 = int(input())
# d = int(input())  # Программа должна вывести n-ый член арифметической прогрессии.
# n = int(input())
# a = a1 + d * (n - 1)
# print(a)
#
# x = int(input())  # x,2x,3x,4x и 5x, разделённых тремя черточками.
# print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')

# b1 = int(input())   # Программа должна вывести n-ый член геометрической прогрессии.
# g = int(input())
# n = int(input())
# b = b1 * g ** (n - 1)
# print(b)

# cen = int(input())  # Программа должна вывести одно число – полное число метров.
# print(cen // 100)

# n = int(input())  # n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине
# k = int(input())
# stud = k // n
# korzina = k % n
# print(stud, korzina, sep='\n')
#
# n = int(input())
# word = -n // 4 * -1
# print(word)
# #
# minutes = int(input())  #  для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах
# hour = minutes // 60
# col_min = minutes % 60
# print(f'{minutes} мин - это {hour} час {col_min} минут.')
#
# # # Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# number = int(input())
# digit3 = number % 10
# digit2 = number % 100 // 10
# digit1 = number // 100
# sum = digit1 + digit2 + digit3
# pr = digit1 * digit2 * digit3
# print('Сумма цифр =', sum)
# print('Произведение цифр =', pr)

# # Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа
# num = int(input())
# dig3 = num % 10
# dig2 = num % 100 // 10
# dig1 = num // 100
# print(dig1, dig2, dig3, sep='')
# print(dig1, dig3, dig2, sep='')
# print(dig2, dig1,dig3, sep='')
# print(dig2, dig3, dig1, sep='')
# print(dig3, dig1, dig2, sep='')
# print(dig3, dig2, dig1, sep='')

# numb = int(input()) # Напишите программу для нахождения цифр четырёхзначного числа.
# unit = numb % 10
# ten = numb % 100 // 10
# hin = numb % 1000 // 100
# chil = numb // 1000
# print('Цифра в позиции тысяч равна', chil)
# print('Цифра в позиции сотен равна', hin)
# print('Цифра в позиции десятков равна', ten)
# print('Цифра в позиции единиц равна', unit)

# Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно.
# print('*' * 17)
# print('*', '*', sep='               ')
# print('*', '*', sep='               ')
# print('*' * 17)

# a = int(input())  # Сумма квадратов VS квадрат суммы
# b = int(input())
# sqw_sum =(a + b) ** 2
# sum_sqw = a ** 2 + b ** 2
# print(f'Квадрат суммы {a} и {b} равен {sqw_sum}')
# print(f'Сумма квадратов {a} и {b} равна {sum_sqw}')

# a = int(input())  # Программа должна вывести значение a ** b + c ** d
# b = int(input())
# c = int(input())
# d = int(input())
# sum_sqw = a ** b + c ** d
# print(sum_sqw)
#
# n = int(input())
# rez = n + (n * 11) + (n * 111)
# print(rez)

# regions_dvostok = ['Амурская область','Еврейская автономная область','Забайкальский край','Камчатский край','Магаданская область','Приморский край','Республика Бурятия','Республика Саха','Сахалинская область','Хабаровский край','Чукотский автономный округ']
# salary = ('Да')
# insurance = ('Да')
# regions = input('Введите регион проживания :  ')
# if regions in regions_dvostok :
#   print ('Базовая ставка для Вашего региона - 2 %')
# else:
#   num_child = int(input('Введите количество детей:  '))
# if num_child >= 3 :
#   print ('Базовая ставка уменьшается на 1 % и составляет 6.8 % '  )
# else:
#   print ('  Возможно у Вас имеются другие льготы \n для снижения процентной ставки '  )
# salary_client = input('Являетесь ли Вы зарплатным клиентом банка ?:  ')
# if  salary in salary_client :
#    print ('Базовая ставка 7.8 % снизилась на 0.5 %  '  )
# else :
#   print ('Предлагаем Вам стать нашим зарплатным клиентом \n ,     для Большей выгоды !')
# insur_client = input('        А,Если Вы оформите страховку \n, то базовая ставка уменьшается на 1.5 % \n Желаете оформить страховку ? :  ')
# if insurance in insur_client :
#    print ('Базовая ставка снижена  еще на 1.5 %  '  )
# else :
#   print ('Обратитесь к работникам нашего банка!\n Они помогут подобрать нужную программу !')

# Ипотечный калькулятор В новом банке решили начать выдавать ипотеку. Появилась необходимость разработать для них ипотечный калькулятор. Нужно рассчитать финальную процентную ставку по ипотеке. От каких критериев зависит скидка на ипотеку:
#
# Если клиент из Дальнего Востока(список регионов определить самостоятельно), то базовая ставка становится 2%.
# Если количество детей больше 3, то базовая ставка уменьшается на 1%.
# Если у клиента зарплатный проект в этом банке, то базовая ставка уменьшается на 0.5%.
# Если в этом же банке будет оформлена страхование, то базовая ставка уменьшается на 1.5% Базовую процентную ставку выбрать самостоятельно. Если клиент оформляет ипотеку по дальневосточной программе, то остальные скидки не применяются.
#
# interest_rate = 7
# region = input('Вы проживаете на Дальнем востоке (да или нет)?: ').lower()
# if region == 'да':
#     print('Ваша базовая ставка становится 2%.')
# else:
#     number_children = int(input('Введите количество детей: '))
#     salary_client = input('У вас есть зарплатный проект в этом банке (да или нет)?: ').lower()
#     insurance = input('Нужна ли Вам страховка в нашем банке (да или нет)?: ').lower()
#     if number_children > 3:
#        interest_rate -= 1
#     if salary_client == 'да':
#        interest_rate -= 0.5
#     if insurance == 'да':
#        interest_rate -= 1.5
#     print(f'Ваша базовая ставка уменьшается и составляет {interest_rate}%.')

# # Введите месяц: март
# # Введите число: 6
# #
# # Вывод:
# # Рыбы if month == "декабрь" and 1 <= day <= 22 ...
# month = input('Введите месяц: ')
# number = int(input('Введите число: '))
# if month == 'декабрь' and 22 <= number <= 31 or month == 'январь' and 1 <= number <= 20:
#     print('Козерог')
# if month == 'январь' and 20 < number <= 31 or month == 'февраль' and 1 <= number <= 19:
#     print('Водолей')
# if month == 'февраль' and 19 < number <= 28 or month == 'март' and 1 <= number <= 20:
#     print('Рыбы')
# if month == 'март' and 20 < number <= 31 or month == 'апрель' and 1 <= number <= 20:
#     print('Овен')
# if month == 'апрель' and 20 < number <= 30 or month == 'май' and 1 <= number <= 20:
#     print('Телец')
# if month == 'май' and 20 < number <= 31 or month == 'июнь' and 1 <= number <= 21:
#     print('Близнецы')
# if month == 'июнь' and 21 < number <= 30 or month == 'июль' and 1 <= number <= 22:
#     print('Рак')
# if month == 'июль' and 22 < number <= 31 or month == 'август' and 1 <= number <= 23:
#     print('Лев')
# if month == 'август' and 23 < number <= 31 or month == 'сентябрь' and 1 <= number <= 23:
#     print('Дева')
# if month == 'сентябрь' and 23 < number <= 30 or month == 'октябрь' and 1 <= number <= 23:
#     print('Весы')
# if month == 'октябрь' and 23 < number <= 31 or month == 'ноябрь' and 1 <= number <= 22:
#     print('Скорпион')
# if month == 'ноябрь' and 22 < number <= 30 or month == 'декабрь' and 1 <= number <= 21:
#     print('Стрелец')

# num = int(input()) # соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# if num // 1000 + num % 10 == num % 1000 // 100 - num % 100 // 10:
#     print('ДА')
# else:
#     print('НЕТ')

# age = int(input())  # Доступ разрешен» если возраст не менее 18
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a = int(input())  # являются ли три заданных числа (в указанном порядке) последовательными членами арифмит прогрес
# b = int(input())
# c = int(input())
# if b - a + b == c:
#     print('YES')
# else:
#     print('NO')

# a = int(input())  # определяет наименьшее из двух чисел.
# b = int(input())
# if a > b:
#     print(b)
# else:
#     print(a)

# a = int(input()) # , которая определяет наименьшее из четырёх чисел
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a, b, c, d))

# age = int(input()) # по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# if 0 < age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 24 < age <= 59:
#     print('зрелость')
# if age > 59:
#     print('старость')

# a = int(input()) #  которая считывает три числа и подсчитывает сумму только положительных чисел.
# b = int(input())
# c = int(input())
# sum = 0
# if a > 0:
#     sum += a
# if b > 0:
#     sum += b
# if c > 0:
#     sum += c
# print(sum)

# a = 2
# b = 4
# c = 6
# if not (c <= 10):
#     print(True)
# else:
#     print(False)

# x = int(input())  # которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку.
# if -1 < x < 17:
#   print('Принадлежит')
# else:
#   print('Не принадлежит')

# x = int(input())  #  которая принимает целое число  x и определяет, принадлежит ли данное число указанным промежуткам.
# if x <= -3 or x >= 7:
#   print('Принадлежит')
# else:
#   print('Не принадлежит')

# x = int(input())  #  которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам
# if -30 < x <= - 2 or 7 < x <= 25:
#   print('Принадлежит')
# else:
#   print('Не принадлежит')

# num = int(input())  # если оно является четырехзначным и делится нацело на 7 или на 17
# if 1000 <= num < 10000 and (num % 7 == 0 or num % 17 == 0):
#   print('YES')
# else:
#   print('NO')
#
# a = int(input())  #  Треугольник существует, если выполняется неравенство треугольника.
# b = int(input())
# c = int(input())
# if a < b + c and b < a + c and c < a + b:
#     print('YES')
# else:
#     print('NO')

# year = int(input())  # Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# n = int(input()) # нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно
# k = int(input())
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# elif n == k:
#     print("Don't know")

# a = int(input())  # вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»)
# b = int(input())
# c = int(input())
# if a == b and a == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# elif a != b and a != c and b != c:
#     print('Разносторонний')

# a = int(input()) # Напишите программу, которая находит среднее по величине число
# b = int(input())
# c = int(input())
# if b < a < c or b > a > c:
#     print(a)
# elif a < b < c or a > b > c:
#     print(b)
# elif a < c < b or a > c > b:
#     print(c)

# month = int(input())  # Программа должна вывести количество дней в этом месяце.
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print(31)
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print(30)
# else:
#     print(28)

# weight = int(input())  # Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых
# if weight < 60:
#     print('Легкий вес')
# elif weight < 64:
#     print('Первый полусредний вес')
# elif weight < 69:
#     print('Полусредний вес')

# a = int(input())  # Самописный калькулятор
# b = int(input())
# st = input()
# if st == '/' and b == 0:
#     print('На ноль делить нельзя!')
# elif st == '/':
#     print(a / b)
# elif st == '+':
#     print(a + b)
# elif st == '-':
#     print(a - b)
# elif st == '*':
#     print(a * b)
# else:
#     print('Неверная операция')

# colour = input()  # Цветовой микшер
# colour1 = input()
# if colour == 'красный' and colour1 == 'красный':
#     print('красный')
# elif colour == 'синий' and colour1 == 'синий':
#     print('синий')
# elif colour =='желтый' and colour1 == 'желтый':
#     print('желтый')
# elif colour == 'красный' and colour1 == 'синий' or colour == 'синий' and colour1 == 'красный':
#     print('фиолетовый')
# elif colour == 'красный' and colour1 == 'желтый' or colour == 'желтый' and colour1 == 'красный':
#     print('оранжевый')
# elif colour == 'синий' and colour1 == 'желтый' or colour == 'желтый' and colour1 == 'синий':
#     print('зеленый')
# else:
#     print('ошибка цвета')

# num = int(input())  цвета рулетки
# if num == 0:
#     print('зеленый')
# elif 1 <= num < 10 and num % 2 != 0 or 11 <= num <= 18 and num % 2 == 0 or 19 <= num <= 28 and num % 2 != 0 or 29 <= num <= 36 and num % 2 == 0:
#     print('красный')
# elif 1 < num <= 10 and num % 2 == 0 or 11 <= num <= 18 and num % 2 != 0 or 19 <= num <= 28 and num % 2 == 0 or 29 <= num <= 36 and num % 2 != 0:
#     print('черный')
# else:
#     print('ошибка ввода')

# year = input() #  оканчивается ли год с данным номером на два нуля
# if year[-1] == '0' and year[-2] == '0':
#     print('YES')
# else:
#     print('NO')

# age = int(input()) #  подаётся натуральное число – возраст претендента и буква обозначающая пол
# gender = input()
# if 10 <= age <= 15 and gender == 'f':
#     print('YES')
# else:
#     print('NO')

# num = int(input())  # которая считывает целое число и выводит соответствующую ему римскую цифру
# if num == 1:
#     print('I')
# elif num == 2:
#     print('II')
# elif num == 3:
#     print('III')
# elif num == 4:
#     print('IV')
# elif num == 5:
#     print('V')
# elif num == 6:
#     print('VI')
# elif num == 7:
#     print('VII')
# elif num == 8:
#     print('VIII')
# elif num == 9:
#     print('IX')
# elif num == 10:
#     print('X')
# else:
#     print('ошибка')
# num = int(input())  # которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO
# if num % 2 != 0:
#     print('YES')
# elif 2 <= num <= 5 and num % 2 == 0:
#     print('NO')
# elif 6 <= num <= 20 and num % 2 == 0:
#     print('YES')
# elif num > 20 and num % 2 == 0:
#     print('NO')

# cat = float(input())  # которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# cat2 = float(input())
# squera = 0.5 * cat * cat2
# print(squera)

# distance = float(input())  # Определите, через какое время старушки встретятся
# speed = float(input())
# speed2 = float(input())
# time_ = distance / (speed + speed2)
# print(time_)

# num = float(input())  # которая считывает с клавиатуры одно число и выводит обратное ему
# if num == 0:
#     print('Обратного числа не существует')
# else:
#     print(num ** -1)

# grade = float(input())  # определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта
# temperature = (5 / 9) * (grade - 32)
# print(temperature)
#
# dog_age = int(input())  # В течение первых двух лет собачий год равен 10.5 человеческим годам
# human_year = 10.5       # После этого каждый год собаки равен 4
# if 0 < dog_age <= 2:
#     dog_age *= human_year
# else:
#     dog_age = dog_age * 4 +13
# print(dog_age)

# num = float(input()) # Дано положительное действительное число. Выведите его первую цифру после десятичной точки
# digit = num * 10 % 10
# print(int(digit))

# num = float(input())  # Дано положительное действительное число. Выведите его дробную часть
# num2 = int(num)
# res = num - num2
# print(res)

# num = int(input())  # Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
# print(f'Наименьшее число =', min(num, num2, num3, num4, num5))
# print(f'Наибольшее число =', max(num, num2, num3, num4, num5))

# num = int(input()) # Напишите программу, которая упорядочивает три числа от большего к меньшему.
# num2 = int(input())
# num3 = int(input())
# mid = num + num2 + num3 - max(num, num2, num3) - min(num, num2, num3)
# print(max(num, num2, num3), mid, min(num, num2, num3), sep='\n')

# num = int(input()) # если в нем разность максимальной и минимальной цифры равняется средней по величине цифре
# dig3 = num % 10
# dig2 = num % 100 // 10
# dig = num // 100
# if max(dig, dig3) - min(dig, dig3) == dig2 or max(dig, dig3) + min(dig, dig3) == dig2:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# a = float(input())  # Напишите программу, которая вычисляет сумму их модулей
# b = float(input())
# c = float(input())
# d = float(input())
# s = float(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(s))

# p1 = int(input())  # Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы
# p2 = int(input())
# q1 = int(input())
# q2= int(input())
# rez = abs(p1 - q1) + abs(p2 - q2)
# print(rez)

# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

# name = input() #  которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу
# sur_name = input()
# print(f'Hello {name} {sur_name}! You just delved into Python')

# team_foot = input() # Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу
# len_ = len(team_foot)
# print(f'Футбольная команда {team_foot} имеет длину {len_} символов')

# cities1 = input()
# cities2 = input()  # Напишите программу, которая определяет самое короткое и самое длинное название города
# cities3 = input()
# if len(cities1) < len(cities2) < len(cities3):
#     print(cities1, cities3, sep='\n')
# elif len(cities2) < len(cities3) < len(cities1):
#     print(cities2, len(cities1), sep='\n')
# elif len(cities3) < len(cities1) < len(cities2):
#     print(cities3, cities2, sep='\n')
# elif len(cities1) < len(cities3) < len(cities2):
#     print(cities1, cities2, sep='\n')
# elif len(cities3) < len(cities2) < len(cities1):
#     print(cities3, cities1, sep='\n')

# colour = input() # выводит «YES», если в введенной строке есть подстрока «синий
# if 'синий' in colour:
#     print('YES')
# else:
#     print('NO')

# s = input()  # если в введённой строке есть подстрока «суббота» или «воскресенье
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')

# s = input()  # имейл
# if '@' in s and '.' in s:
#     print('YES')
# else:
#     print('NO')

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys) == len(girls):  # Если количество людей в списках будет не совпадать
#     boys.sort()            #  отсортируем имена по алфавиту
#     girls.sort()
#     ideal_couples = zip(boys, girls)   # «Познакомить» пары нам поможет функция zip
#     print("Идеальные пары:")
#     for boy, girl in ideal_couples:   # В цикле распакуем zip-объект
#         print(f'{boy} и {girl}')      # выведем информацию в виде
# else:
#     print('Кто-то может остаться без пары!')   #  то мы никого знакомить не будем

# person = 5   #  количество людей
# cook_book = [          #  которой хранится информация об ингредиентах блюд и их количестве в расчёте на одну порцию:
#   ['салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['майонез', 70, 'мл.'],
#       ]
#   ],
#   ['пицца',
#       [
#         ['сыр', 50, 'гр.'],
#         ['томаты', 50, 'гр.'],
#         ['тесто', 100, 'гр.'],
#         ['бекон', 30, 'гр.'],
#         ['колбаса', 30, 'гр.'],
#         ['грибы', 20, 'гр.'],
#       ],
#   ],
#   ['фруктовый десерт',
#       [
#         ['хурма', 60, 'гр.'],
#         ['киви', 60, 'гр.'],
#         ['творог', 60, 'гр.'],
#         ['сахар', 10, 'гр.'],
#         ['мед', 50, 'мл.'],
#       ]
#   ]
# ]
# for dish, recipe in cook_book:      #  вывести пользователю список покупок необходимого количества ингредиентов
#     print(f'{dish.capitalize()}:')
#     for product, size, measure in recipe:
#         print(f'{product}, {size * person} {measure}')
#     print()

# x1, x2, y1, y2 = float(input()), float(input()), float(input()), float(input())
# distance = ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** 0.5  # Евклидово расстояние
# print(distance)

# from math import pi  # программу определяющую площадь круга и длину окружности по заданному радиусу R.
# r = float(input())
# s = pi * r ** 2
# c = 2 * pi * r
# print(s, c,sep='\n')

# a = float(input()) # Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
# b = float(input())
# arithmetic = (a + b) / 2
# geometric = (a * b) ** 0.5
# harmonic = 2 * a * b / (a + b)
# quadratic = ((a ** 2 + b ** 2) / 2) ** 0.5
# print(arithmetic, geometric, harmonic, quadratic, sep='\n')

# from math import cos, sin, tan, pi, radians #  вычисляющую значение тригонометрического выражения
# x = radians(float(input()))
# trigonometric = sin(x) + cos(x) + tan(x) ** 2
# print(trigonometric)

# from math import ceil, floor #  потолок числа,  пол числа.
# x = float(input())
# rez = ceil(x) + floor(x)
# print(rez)

# a, b, c = float(input()), float(input()), float(input())
# discriminant = b ** 2 - 4 * a * c
# x1 = (-b + discriminant ** 0.5) / (2 * a)
# x2 = (-b - discriminant ** 0.5) / (2 * a)
# if discriminant < 0:
#     print('Нет корней')   # Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# elif discriminant == 0:
#     print(-b / (2 * a))
# elif discriminant > 0:
#     print(min(x1, x2), max(x1, x2), sep='\n')
#
# from math import pi, tan
# n = int(input()) # Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле:
# a = float(input())
# squer = (n * a ** 2) / (4 * tan(pi / n))
# print(squer)

# for i in range(10):  #  которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
#   print('Python is awesome!')

# s = input()  # Программа должна вывести указанное текстовое предложение нужное количество раз
# s2 = int(input())
# for i in range(s2):
#   print(s)

# for i in range(6): # ровно три цикла for для печати следующей последовательности символов
#   print('AAA')
# for i in range(5):
#   print('BBBB')
# print('E')
# for i in range(9):
#   print('T' * 5)
# print('G')
#
# n = int(input())  # Напишите программу, которая печатает звездный прямоугольник размерами n×19
# for i in range(n):
#   print('*' * 19)

# st = input()  #  считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9
# for i in range(10):
#     print(i, st)

# n = int(input()) # Квадрат числа
# for i in range(n + 1):
#     print(f'Квадрат числа {i} равен {i * i}')

# cathet = int(input()) # Программа должна вывести треугольник в соответствии с условием задачи.
# for i in range(cathet, 0, -1):
#     print(i * '*')

# m, n = int(input()), int(input()) #  Напишите программу, которая выводит все числа от m до n включительно.
# for i in range(m, n + 1):
#     print(i)

# m, n = int(input()), int(input()) # т все числа от m до n включительно в порядке возрастания, или в порядке убывания в противном случае.
# if m < n:
#   for i in range(m, n + 1):
#     print(i)
# else:
#     for i in range(m, n - 1, -1):
#       print(i)

# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#   if i % 2 != 0: #  которая выводит все нечетные числа от m доn включительно v порядке убывания
#     print(i)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#   if i % 17 == 0:        # число кратно 17;число оканчивается на 9;число кратно 3 и 5 одновременно.
#     print(i)
#   elif i % 10 == 9:
#     print(i)
#   elif i % 3 == 0 and i % 5 == 0:
#     print(i)
#
# n = int(input())  #  таблицу умножения на n.
# for i in range(1, 11):
#   print(f'{n} x {i} = {n * i}')

# counter = 0  # подсчитывает количество чисел  куб которых оканчивается на 4 или 9
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#   if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#     counter += 1
# print(counter)

# total = 0
# n = int(input()) # которая подсчитывает сумму введенных чисел.
# for i in range(n):
#     n2 = int(input())
#     total += n2
# print(total)

# n = int(input()) # подсчитывает сумму тех чисел от 1 до n  квадрат которых оканчивается на 2 or 5 or 8
# total = 0
# for i in range(1, n + 1):
#     if i * i % 10 == 2 or i * i % 10 == 5 or i * i % 10 == 8:
#         total += i
# print(total)

# n = int(input()) # Факториал
# total = 1
# for i in range(1, n +1):
#     total *= i
# print(total)

# total = 1
# for i in  range(10): # , которая считывает 10 чисел и выводит произведение отличных от нуля чисел
#     num = int(input())
#     if num > 0:
#         total *= num
# print(total)
#
# courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
#            "Frontend-разработчик с нуля"]
#
# mentors = [
#     ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
#      "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
#      "Роман Гордиенко"],
#     ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
#      "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
#      "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
#      "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
#     ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
#      "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
#      "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
#     ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
#      "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
#
# # Добавьте в список всех преподавателей со всех курсов
# all_list = []
# for m in mentors:
# # Допишите здесь ваш код, который заполнит all_list. Можете как складывать списки, так и использовать метод extend
#     all_list.extend(m)
# # Сделайте список all_names_list, состоящий только из имён, и заполните его
# all_names_list = []
# for mentor in all_list:
#     name = mentor.split(' ')[0]
#     all_names_list.append(name)
#
# # Сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
# unique_names = set(all_names_list)
#
# # Теперь необходимо отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
# # Допишите код ниже
# all_names_sorted = sorted(unique_names)
# # Допишите конструкцию вывода результата. Можете использовать string.join()
# # Результат будет в all_names_sorted
# print(f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}')
#

# courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
#
# mentors = [
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
#
#
# # Добавьте сюда ваш код из Задачи 1
# all_list = []
# for m in mentors:
#     all_list.extend(m)
# all_names_list = []
# for mentor in all_list:
#      name = mentor.split(' ')[0]
#      all_names_list.append(name)
# unique_names = set(all_names_list)
# all_names_sorted = sorted(unique_names)
#
# # Уникальные имена будут в unique_names
# unique_names = ", ".join(all_names_sorted)
#
# # Подсчитайте встречаемость каждого имени через list.count()
# popular = []
# for name in all_names_list:
#     popular.append((name, all_names_list.count(name))) # добавьте подсчет имен
#
# popular = list(set(popular)) # Добавьте подсчёт имён
#
# # Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
# # Используйте его, как есть, или напишите собственный :)
# popular.sort(key=lambda x:x[1], reverse=True)
#
# # Получите топ-3 часто встречающихся имён из списка popular
# # Подсказка: возьмите срез списка
#
# top_3 = popular[:3]
# print(', '.join([f"{n[0]}: {n[1]} раз(а)" for n in top_3]))

# total = 0
# n = int(input())  # программу, которая вычисляет сумму всех его делителей.
# for i in range(1, n + 1):
#   if n % i == 0:
#     total += i
# print(total)

# n = int(input()) # Знакочередующаяся сумма
# total = 0
# for i in range(1, n + 1):
#   if i % 2 == 0:
#     total -= i
#   else:
#     total += i
# print(total)

# counter = 0
# for i in  range(10): # определяет является ли каждое из них четным
#     n = int(input())
#     if n % 2 == 0:
#         counter += 1
# if counter == 10:
#     print('YES')
# else:
#     print('NO')
#
# s = input() # которая выводит члены данной последовательности. До КОНЦА
# while s != 'КОНЕЦ':
#     print(s)
#     s = input()

# s = input()  #  Концом последовательности является слово «КОНЕЦ» или «конец»
# while s != 'КОНЕЦ' and s != 'конец':
#     print(s)
#     s = input()

# counter = 0  # количество членов данной последовательности.Концом одно из трех слов: «стоп», «хватит», «достаточно
# s = input()
# while s != 'стоп' and s != 'хватит' and s != 'достаточно':
#     counter += 1
#     s = input()
# print(counter)
#
# s = int(input()) #  Концом последовательности является любое число не делящееся на 7, которая выводит члены данной
# while s % 7 == 0:
#     print(s)
#     s = int(input())

# total = 0 # Сумма чисел Концом последовательности является любое отрицательное число.
# s = int(input())
# while s >= 0:
#     total += s
#     s = int(input())
# print(total)

# # Задание «Суперимена: преподаватели с какими именами учат сразу на двух курсах?»
# courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
#
# mentors = [
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
#
# # Делаем список списков имён
# mentors_names = []
# for m in mentors:
# 	course_names = []
# 	for name in m:
# 		course_names.append(name.split()[0]) # Допишите код здесь
# 	# Допишите ниже код, который добавляет списки имён в общий список mentors_names:
# 	mentors_names.append(course_names)
#
# # Храните здесь пары курсов, в которых есть совпавшие имена
# pairs = []
# # # Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
# for id1 in range(len(mentors_names)):
# 	for id2 in range(len(mentors_names)):
# 		# Проверьте, что вы не сравниваете список сам с собой:
# 		if id1 != id2:
# 		# Допишите ниже код для сравнения двух "наборов" преподавателей. Подсказка: используйте множества
# 			intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
# 			if len(intersection_set) > 0: # Допишите проверку, что результат не пустой, имена есть
# 			# Допишите ниже код, который проверяет, что эта пара ещё не встречалась
# 				pair = {courses[id1], courses[id2]}
# 			# Если pair еще не встречалась, то выведите на экран два курса и список преподавателей, которые есть на обоих курсах
# 			if pair not in pairs:
# 				pairs.append(pair)
# 				# Отсортируйте имена по алфавиту. Подсказка: используйте sorted() для списка
# 				all_names_sorted = sorted(list(intersection_set))
# 				# Допишите конструкцию вывода результата. Можете использовать string.join()
# 				print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
#

# # Задание «О чём говорит имя»
# courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
#
# mentors = [
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
#
# codes_info = [
# 	"",
# 	"1 — число цели, которая проявляется в форме агрессивности и амбиций",
# 	"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
# 	"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
# 	"4 — означает устойчивость и прочность",
# 	"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
# 	"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
# 	"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
# 	"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
# 	"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
# ]
# # Здесь ничего менять не нужно, это готовый код, который считает число имени
# def calc_namecode(name):
# 	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
# 			   "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
#
# 	name = name.upper()
# 	code = 0
# 	for letter in name:
# 		try:
# 			ltr_code = letters.index(letter) % 9
# 		except:
# 			continue
# 		if ltr_code == 0:
# 			ltr_code = 9
# 		code += ltr_code
#
# 	while code > 9:
# 		curr = code // 10 + code % 10
# 		code = curr
#
# 	return code
#
# # Добавьте сюда ваш код из Задачи 1
# all_list = []
# for m in mentors:
#      all_list.extend(m)
# all_names_list = []
# for mentor in all_list:
#      name = mentor.split(' ')[0]
#      all_names_list.append(name)
# unique_names = set(all_names_list)
# all_names_sorted = sorted(unique_names)
# # Уникальные имена будут в unique_names
# #unique_names = ", ".join(all_names_sorted)
#
# # Этот код создаст вам уже готовый (пока что пустой) список, в который вы будете добавлять имена
# names_codes = [[] for n in range(10)]
#
# # Подсказка: в список names_codes дописывайте список имён с группировкой по числу имени.
# # Рекомендуем для простоты список с именами записывать по индексу, который равняется числу имени
# # Например, код имени Владимир — 2, и итоговый результат был бы
# # names_codes = [[], [], ["Владимир"]] - внутренний список с именем Владимир находится по индексу 2 в списке names_codes
# # Самый первый список с индексом 0 будет всегда пустым, т. к. нет числа имени 0
#
# # Перебираем все имена и группируем их по числу имени
# for name in unique_names:
# 	# Команду ниже используйте как есть - она вычисляет число имени. На входе функция принимает имя (регистр не важен)
# 	# На выходе возвращает целое число от 1 до 9 - это число имени. Например, если введёте "Анна" - получите 5
# 	code = calc_namecode(name)
#
# 	# Допишите код, который добавит ещё одно имя к нужному числу имени в списке names_codes
# 	names_codes[code].append(name)
#
# # Выводим окончательный результат на экран
# for id, _ in enumerate(names_codes):
# 	if id == 0:
# 		continue
# 	# Допишите вывод расшифровки числа имени из codes_info
# 	# Должно выводиться так: 1 — число цели, которая проявляется в форме агрессивности и амбиций
# 	print(codes_info[id])
#
# 	# Теперь нужно отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
# 	# Допишите код ниже:
# 	all_names_sorted = sorted(list(names_codes[id]))
#
# 	# Допишите код, который выводит сообщение на экран
# 	# Должно выводиться так: Коду 1 соответствуют: Азамат, Денис, Роман, Ринат, Евгений, Адилет, Сергей
# 	print(f"Коду {id} соответствуют: {', '.join(all_names_sorted)}")

# num = int(input()) # Напишите программу, которая выводит его цифры в столбик в обратном порядке.
# while num != 0:
#   dig = num % 10
#   num = num // 10
#   print(dig)

# n = int(input()) #  Напишите программу, которая меняет порядок цифр числа на обратный
# while n != 0:
#   dig = n % 10
#   n = n // 10
#   print(dig, end = '')

# n = int(input()) # сумму его цифр; количество цифр в нем; произведение его цифр; среднее арифметическое его цифр;
#                         # его первую цифру; сумму его первой и последней цифры.
# total = 0
# counter = 0
# multi = 1
# last_dig = n % 10
# while n != 0:
# 	dig = n % 10
# 	n = n // 10
# 	counter += 1
# 	total += dig
# 	multi *= dig
# print(total, counter, multi, total / counter, dig, last_dig + dig, sep='\n')

# n = int(input()) # Напишите программу, которая определяет его вторую (с начала) цифру.
# while n > 9:
# 	dig = n % 10
# 	n = n // 10
# print(dig)

# n = int(input()) #  которая определяет, состоит ли указанное число из одинаковых цифр.
# counter = 0
# l_dig = n % 10
# while n != 0:
# 	digit = n % 10
# 	n = n // 10
# 	if l_dig != digit:
# 		counter += 1
# if counter > 0:
# 	print('NO')
# else:
# 	print('YES')

# n = int(input())  # . Напишите программу, которая выводит его наименьший отличный от 1 делитель. n > 1
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break
#
# n = int(input())
# for i in range(1, n +1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# count = 0 #  которая выводит на экран количество неотрицательных чисел последовательности и их произведение
# p = 1
# for i in range(10):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')
#
# s = 0 # подсчитывает и выводит сумму всех чётных чисел последовательности или 0 если чётных чисел в последовательности нет
# for i in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# if s > 0:
#     print(s)
# else:
#     print(0)

# n = int(input()) #  написать программу, которая выводит на экран его первую (старшую) цифру.
# while n > 9:
#     n1 = n % 10
#     n //= 10
# print(n)

# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input()) #  которая печатает таблицу размером n×3 состоящую из данного числа числа отделены одним пробелом).
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()
#
# n = int(input()) # оторая печатает таблицу размером n×5, где в i-ой строке указано число i
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())  # которая печатает таблицу сложения для всех чисел от 1 до n в соответствии с примером
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}', end=' ')
#         print()
#     print()
#
# n = int(input())  #  которая печатает численный треугольник в соответствии с примером
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# counter = 0 # Численный треугольник 3
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         counter += 1
#         print(counter, end=' ')
#     print()

# n = int(input())  # печатает равнобедренный звездный треугольник
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(n // 2, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

# n = int(input())  # Численный треугольник 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()

# courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
# mentors = [
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
# durations = [14, 20, 12, 20]
#
# # В этот список будут добавляться словари-курсы
# courses_list = []
# for courses, mentors, duration in zip(courses,mentors,durations):# Допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"
# 	course_dict = {'title':courses, 'mentors':mentors, 'duration':duration}
# 	courses_list.append(course_dict)
# # Найдите самое маленькое и самое большое значение длительности курса
# # Подсказка: используйте функции min и max для списка durations
# min = min(durations)
# max = max(durations)
# # Как видите, в duration встречаются одинаковые длительности курса. Допишите код, который это учитывает
# # Подсказка 1: найдите индексы, по которым в списке durations встречается самое маленькое и самое большое значение
# # Подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate
# maxes = []
# minis = []
# for index, duration in enumerate(durations):
# 	if durations[index] == max:
# 		maxes.append(index)
# 	elif durations[index] == min:
# 		minis.append(index)
# # Соберите все названия самых коротких и самых длинных курсов
# # Так как курсов с одной длительностью может быть больше одного,
# # создайте список названий самых коротких (courses_min) и самых длинных (courses_max) курсов
# courses_min = []
# courses_max = []
# for id in minis:
# 	courses_min.append(courses_list[id]['title']) # Допишите код, который берёт по id нужный курс из courses_list и получает название курса из ключа "title"
# for id in maxes:
# 	courses_max.append(courses_list[id]['title'])
# Допишите конструкцию вывода результата. Можете использовать string.join()
# print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min} месяца(ев)')
# print(f'Самый длинный курс(ы): {", ".join(courses_max)} - {max} месяца(ев)')

# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')

# st = input() # Напишите программу, которая выводит элементы строки с индексами 0, 2, 4...
# for index in range(0, len(st), 2):
# 	print(st[index])

# st = input()  # Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
# for ind in range(1, len(st) + 1):
# 	print(st[-ind])

# name = input() # Напишите программу, которая выводит инициалы человека.
# surname = input()
# patron = input()
# print(surname[0] + name[0] + patron[0], end='')
#
# Наводим порядок: упорядочиваем курсы по продолжительности
#
# courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
# mentors = [
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
# durations = [14, 20, 12, 20]
#
# courses_list = []
# for course, mentor, duration in zip(courses, mentors, durations):
# 	course_dict = {"title":course, "mentors":mentor, "duration":duration}
# 	courses_list.append(course_dict)
#
# # С этого момента начинается выполнение задания 2
# # На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете
#
# # Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
# # Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
# # Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
# durations_dict = {}
#
# # Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
# for id, course in enumerate(courses_list):
# 	key = course['duration'] # Получите значение из ключа duration
# 	# Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id
# 	durations_dict.setdefault(key, [])
# 	durations_dict[key].append(id)
#
# # Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
# # Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам
# durations_dict = dict(sorted(durations_dict.items()))
#
# # Выведите курсы, отсортированные по длительности
# # Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения
# for duration, ids in durations_dict.items():
# 	# Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»
#     for id in  ids:
#        print(f'{courses_list[id]["title"]} - {duration} месяцев')
#
# courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
# mentors = [
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
# durations = [14, 20, 12, 20]
#
# courses_list = []
# for course, mentor, duration in zip(courses, mentors, durations):
# 	course_dict = {"title":course, "mentors":mentor, "duration":duration}
# 	courses_list.append(course_dict)
#
#
# # С этого момента начинается выполнение задания 3.
# # На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете
#
# # Подсказка: если связь между продолжительностью курсов и количеством преподавателей есть,
# # то после сортировки курсов по длительности и по количеству преподавателей курсы должны идти в одном и том же порядке
# # Проверьте себя: в этом задании курсы будут идти в таком порядке:
# # ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"] - по продолжительности,
# # ["Python-разработчик с нуля", "Frontend-разработчик с нуля", "Fullstack-разработчик на Python", "Java-разработчик с нуля"] - по количеству преподавателей
# # То есть ваш скрипт должен вывести "Связи нет", т.к. порядок оказался разным
#
# # Подсказка 1: для сравнения используйте не названия курсов, а их порядковые номера в списке courses_list
# # Подсказка 2: для сравнения сделайте пары [duration, index] и [mentors_count, index]
# # Допишите код ниже, который добавляет эти пары в список duration_index и mcount_index соответственно:
# duration_index = []
# mcount_index = []
# for index, course in enumerate(courses_list):
# 	duration_index.append([course['duration'], index])
# 	mcount_index.append([len(course['mentors']), index]) # Напишите код по аналогии с duration_index
#
# # Отсортируйте список duration_index и список mcount_index
# # Подсказка: функция sort() будет сортировать по первому элементу (то есть по duration и по количеству преподавателей),
# # поэтому вы сразу получите правильный результат
# # Самостоятельно напишите код сортировки ниже:
# duration_index.sort()
# mcount_index.sort()
#
# # Теперь вам необходимо отделить отсортированные индексы. Перенесите их в отдельные списки:
# # indexes_d (индексы для сортировки курсов по длительности) и
# # indexes_m (индексы для сортировки курсов по количеству преподавателей)
# indexes_d = []
# indexes_m = []
#
# # Допишите код ниже:
# for id1 in duration_index:
# 	indexes_d.append(id1[1])
# # Для indexes_m напишите аналогичный код самостоятельно:
# for id2 in mcount_index:
#     indexes_m.append(id2[1])
#
# # Сравните два получившихся списка индексов. Если они равны, то есть индексы идут в одинаковом порядке,
# # выведите "Связь есть", если не равны - выведите "Связи нет" и ниже - номера курсов по длительности, а потом - по количеству преподавателей
# # Допишите код ниже:
# print("Связь есть" if indexes_d == indexes_m else "Связи нет")
# print(f"Порядок курсов по длительности: {indexes_d}")
# print(f"Порядок курсов по количеству преподавателей: {indexes_m}")
#
# st = input()
# for ind in range(len(st)): #  Напишите программу, которая выводит сообщение «Цифра»
# 	if st[ind] in '0123456789':
# 		print('Цифра')
# 		break
# else:
# 	print('Цифр нет')

# counter = 0 # Напишите программу, которая определяет сколько раз в строке встречаются символы
# couter2 = 0
# st = input()
# for el in st:
# 	if el == '+':
# 		counter += 1
# 	elif el == '*':
# 		couter2 += 1
# print(f'Символ + встречается {counter} раз', f'Символ * встречается {couter2} раз', sep='\n')

# counter = 0 # , которая определяет сколько в ней одинаковых соседних символов.
# st = input()
# for ind in range(len(st) - 1):
# 	if st[ind] == st[ind + 1]:
# 		counter += 1
# print(counter)

# counter = 0
# counter2 = 0 # Напишите программу, которая определяет количество гласных и согласных букв.
# st = input().lower()
# glasn = 'ауоыиэяюёе'
# soglas = 'бвгджзйклмнпрстфхцчшщ'
# for ind in range(len(st)):
# 	if st[ind] in glasn:
# 		counter += 1
# 	elif st[ind] in soglas:
# 		counter2 += 1
# print(f'Количество гласных букв равно {counter}', f'Количество согласных букв равно {counter2}', sep='\n')

# s = input()  # Палиндром
# if s[:] == s [::-1]:
#   print('YES')
# else:
#   print('NO')

# counter = 0
# st = input()
# for ind in range(len(st)):
#   counter += 1
# print(counter)
# print(st * 3)
# print(st[0])
# print(st[:3])
# print(st[-3:])
# print(st[::-1])
# print(st[1:-1])

# sur_name = input()  #  вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае
# sur_name2 = sur_name.title()
# if sur_name == sur_name2:
# 	print('YES')
# else:
# 	print('NO')

# swep_case = input() # строчные символы заглавными и наоборот.
# print(swep_case.swapcase())

# st = input().lower() #  если содержит подстроку «хорош» во всевозможных регистрах.
# if 'хорош' in st:
# 	print('YES')
# else:
# 	print('NO')

# print(input().count(' ') + 1) # подсчитывает количество слов в ней.

# st = input().lower()
# s1 = st.count('а')
# s2 = st.count('г')
# s3 = st.count('ц')
# s4 = st.count('т')
# print(f'Аденин: {s1}', f'Гуанин: {s2}', f'Цитозин: {s3}', f'Тимин: {s4}', sep='\n')

# # Это вы мне? Подсчитываем тёзок на каждом курсе
#
# courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
# mentors = [
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
# durations = [14, 20, 12, 20]
#
# courses_list = []
# for course, mentor, duration in zip(courses, mentors, durations):
# 	course_dict = {"title":course, "mentors":mentor, "duration":duration}
# 	courses_list.append(course_dict)
#
# # С этого момента начинается выполнение задания 4.
# # На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете
#
# # На каждом курсе в отдельности вам необходимо: 1) найти имена, которые встречаются более 1 раза;
# # 2) отобрать людей (Имя + Фамилия), для которых совпало Имя. Это и будут наши тёзки
# names = []
# for course in courses_list:
# 	# Самостоятельно напишите код, который создаёт множество уникальных имён без фамилий
# 	# Подсказка: вам нужно вспомнить и повторить код из задания 1 по множествам
# 	# Результат (уникальные имена без фамилий) запишите в переменную под названием unique_names, преобразуйте в список и отсортируйте по возрастанию
# 	# Это необходимо, чтобы ваша программа всегда давала один и тот же результат и тренажёр смог его сверить
# 	for name in course['mentors']:
# 		names.append(name.split()[0])
# 	unique_names = sorted(list(set(names)))
# 	same_name_list = []
#
# 	for uname in unique_names:
# 		count = 0
# 		for gname in course['mentors']:
# 			if uname in gname:
# 				count += 1
# 				if count > 1 and uname not in same_name_list:
# 					same_name_list.append(uname)
# 	same_name_list_res = []
# 	for i in same_name_list:
# 		for j in course['mentors']:
# 			if i in j:
# 				same_name_list_res.append(j)
# 	same_name_list_res = sorted(same_name_list_res)
# 	if same_name_list_res != []:
# 		title = course['title']
# 		res = ', '.join(same_name_list_res)
# 		print(f'На курсе {title} есть тёзки: {res}')
#
# 	# Напишите алгоритм, который подсчитывает частоту встречаемости каждого имени из names_set в исходном списке преподавателей
# 	# Подсказка: при работе со строками воспользуйтесь конструкцией in
# 	# Внимание: в список same_name_list вы будете сохранять найденных тёзок-преподавателей
# 	#same_name_list = []
# 	# Организуйте цикл по всем именам на курсе из множества:
# 	#for ...:
# 		# Подсчитайте частоту встречаемости имени (должно быть более 1 раза):
# 		#if ...:
# 			# Сделайте цикл по исходному списку преподавателей (с Именем и Фамилией)
# 			#for ...:
# 				# Найдите тех преподавателей, у кого совпало имя (для них if вернёт True)
# 				#if ... in ...:
# 					# Добавьте преподавателя с этим именем в список тёзок
# 					#same_name_list.append(...)
# 	# Если список тёзок не пустой, выведите всех преподавателей из него
# 	#if ...:
# 		# Дополните конструкцию ниже, чтобы выводилось сообщение такого вида: На курсе Название есть тёзки: тёзки через запятую
# 		# Подсказка: для соединения преподавателей через запятую используйте string.join()
# 		#print(f'На курсе {...} есть тёзки: {...}')

# counter = 0
# n = int(input()) # Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
# for i in range(n):
# 	n1 = input()
# 	n2 = n1.count('11')
# 	if n2 >= 3:
# 	    counter += 1
# print(counter)

# counter = 0  # Программа должна вывести количество цифр в данной строке
# s = input()
# for digit in range(10):
# 	counter += s.count(str(digit))
#
# print(counter)

# st = input() # удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними
# el = st.find('h')
# end_el = st.rfind('h')
# print(st[:el], st[end_el + 1:], sep='')

# st = input()  # Первое и последнее вхождение
# el = st.find('f')
# el_end = st.rfind('f')
# if st.count('f') == 1:
# 	print(el)
# elif st.count('f') > 1:
# 	print(el, el_end)
# else:
# 	print('NO')
#
# a = int(input()) # Символы в диапазоне выводит соответствующий ему символ из таблицы символов Unicode
# b = int(input())
# for symbol in range(a, b + 1):
#     print(chr(symbol), end=' ')

# st = input() # Программа должна вывести кодовые значения символов строки
# for code in st:
#     print(ord(code), end=' ')

# num = int(input()) # Список чисел
# print(list(range(1, num + 1)))

# def discriminant(a, b, c):
#     """
#     функция для нахождения дискриминанта
#     """
#     # Ваш алгоритм
#     return b ** 2 - 4 * a * c
#
# def solution(a, b, c):
#     """
#     функция для нахождения корней уравнения
#     """
#     if discriminant(a, b, c) < 0:
#         print('корней нет')
#     elif discriminant(a, b, c) == 0:
#         x = -b / (2 * a)
#         print(x)
#     else:
#         x_1 = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
#         x_2 = (-b - discriminant(a,b,c) ** 0.5) / (2 * a)
#         print(x_1, x_2)
#
#
# if __name__ == '__main__':
#     solution(1, 8, 15)
#     solution(1, -13, 12)
#     solution(-4, 28, -49)
#     solution(1, 1, 1)
#
#
# your code
# times = 0
# def vote(votes):
#     global times # Вывести число, которое встречается чаще всего
#     times +=1
#     count = []
#     for i in votes:
#         count.append(votes.count(i))
#         max_times = max (count)
#         n = count.index(max_times)
#     return (f'{times}')
#
# if __name__ == '__main__':
#     print(vote([1,1,1,2,3]))
#     print(vote([1,2,3,2,2]))

# num = int(input())  # Напишите программу, которая выводит список, состоящий из n букв английского
# sp = []
# for i in range(num):
#   sp.append(chr(ord('a') + i))
# print(sp)

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers) + max(numbers)) # так чтобы он вывел сумму минимального и максимального элементов списка

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens) # чтобы он вывел среднее арифметическое элементов списка
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый' # , чтобы элемент списка имеющий значение Green заменился на значение Зеленый
# rainbow[6] = 'Фиолетовый'
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1]) # чтобы он вывел элементы списка languages в обратном порядке.

# numbers1 = [1, 2, 3]  # [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
#         {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
#       ]
#
# directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006'],
#         '3': []
#       }
#
# def get_name(doc_number):
#     # your code
#     for numbers in documents:
#         if doc_number in numbers['number']:
#             return numbers['name']
#     return 'Документ не найден'
#
#
# def get_directory(doc_number):
#     # your code
#     for key in directories.keys():
#         number_list = directories[key]
#         if doc_number in number_list:
#             return key
#     return 'Полки с таким документом не найдено'
#
#
# def add(document_type, number, name, shelf_number):
#     # your code
#     key = str(shelf_number)
#     directories[key].append(number)
#     documents.append({'type': document_type, 'number': number, 'name': name})
#
# if __name__ == '__main__':
#     print(get_name("10006"))
#     print(get_directory("11-2"))
#     print(get_name("101"))
#     add('international passport', '311 020203', 'Александр Пушкин', 3)
#     print(get_directory("311 020203"))
#     print(get_name("311 020203"))
#     print(get_directory("311 020204"))

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers)) # Вывел длину списка
# print(numbers[-1]) # Вывел последний элемент списка
# print(numbers[::-1])
# print('YES') if 5 in numbers and 17 in numbers else print('NO') # Вывел YES если список содержит числа 5 и 17, и NO в противном случае
# del numbers[0]
# del numbers[-1]
# print(numbers)

# sp = []
# num = int(input()) # которая создает из указанных строк список и выводит его.
# for i in range(num):
#     st = input()
#     sp.append(st)
# print(sp)
#
# sp = []  # Алфавит
# for i in range(1, 27):
#     sp.append(chr(96 + i) * i)
# print(sp)
#
# num = int(input())  # Список кубов
# sp = []
# for i in range(num):
#     dig = int(input())
#     sp.append(dig ** 3)
# print(sp)

# num = int(input())  # которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список
# sp =[]
# for i in range(num):
#     dig = int(input())
#     sp.append(dig)
# del sp[1::2]
# print(sp)

# num = int(input()) # Символы всех строк
# sp = []
# for i in range(num):
#     st = input()
#     sp.extend(st)
# print(sp)

# sp = []  # так чтобы он вывел сумму квадратов элементов списка numbers
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for el in numbers:
#     sp.append(el ** 2)
# print(sum(sp))

# sp = []  # Значение функции каждое на отдельной строке
# num = int(input())
# for i in range(num):
#     num2 = int(input())
#     sp.append(num2 ** 2 + 2 * num2 +1)
#     print(num2)
# print()
# print(*sp, sep='\n')

# sp = []
# num = int(input())  # которая удаляет наименьшее и наибольшее значение из указанных чисел
# for i in range(num):
#     num2 = int(input())
#     sp.append(num2)
# sp.remove(min(sp))
# sp.remove(max(sp))
# print(*sp, sep='\n')

# num = int(input())  # Без дубликатов
# sp = []
# for i in range(num):
#     st = input()
#     if st not in sp:
#         sp.append(st)
# print(*sp, sep='\n')

# num = int(input())
# if num > 0:
#     print('her')
# else:
#     print('push')
#
# num = int(input())
# sp = []
# sp1 = []
# sp2 = []
# for el in range(num):  # отрицательные числа, затем нули, а затем все положительные числа
#     n = int(input())
#     if n < 0:
#         sp.append(n)
#     elif n == 0:
#         sp1.append(n)
#     else:
#         sp2.append(n)
# print(*sp + sp1 + sp2, sep=('\n'))

# text = input().split()  # которая выводит слова введенной строки в столбик.
# print(*text, sep=('\n'))

# sur_name = input().split()  # Инициалы
# name = sur_name[0][0]
# name1 = sur_name[1][0]
# name2 = sur_name[2][0]
# print(name, name1, name2 + '.', sep='.')

# st = input().split('\\')  # которая разбирает строку на части, разделенные символом "\".
# print(*st, sep='\n')

# st_num = input().split()
# for el in range(len(st_num)): # которая по заданным числам строит столбчатую диаграмму.
#     st_num[el] = int(st_num[el])
#     print(st_num[el] * '+')

# st = list(map(int, input().split('.')))  # ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
# if 0 <= st[0] <= 255 and 0 <= st[1] <= 255 and 0 <= st[2] <= 255 and 0 <= st[3] <= 255:
#     print('ДА')
# else:
#     print('НЕТ')

# st = list(input())  # Добавь разделитель
# st1 = input()
# print(st1.join(st))

# numbers = [8, 9, 10, 11]  # Все сразу 2
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

# st = list(map(int, input().split()))  # Переставить min и max
# min_ = st.index(min(st))
# max_ = st.index(max(st))
# st[min_], st[max_] = st[max_], st[min_]
# print(*st)

# st_text = input().lower().split()  # Количество артиклей
# counter = st_text.count('a')
# counter1 = st_text.count('an')
# counter2 = st_text.count('the')
# print(f'Общее количество артиклей: {counter + counter2 + counter1}')
#
# st = list(map(int, input().split()))  # Сортировка чисел
# st1 = st[:]
# st.sort()
# print(*st)
# st1.sort(reverse=True)
# print(*st1)

# chars = [c for c in 'abcdefg']
# print(chars)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#             'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]  # с удаленным первым символом.
#
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(i) for i in keywords]  # длины строк исходного списка.
#
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [el for el in keywords if len(el) >= 5]  # только слова длиной не менее пяти символов (включительно).
#
# print(new_keywords)

# palindromes = [n for n in range(100, 1001) if n % 10 == n // 100]
#
# print(palindromes)  # получить список всех чисел палиндромов от 100 до 1000

# num = int(input())  # список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на отдельной строке.
# sqw = [i ** 2 for i in range(1, num + 1)]
# for i in sqw:
#     print(i)

# num = input().split()  # которая выведет кубы указанных чисел также на одной строке
# realu = [int(i) ** 3 for i in num]
# print(*realu)

# print(*[el for el in input().split()], sep='\n')  #  выводит слова введенной строки в столбик

# text = input()  # цифровые символы данной строки.
# print(*[n for n in text if n.isdigit()], sep='')

# num = input().split()  # которая выведет квадраты четных чисел, которые не оканчиваются на цифру 4.
# print(*[int(i) ** 2 for i in num if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])
#
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97,
#      0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26,
#      63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):  # Оптимизируйте приведенный код, реализующий алгоритм пузырьковой сортировки.
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)

# def draw_box():
#     for _ in range(5):  # прямоугольник
#         print('*' * 7)
#
# draw_box()

# объявление функции
# def draw_box():
#     print('*' * 10)  # Звездный прямоугольник 1
#     for i in range(12):
#         print('*' + ' ' * 8 + '*' )
#     print('*' * 10)
#
# # основная программа
# draw_box()  # вызов функции

# объявление функции
# def draw_triangle():
#     for i in range(10 + 1):
#         print('*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции

# def draw_triangle(fill, base):
#     pass
#
# # считываем данные
# fill = input()
# base = int(input())
# for i in range(base // 2 + 1):
#     for j in range(i + 1):  # Звездный треугольник
#         print(fill, end='')
#     print()
# for i in range(base // 2, 0, -1):
#     for j in range(i):
#         print(fill, end='')
#     print()
# # вызываем функцию
# draw_triangle(fill, base)

# def print_fio(name, surname, patronymic):
#     sp = []
#     sp.append(surname[0].upper())  # Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
#     sp.append(name[0].upper())
#     sp.append(patronymic[0].upper())
#     print(*sp, sep='')
#
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# def print_digit_sum(num):
#     total = 0
#     while num > 0:  #  и выводит на печать сумму его цифр.
#         dig = num % 10
#         total += dig
#         num //= 10
#     print(total)
# # считываем данные
# n = int(input())
# # вызываем функцию
# print_digit_sum(n)


# def convert_to_miles(km):
#     miles = km * 0.6214
#     return miles  # которая принимает в качестве аргумента расстояние в километрах и возвращает в милях
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))


# def get_days(month):  # принимает в качестве аргумента номер месяца и возвращает количество дней
#     dni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return dni[month]
#
# # считываем данные
# num = int(input())
# # вызываем функцию
# print(get_days(num))

# class Book:
#     name = '1984'
#     writer ='Джордж Оруэлл'  #  вывести на разных строках сначала атрибут класса writer, а затем атрибут name
#     pages= 213
#
# print(Book.writer)
# print(Book.name)

# class Config:  # Ваша задача написать только определение функции create_instance , и не забывайте, что она должна вернуть ЭК.
#     pass
#
# def create_instance(n: int) -> Config:
#     obj = Config()
#     for i in range(1, n + 1):
#         setattr(obj, 'attribute' + str(i), 'value' + str(i))
#     return obj
#
#
# # Ниже расположены проверки для функции create_instance
#
# config_2 = create_instance(2)
# assert isinstance(config_2, Config)
# assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}
#
# config_4 = create_instance(4)
# assert isinstance(config_4, Config)
# assert config_4.__dict__ == {'attribute1': 'value1',
#                              'attribute2': 'value2',
#                              'attribute3': 'value3',
#                              'attribute4': 'value4'}
#
# config_7 = create_instance(7)
# assert isinstance(config_7, Config)
# assert config_7.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
#                              'attribute3': 'value3', 'attribute4': 'value4',
#                              'attribute5': 'value5',
#                              'attribute6': 'value6',
#                              'attribute7': 'value7'}
#
# config_10 = create_instance(10)
# assert isinstance(config_10, Config)
# assert config_10.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2',
#                               'attribute3': 'value3', 'attribute4': 'value4',
#                               'attribute5': 'value5', 'attribute6': 'value6',
#                               'attribute7': 'value7', 'attribute8': 'value8',
#                               'attribute9': 'value9', 'attribute10': 'value10'}
#
# print('good')
#
# class Lion:  # Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
#     def roar(self):
#         print('Rrrrrrr!!!')
#
# simba = Lion()
# simba.roar()

# class Robot:
#     def say_hello(self):  # Метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
#         print('Hello, human! My name is C-3PO')
#
#     def sey_bye(self):  # Метод say_bye ,  печатающий на экран фразу «See u later alligator»
#         print('See u later alligator')
#
#
# c3po = Robot()
# r2d2 = Robot()
#
# c3po.say_hello()
# c3po.sey_bye()
# r2d2.say_hello()
# r2d2.sey_bye()

# class Robot:
#     def set_name(self, name):  # Метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name
#         self.name = name
#
#     def say_hello(self):  # Метод должен проверить, есть ли у ЭК атрибут name
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print('У робота нет имени')
#
#     def say_bye(self):
#         print('See u later alligator')
#
#
# c3po = Robot()
# c3po.say_hello()
# c3po.set_name('R2D2')
# c3po.say_hello()
# c3po.say_bye()
#
# r = Robot()
# r.set_name('Chappy')
# r.say_hello()
#
# d = Robot()
# d.say_hello()
# d.set_name('Wally')
# d.say_hello()

# class Counter:
#     def start_from(self, value=0):  # который принимает один необязательный аргумент умолчанию равно 0.
#         self.value = value
#
#     def increment(self):  # который увеличивает счетчик на
#         self.value += 1
#
#     def display(self):  #  который печатает фразу "Текущее значение счетчика = <value>
#         print(f'Текущее значение счетчика = {self.value}')
#
#     def reset(self):  # который обнуляет накопившееся значение счетчика.
#         self.value = 0
#
#
# # Ниже код для проверки класса Counter
#
# c1 = Counter()
# c2 = Counter()
#
# assert isinstance(c1, Counter)
# assert isinstance(c2, Counter)
# assert c1.__dict__ == {}
# assert c2.__dict__ == {}
#
# c1.start_from(45)
# assert len(c1.__dict__) == 1
# c1.increment()
# c1.display()  # печатает 46
# c1.increment()
# c1.display()  # печатает 47
#
# c2.start_from()
# c2.display()  # печатает 0
# c2.increment()
# c2.display()  # печатает 1
#
# c1.reset()  # обнулили с1, но с2 не должен меняться
# c1.display()  # печатает 0
#
# c2.display()  # попрежнему печатает 1
