# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
user_input = int(input("Please enter a number:"))
largest_number = 0

while user_input > 0:
    current_figure = user_input % 10
    if current_figure > largest_number:
        largest_number = current_figure
    user_input = user_input // 10
    continue

print(largest_number)