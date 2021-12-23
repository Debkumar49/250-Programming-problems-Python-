try:
    character = input('Enter the character to see ASCII value : ')
    print('The ASCII value of the character is : ',ord(character))
except Exception as e:
    print(e)

