# ДЗ:
# 1. Создать функцию, которая выводит на экран цифру, введенную пользоватлем в консоли.
value = input("Введите число: ")
печать(значение)

# 2. Написать программу, которая считает 5 значений, введенных пользователем из консоли, сохранит их в список
# затем передаст значения в фукцию, которая выводит на экран сумму значений списка.

def num_sum(массив):
    итого = 0

    для i в массиве:
        итого += i

    печать(всего)

list_num = []
для i в диапазоне(5):
    inputs = int(input(' '))
    list_num.добавить(входы)
    print(list_num)


num_sum(list_num)

# 3. Написать программу, которая:
# - выводит следующее меню на экран
# 1. Ввести значения а и b
# 2. Умножить значения а и b
# 3. Делить а на b
# 4. Выход
# - реализует кажду опцию как фукцию
# - реализует все ошибки и исключения.

def user_input():
    A = int(input('a: '))
    B = int(input('b: '))

    возврат A, B


 умножение def(A, B):
    возврат A * B


def divided(A, B):
    возврат A / B


def quit_pr():
    return True


а = 0
b = 0

пока это правда:

    print('1. Ввести значения а и b')
    print('2. а * b')
    печать('3. а / b')
    печать('4. Выход')

    попробуй:
        user_choice = int(input(' '))

        если user_choice != 4:
            if user_choice == 1:
                a, b = user_input()
                print('a: {0}, b: {1}'.формат(a, b))
            elif user_choice == 2:
                m = умножение(a, b)
                print('a * b =', m)
            elif user_choice = = 3:
                m = делится(a, b)
                print('a / b =', m)
            остальное:
                print('Ошибка.')
        остальное:
            q = quit_pr()
            если q  истинно:
                print('Выход из программы...')
                перерыв
    за исключением:
        print('Ошибка.')