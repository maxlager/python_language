#task1------------------------------------------------------------
"""
Умова: Напишите программу, которая считывает три числа и выводит их сумму.
Каждое число записано в отдельной строке. 
"""
#Програма вираховує суму введених числ
number_one = float(input('Enter number one: '))
number_two = float(input('Enter number two: '))
number_three = float(input('Enter number three: '))
print('Sum 3 numbers is: ',number_one+number_two+number_three)



#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке. 
"""
#Програма вираховує площу прямокутного трикутника
catet_one = float(input('Enter catet one: '))
catet_two = float(input('Enter catet two: '))
print('Area of triangl is: ',catet_one*catet_two/2)



#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: N студентів отримали K яблук і розподілити їх між собою порівну.Неподілені яблука залишились у кошику.
Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
"""
#Програма вираховує кількість яблук в кожного студента і в кошику
number_of_students = int(input('Enter number of student: '))
number_of_apples = int(input('Enter number of apples: '))
print('The apples in one student is: ',number_of_apples // number_of_students)
print('The apples in basket is: ',number_of_apples % number_of_students)



#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі.
Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?
Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59).
Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.
"""
#Програма вираховує котрий час становить введена кількість хвилин
all_minets = int(input('Enter number of minets: '))
time_hours = all_minets//60 #вираховує кількість годин
time_minets = all_minets % 60 #вираховує залишок хвилин
print('The time is: ',time_hours%24,':',time_minets)



#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
 Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього.
 Наприклад “Hello, Mike!”
"""
#Програма виводить вітання користувачеві
your_name = input('Write your name: ')
print('Hello, '+your_name+'!')



#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
 Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
  	
 The next number for the number 179 is 180.
 The previous number for the number 179 is 178. 
"""
#Програма виводить попереднє і наступне значення цілого числа
number = int(input('Enter an integer number: '))
next_number = number-1 #наступне число
previous_number = number+1 #попереднє число
print('The next number for the number ', number,'is',next_number)
print('The previous number for the number', number ,'is',previous_number)


#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
 Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи.
 У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів.
 Яку мінімальну кількість столів необхідно придбати?
"""
#Програма вираховує найменшу кількість столів для учнів трьох груп
#за умови що за 1 партою не більше 2 учнів
class1 = int(input('Enter numper of students in first class'))
class2 = int(input('Enter numper of students in second class'))
class3 = int(input('Enter numper of students in third class'))
desks_1 = class1//2+class1%2 #потреба парт в першій групі учнів
desks_2 = class2//2+class2%2 #потреба парт в другій групі учнів
desks_3 = class3//2+class3%2 #потреба парт в третій групі учнів
all_desks = desks_1+desks_2+desks_3
print('You need the ',all_desks,' desks')



#-----------------------------------------------------------------
