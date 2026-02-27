print('number\tSquare\tCube')
print('-------------------------')
maxNumber = int(input('What is the maximum number '))
maxNumber+=1
for number in range (1,maxNumber):
    square = number**2
    cube = number**3
    print(number, '\t', square, '\t' ,cube)
    
