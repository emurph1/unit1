#Emily Murphy
#2017-08-31
#nameAge.py - user asks questions

name = input('What is your first and last name?')
print(name)
name1, name2 = name.split()
age = int(input('How old are you?'))
print(age)
print(len(name1))
print(len(name2))
print('Next year you will be', age+1, 'years old')
