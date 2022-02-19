n=int(input("Enter the number upto which you want to show the fibinacci series : "))
first = 0
second=1
next=0
print(first,second)
for i in range(2,n):
    next=first+second
    print(next)
    first=second
    second=next


