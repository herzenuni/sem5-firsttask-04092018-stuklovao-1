class RangeException(Exception):
  def __init__(self,text):
        RangeException.txt = text

numbers = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
types = ['bin', 'oct', 'hex']

a =  input("Введите один из типов hex, oct, bin:")


def func(x, num_type):
  if num_type in types and num_type != "" and x in range(0,10):
    if (num_type == 'hex'):
      return hex(x)
    elif (num_type == 'oct'):
      return oct(x)
    elif (num_type == 'bin'):
      return bin(x)

  if x in range(0,10):
    return numbers[x] 
  else:
    return "Неверное значение"


try:
  num =  int(input("Введите число от 0 до 9:"))
  if ((num<0) | (num>9)):
      raise RangeException('Введено неверное значение числа') 
  else:
      print(func(num, a)) 
      with open('Record.txt', 'a') as f:
        f.write('Numbers:'"\n" + str(num) + 'Type:' + str(a)+"\n") 
except RangeException:
  print(RangeException.txt)
except ValueError:
  print("Введено неверное значение числа")

def test():
  assert func(9, 'oct') == '0o11'
  assert func('qw', 'oct') == 'Неверное значение'
  assert func(5, 'qwer') == 'пять'

test()
 
