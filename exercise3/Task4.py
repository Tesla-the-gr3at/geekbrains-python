def my_func(a,b):

    # Do not use built-in function:
    if (not a >=0) or (not b <=0):
        print("First number must be more than 0, scond number must be less than 0")
        exit(0)
    elif (type(a) != int) or (type(b) != int):
        print("Wrong number type, must be integer")
        exit(0)

    b_module = b * -1
    result = a

    for i in range(1,b_module):
        result = result * a
    
    result = 1 / result
    

    #use built-in function
    result2 = 1 / (a**b_module)
    
    return result, result2
print(my_func(4,-4))
    