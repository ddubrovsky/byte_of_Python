age = 26
name = 'Swaroop'

print('Age {0} -- {1} year'.format(name, age))
print('Why {0} has a fun with the Python?'.format(name))

# digits are not necesary
print('Age {} -- {} year'.format(name, age))
print('Why {} have a fun with the Python?'.format(name))

print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
print('{name} was {age} years old when wrote this book'.format(name=name, age=age))
print(f'{name} was {age} years old when wrote this book') # notice the 'f' before the string

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
print('{0:.3f}'.format(1.0/3))
# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))
# по ключевым словам

# you can cpecify that it should end with a blank:
print('a', end='')
print('b', end='') # next print start from this string

# or you can end with a space:
print('a', end=' ')
print('b', end=' ')
print('c')

print('What\'s your name?') # notice the backslash (called an escape sequence)