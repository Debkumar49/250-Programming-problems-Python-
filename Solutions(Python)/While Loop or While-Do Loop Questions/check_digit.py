n=int(input("enter the number "))
temp=n
count=0
while n!=0:
    count+=1
    n=n//10
print(f"Entered number {temp} has {count} digits")