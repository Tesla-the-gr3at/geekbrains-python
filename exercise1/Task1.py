# Поработайте с переменными, создайте несколько, выведите на экран
variable1 = "1"
variable2 = 1
variable3 = input("Please enter a word:")
variable4 = int(variable1) + variable2

print(variable1)
print(variable2)
print(variable3)
print(f"variable1 + variable2 = {variable4}")


# запросите у пользователя несколько чисел сохраните в переменные, выведите на экран
# Prompt for 3 numbers and add them to a single variable
for i in range(3):
    temp_variable = int(input("Please enter a number:"))
    print(f"you entered: {temp_variable}")


# запросите у пользователя несколько строк сохраните в переменные, выведите на экран
for i in range(3):
    temp_variable = int(input("Please enter a string:"))
    print(f"you entered: {temp_variable}")



