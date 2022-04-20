# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то 
# новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

rating = [8, 6, 5, 3, 3, 1]
index = 0
user_number = int(input("Please enter a number:"))

while index < len(rating):                             
    if rating[index] < user_number :
        rating.insert(index,user_number)
        break
    elif (index == len(rating)-1) or ((rating[index] == user_number) and (rating[index+1] < user_number)):
        rating.insert(index+1,user_number)
        break
    else:
        index+=1
        continue
    
print(rating)
