#Emily Murphy
#2017-08-31
#tipCalculator.py - finding out tip

meal = (input('How much was the meal?'))
print(meal)
percent = int(input('What percent tip?'))
tip = (percent/100)
print(tip)
print('You should tip', (tip * meal))

