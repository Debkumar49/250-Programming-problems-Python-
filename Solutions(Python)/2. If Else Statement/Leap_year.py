def Leap_year():

    print("This program is to find out the year is odd or even ")
    year = int(input("Enter the year : "))

    if year%400==0 and year%4==0 or year%100!=0:
        print(f"{year} year is a Leap Year.")
    else:
        print(f"{year} year is not a Leap year.")


Leap_year()