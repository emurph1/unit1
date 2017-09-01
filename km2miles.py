#Emily Murphy  
#2017-08-31
#km2miles.py - converting km to miles

km = int(input('How many kilometers? '))
conv_fac = 0.621371
miles = round((km * conv_fac), 3)

print(km, 'kilometers is', miles, 'miles')

