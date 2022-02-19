num = int(input("Enter the Number to check whheather the number is amstrong or not : "))
temp=num
result=0
count=len(str(num))
while temp!=0:
    reaminder = temp%10
    result = result+reaminder**count
    temp = temp//10
if result==num:
    print(f"{num} is an Amstrong Number.")
else:
    print(f"{num} is not an Amstrong Number.")