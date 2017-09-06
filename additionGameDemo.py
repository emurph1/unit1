#Emily Murphy
#2017-09-06
#additionGameDemo.py -

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)
answer = int(input(str(num1)+ '+' + str(num2)+ ':'))
print(answer == num1 + num2)