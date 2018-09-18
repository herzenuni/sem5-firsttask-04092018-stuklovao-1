class RangeException(Exception):
 pass

try:
    number = int(input('Введите число от 0 до 9: '))
    if ((number<0) | (number>9)):
      raise RangeException('Введенное число не входит в указанный интервал')    
except RangeException:
    print('Введенное число не подходит, попробуйте ввести число еще раз')
    number = int(input('Введите число от 0 до 9: '))


t=str(input('Введите систему счисления - ')) 
def print_number_and_word(number, t=''): 

    if (number == 0):
      print("\n Ноль")
    elif (number == 1):
      print("\n Один")
    elif (number == 2):
      print("\n Два")
    elif (number == 3):
      print("\n Три")
    elif (number == 4):
      print("\n Четыре")
    elif (number == 5):
      print("\n Пять")
    elif (number == 6):
      print("\n Шесть")
    elif (number == 7):
      print("\n Семь")
    elif (number == 8):
      print("\n Восемь")
    elif (number == 9):
      print("\n Девять")
    else:
      print("Начните сначала")


    if t == 'bin':
      print(bin(number))
    elif t == 'oct':
      print(oct(number))
    elif t == 'hex':
      print(hex(number))

print_number_and_word(number,t) 
