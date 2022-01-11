import datetime
inputdate = input("Enter the date is dd/mm/yyyy format : ")
day,month,year = inputdate.split('/')

IsValidDate = True
try:
    datetime.datetime(int(year),int(month),int(day))
except ValueError:
    IsValidDate = False

if(IsValidDate):
    print("The date Entered is valid")
else:
    print("The date you entered is invalid")