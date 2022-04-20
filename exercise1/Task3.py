#  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
user_input = input("Please enter a number:")
increment = 1
result = 0

while increment <= int(user_input):  #
    result += int(user_input * increment)  # multiply number by increment convert to int and add to the result
    increment += 1  # increase increment by 1

print(result)
