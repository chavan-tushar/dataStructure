from ast import Lambda


createdObj = []
def try_enum(obj):
    for index, value in enumerate(obj):
        print(f"At position {index} value is {value}")

def user_input():
    global createdObj
    while True:
        userInput = input("Please enter student name: ")
        if userInput in ['x','X']:
            break
        createdObj.append(userInput)

def list_comprehension():
    normalList = [num for num in range(10)]
    listWithCalc = [num ** 2 for num in range(10)]
    listWithIf = [num for num in range(1,11) if num % 2 == 0]
    listWithIfElse = [ num if num % 2 == 0 else "ODD" for num in range(1,11)]
    listWithNestedFor = [num*num1 for num in [2,3,4] for num1 in [10,100,1000]]
    print(normalList)
    print(listWithCalc)
    print(listWithIf)
    print(listWithIfElse)
    print(listWithNestedFor)


# Map
def square(num):
    return num ** 2

def use_map(obj):
    lst = list(map(square, obj))
    print(lst)

# Reduce
def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, [1,2,3,4,5,6,7,8,9,10]))

# Lambda
myList = list(filter(lambda num:num%2 == 0, [101,200,301,4021,500,61]))
print(myList)

if __name__ == "__main__":
    # user_input()
    # try_enum(createdObj)
    # list_comprehension()
    use_map([1,2,3,4,5])