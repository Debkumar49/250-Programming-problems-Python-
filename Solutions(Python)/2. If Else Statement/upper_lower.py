def upper():
    ch = input("Enter something to check the property of the input : ")
    if ord(ch)>=65 and ord(ch)<=90:
        print("Uppercase Alphabet")
    elif ord(ch)>=97 and ord(ch)<=122:
        print("Lowercase Alphabet")
    elif ord(ch)>=48 and ord(ch)<=57:
        print("Number ")
    else:
        print("Symbol")

upper()