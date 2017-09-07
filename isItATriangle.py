#Emily Murphy
#2017-09-06
#isItATriangle.py - input three lengths and determine if they can make a triangle

sideA = float(input('Enter side A: '))
sideB = float(input('Enter side B: '))
sideC = float(input('Enter side C: '))
float(max(sideA,sideB, sideC))
float(min(sideA,sideB, sideC))
middle = float((max(sideA,sideB, sideC)- min(sideA,sideB, sideC)))
print((float(min(sideA,sideB, sideC)) + middle)>float(max(sideA,sideB, sideC)))
