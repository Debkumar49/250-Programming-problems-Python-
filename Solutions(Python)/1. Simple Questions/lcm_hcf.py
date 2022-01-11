n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
min = n1 if n1<n2 else n2
for i in range (1,min+1):
    if n1%i == 0 and n2%i == 0:
        hcf = i

lcm = (n1*n2)//hcf
print(f"The LCM of {n1} and {n2} is : {lcm}")
print(f"The HCF of {n1} and {n2} is : {hcf}")
