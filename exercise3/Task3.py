def my_func(a,b,c):
    order = [a,b,c]
    order.sort(reverse=True)
    return(order[0]+order[1])


print(my_func(
                int(input("Enter first number : ")),
                int(input("Enter second number : ")),
                int(input("Enter third number : ")),
                ))
