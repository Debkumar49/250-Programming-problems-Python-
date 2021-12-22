pi = 3.14
radius = int(input('Enter the radius of the circle : '))
area = pi*radius*radius
circumference = 2*pi*radius
print('Enter 1 to calculate Area \nEnter 2 to calculate circumference \nEnter 0 to exit ')

def selector(choice):
    switcher={
        1:area,
        2:circumference,
        0:exit(),
    }
    return switcher.get(choice,'Please enter valid input')

choice = int(input('Enter your choice '))
res = selector(choice)
print(res)