def countCurrency(amount):
     
    notes = [2000, 500, 200, 100,
               50, 20, 10, 5, 2,1]
                
    noteCounter = [0, 0, 0, 0, 0,
                     0, 0, 0, 0,0]
     
    print ("Currency Count -> ")
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i ," : ", j)
 
# Driver code
amount = int(input("Enter the Amount : "))
countCurrency(amount)