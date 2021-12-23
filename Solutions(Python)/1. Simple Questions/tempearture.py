result = 0
def farenheit_celcius():
    farenheit = float(input('Enter the value in Farenheit : '))
    result = ((5*farenheit-160)/9)
    print(f'The value of Farenheit {farenheit} will be ',result,' in celcius ')

def celcius_farenheit():
    celcius = float(input('Enter the value in celcius : '))
    result =((9*celcius/5)+32)
    print(f'The value of celcius {celcius} will be ',result,' in Farenheit ')


print('''
        1.Convert Farenheit to celcius.
        2. Convert Celcius to Farenheit.

''')

choice = int(input('Enter your choices : '))
operations = [farenheit_celcius,celcius_farenheit]

operations[choice -1]()


