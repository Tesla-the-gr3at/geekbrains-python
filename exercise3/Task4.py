def my_func(a,b):
    if (not a >=0) or (not b <=0):
        print("First number must be more than 0, scond number must be less than 0")
        exit(0)
    elif (type(a) != int) or (type(b) != int):
        print("Wrong number type, must be integer")
        exit(0)

    b_module = b * -1

    for i in range(1,b_module+1):
        pass # broken
print(my_func(5,-2))
    