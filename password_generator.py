import random

lower = 'abcdefghijklmnopqrstuvxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
symbol = '[]{}()#*;._-'
number = '0123456789'

length = 18

all = lower + symbol + upper + number
password = ''.join(random.sample(all,length))

print(password)

