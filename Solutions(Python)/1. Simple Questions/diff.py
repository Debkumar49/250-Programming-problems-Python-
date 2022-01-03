import sys

def int_1():
    x=0
    print("The size of the Integer Data type : ",sys.getsizeof(x))
    print("An example of integer DataType : ",x)

def float_1():
    x=0.0
    print("The size of the float datatype",sys.getsizeof(x))
    print("An example of Float DataType : ",x)


def complex_1():
    x=9+5j
    print("The size of the complex datatype : ",sys.getsizeof(x))
    print("An example of Complex DataType : ",x)


def boolean_1():
    x = True
    print("The size of Boolean dataType : ",sys.getsizeof(x))
    print("An example of Boolean DataType : ",x)

def list_1():
    x=[1,2,3,4]
    print("Lists are mutable")
    print("The size of list datatype : ",sys.getsizeof(x))
    print("An example of List DataType : ",x)

def tupple_1():
    x = (1,4,5,6)
    print("Tupples are immutable")
    print("The size of tupple data type : ",sys.getsizeof(x))
    print("An example of Tupple DataType : ",x)

def set_1():
    x = {1,2,4,5}
    print("Set is mutable but contains no duplicate")
    print("The size of set Datatype : ",sys.getsizeof(x))
    print("An example of Set DataType : ",x)

def string_1():
    x ='Github'
    print("The size of the string Datatype : ",sys.getsizeof(x))
    print("An example of String DataType : ",x)

def range_1():
    x = range(0,10)
    print("The size of the range Datatype : ",sys.getsizeof(x))
    print("An example of Range DataType : ",x)




print(
    '''
    Enter the Number in range and Find out the size of the Datatype : 
    1. Integer.
    2. Float.
    3. complex.
    4. Boolean.
    5. List.
    6. Tupple.
    7. Set.
    8. String.
    9. Range.
    '''
)
choice = int(input('Please enter your Choice : '))
operations = [int_1,float_1,complex_1,boolean_1,list_1,tupple_1,set_1,string_1,range_1]
operations[choice-1]()


