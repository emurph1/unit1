#Emily Murphy
#2017-09-06
#binary.py - enter 8 digit binary number and converts it into base of 10

num = int(input('Enter 8-digit binary number: '))
num1 = (num % 10)
final1 = (num // 10)
num2 = (final1 % 10)
final2 = (final1 // 10)
num3 = (final2 % 10)
final3 = (final2 // 10)
num4 = (final3 % 10)
final4 = (final3 // 10)
num5 = (final4 % 10)
final5 = (final4 // 10)
num6 = (final5 % 10)
final6 = (final5 // 10)
num7 = (final6 % 10)
final7 = (final6 // 10)
num8 = (final7 % 10)
final8 = (final7 // 10)
print((num1*1) + (num2*(2**1)) + (num3*(2**2)) + (num4*(2**3)) + (num5*(2**4)) + (num6*(2**5)) + (num7*(2**6)) + (num8*(2**7)))