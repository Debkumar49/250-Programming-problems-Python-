fact  = 1
n = int(input("Enter the value of n : "))
if n==0:
    print("The factorial of ",n,"is : 1 ")
else:
    for i in range(1,n+1):
        fact =  fact*i
    print(fact)