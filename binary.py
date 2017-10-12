#Emily Murphy
#2017-09-06
#binary.py - enter 8 digit binary number and converts it into base of 10

num = int(input('Enter 8-digit binary number: '))
digit1 = bin%10
digit2 = (num//10)%10
digit3 = (num//100)%10
digit4 = (num//1000)%10
digit5 = (num//10000)%10
digit6 = (num//100000)%10
digit7 = (num//1000000)%10
digit8 = (num//10000000)%10
print(digit1 + digit2*(2**1) + digit3*(2**2) + digit4*(2**3) + digit5*(2**4) + digit6*(2**5) +
digit7*(2**6) + digit8*(2**7))
