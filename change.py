#Emily Murphy
#2017-09-06
#change.py - talking about money

cents = int(input('Enter number of cents: '))
quarters = (cents//25)
dimes = ((cents - (25 * quarters))//10)
nickels = ((cents - ((10 * dimes) + (25 * quarters)))//5)
pennies = ((cents - ((5 * nickels) + (10 * dimes) + (25 * quarters)))//1)
print(('Quarters:'), quarters)
print(('Dimes:'), dimes)
print(('Nickels:'), nickels)
print(('Pennies:'), pennies)
