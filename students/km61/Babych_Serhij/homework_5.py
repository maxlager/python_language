# task1-------------------------------------------------------------
"""
Умова: Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""
# Програма для обчислення відстані між 2 точками за їх кординатами
# використаєм відому формулу ((x2- x1)^2 + (y2 - y1)^2)^(1/2)
def distance(x1,y1,x2,y2): # створюємо функцію
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2) # блок дії функції

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1,y1,x2,y2)) # визов функції для введених значень


#-----------------------------------------------------------------


# task2------------------------------------------------------------
"""
Умова: Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
"""
# Програма піднесення дійсного додатнього числа (a) до цілої степені (n)
def power(a, n): # створюємо функцію
    pow = 1
    for i in range(abs(n)): # створюємо цикл для пднесення до степені
        pow = pow * a
    if n >= 0:            # оскільки стпінь може бути відємно то потрібно накласти умову
        return pow        # при цілій додатній степені і нуля
    else:
        return 1 / pow    #  при цілій відємній степені
a = float(input())
n = int(input())
print(power(a, n)) # визов функції для введених значень


#-----------------------------------------------------------------


# task3------------------------------------------------------------
"""
Умова: Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
а используя рекуррентное соотношение an=a⋅an-1.
"""
# Програма піднесення дійсного додатнього числа (a) до цілої не відємної степені (n)
def power(a, n): # створюємо функцію
    if n == 0:          # накладаємово умову для степені
        return 1
    elif n > 0:
        return a * power(a,n -1) # визов рекурсії для піднесення до степені

a = float(input())
n = int(input())
print(power(a, n)) # визов функції для введених значень


#-----------------------------------------------------------------


# task4------------------------------------------------------------
"""
Умова: Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фібоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""
# Програма яка за порядковим номером повертає значення числа Фібоначи
def fib(n): # створюємо функцію
    if n==1:        # накладаємо умову вмконання для різних значень
        return 1
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2) # визов рекурсії
n = int(input())
print(power(n)) # визов функції для введеного значення


#-----------------------------------------------------------------


