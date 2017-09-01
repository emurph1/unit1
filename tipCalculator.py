#Emily Murphy
#2017-08-31
#tipCalculator.py - finding out tip

meal = float((input('How much was the meal?')))
print(meal)
percent = float(input('What percent tip?'))
tip = (percent/100)
print(tip)
total = float(tip * meal)
print(total)
print('You should tip', round(total, 2))

