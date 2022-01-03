import sys 
sys.setrecursionlimit(200)
def find_fact(n):
  if n == 0 or n == 1:
    return 1
  else :
    return (n*find_fact(n-1))  

n1 = int(input("Enter the number to find the factorial : ")) 
print("Factorial is :", find_fact(n1))