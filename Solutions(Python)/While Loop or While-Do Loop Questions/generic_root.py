from ast import Break


n=int(input("Enter the number to find Genereic root : "))
temp=n
while n>=10:
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    if sum>=10:
        n=sum
    else:
        Break

print(f"Genreic root of {temp} is {sum}")