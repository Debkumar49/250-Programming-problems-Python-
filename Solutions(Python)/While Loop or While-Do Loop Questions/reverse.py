n = int(input("Enter the Number to reverse : "))
temp = n
rev = 0
while n!=0:
    remainder = n%10
    rev = rev*10 + remainder
    n = n//10
print(f"Reverse of {temp} is  {rev}")