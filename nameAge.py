#Emily Murphy
#2017-08-31
#nameAge.py - user asks questions

name = input('What is your first and last name?')
print(name)
name1, name2 = name.split()
age = int(input('How old are you?'))
print(age)
print('Your first name has',len(name1),'letters')
print('Your last name has', len(name2),'letters')
print('Next year you will be', age+1, 'years old')
