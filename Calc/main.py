from calculator import *
print("Добро пожаловать в программу 'Калькулятор'")
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
while True:
    user_choice = input("Выберите знаком (+, -, *, /) арифметическое действие, которое желаете совершить: ")
    if user_choice == "+":
        result = summarize(number_1, number_2)
        print(f"Результат вашей арифметической операции - {result}")
        break
    elif user_choice == "-":
        result = subtract(number_1, number_2)
        print(f"Результат вашей арифметической операции - {result}")
        break
    elif user_choice == "*":
        result = product(number_1, number_2)
        print(f"Результат вашей арифметической операции - {result}")
        break
    elif user_choice == "/":
        result = divide(number_1, number_2)
        if result is not None:
            print(f"Результат вашей арифметической операции - {result}")
            break
        else:
            print("Ваш результат равен нулю, поскольку вы пытались поделить на ноль")
            break
    else:
        print("Введены некорректные данные. Попробуйте еще раз")


print("Спасибо за использование нашей программы")
