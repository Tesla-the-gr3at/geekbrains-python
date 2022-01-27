# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.

a = input("First day result in kilometers:")
b = input("Desired result:")
day_count = 1

# Check if user input is number
try:
    a = float(a)
    b = float(b)
except ValueError:
    print(f"Please enter two numbers.")
    exit()

while a < b:
    a = a + a / 10
    day_count += 1
    continue

print(f"{b}km will be achieved on {day_count} day")
