#task1------------------------------------------------------------
"""
�� ������� ������ ����� N ������������ ��� �������� ����������� �����, �� ������������� N, � ������� �����������.
"""



n = int(input())
i = 1

while i*i <= n:
    print(i*i)
    i += 1

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
���� ����� �����, �� ������� 2. �������� ��� ���������� ����������� ��������, �������� �� 1.
"""



n = int(input())
i = 2

while n%i != 0:
    i += 1
print(i)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
�� ������� ������������ ����� N ������� ���������� ����� ������� ������, �� ������������� N. �������� ���������� ������� � ���� �������.

��������� ���������� � ������� ������������ ������!
"""



n = int(input())
pow = 1
i = 0

while pow <= n:
    i += 1
    pow *= 2
print(i - 1, pow // 2)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
� ������ ���� ��������� �������� x ����������, � ����� �� ������ ���� ���������� ������ �� 10% �� ����������� ��������. �� ������� ����� y ���������� ����� ���, �� ������� ������ ���������� �������� �� ����� y ����������.

��������� �������� �� ���� �������������� ����� x � y � ������ ������� ���� ����������� �����.
"""



x = float(input())
y = float(input())
i = 1

while x < y:
    x *= 1.1
    i += 1
print(i)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
����� � ����� ���������� x ������. �������� �� ������������� �� p ���������, ����� ���� ������� ����� ������ �������������. ����������, ����� ������� ��� ����� �������� �� ����� y ������.

��������� �������� ����� ������ �������������� ��������, ��� ���� � ��� ��������� 123.4567 ������, �. �. 123 ����� � 45.67 ������, �� ����� ���������� � ��� ��������� 123 ����� � 45 ������, �.�. 123.45 ������.

��������� �������� �� ���� ��� ����������� �����: x, p, y � ������ ������� ���� ����� �����.
"""



x = int(input())
p = int(input())
y = int(input())
i = 0

while x < y:
    x = int(x * (1 + (p/100)) * 100) /100
    i += 1
print(i)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
��������� �������� �� ���� ������������������ ����� ��������������� �����, ������ ����� �������� � ��������� ������. ������������������ ����������� ������ 0, ��� ���������� �������� ��������� ������ ��������� ���� ������ � ������� ���������� ������ ������������������ (�� ������ ������������ ����� 0). �����, ��������� �� ������ 0, ��������� �� �����.
"""



number = 1
sum = 0

while number != 0:
    number = int(input())
    sum += number
print(sum)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
���������� ����� ���� ��������� ������������������, ������������� ������ 0. � ���� � �� ���� ��������� ������� �����, ��������� �� ������ �����, ��������� �� �����.
"""



number = 1
sum = 0

while number != 0:
    number = int(input())
    sum += number
print(sum)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
���������� ������� �������� ���� ��������� ������������������, ������������� ������ 0.
"""



number = 1
sum = 0
i = 0

while number != 0:
    number = int(input())
    sum += number
    i += 1
i -= 1
print(sum/i)

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. ���������� �������� ����������� �������� ������������������.
"""



number = 1
max = 0

while number != 0:
    number = int(input())
    if number > max:
        max = number

print(max)

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. ���������� ������ ����������� �������� ������������������. ���� ���������� ��������� ���������, �������� ������ ������� �� ���. ��������� ��������� ���������� � ����.
"""



number = 1
max = 0
i = 0
index = 0

while number != 0:
    number = int(input())
    if number > max:
        max = number
        index = i
    i += 1
print(index)

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
���������� ���������� ������ ��������� � ������������������, ������������� ������ 0.
"""



number = 1
max = 0
count = 0

while number != 0:
    number = int(input())
    if number % 2 == 0 and number != 0:
        count += 1
print(count)

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. ����������, ������� ��������� ���� ������������������ ������ ����������� ��������.
"""



number = 1
prev = 0
i = 0

while number != 0:
    number = int(input())
    if number > prev:
        if prev != 0:
            i += 1
    prev = number
print(i)

#-----------------------------------------------------------------


#task13------------------------------------------------------------
"""
������������������ ������� �� ��������� ����������� ����� � ����������� ������ 0. ���������� �������� ������� �� �������� �������� � ���� ������������������. �������������, ��� � ������������������ ���� ���� �� ��� ��������.
"""



number = 1
first = 0
second = 0

while number != 0:
    number = int(input())
    if number > first:
        second = first
        first = number
    elif number > second:
        second = number
print(second)

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. ����������, ������� ��������� ���� ������������������ ����� �� ����������� ��������.
"""



number = 1
max = 0
i = 1

while number != 0:
    number = int(input())
    if number > max:
        i = 1
        max = number
    elif number == max:
        i += 1
print(i)

#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
�� ������� ����� n ���������� n-� ����� ���������.

��� ������ ����� ������ � ������ for.
"""



i = 0
n_1 = 1
n_2 = 0
n = 0
count = int(input()) - 1

for i in range(0, count):
    n = n_1 + n_2
    n_2 = n_1
    n_1 = n
if count == 0:
    n = 1
print(n)

#-----------------------------------------------------------------


#task16------------------------------------------------------------
"""
���� ����������� ����� A. ����������, ����� �� ����� ������ ��������� ��� ��������, �� ���� �������� ����� ����� n, ��� �n = A. ���� � �� �������� ������ ���������, �������� ����� -1.
"""



a = int(input())
i = 0

n_2, n_1 = 0, 1
while True:
    if n_1 > a:
        i = -1
        break
    elif n_1 == a:
        i += 1
        break
    n_2, n_1 = n_1, n_2 + n_1
    i += 1
print(i)

#-----------------------------------------------------------------


#task17------------------------------------------------------------
"""
���� ������������������ ����������� �����, ������������� ������ 0. ����������, ����� ���������� ����� ������ ������ ��������� ���� ������������������ ����� ���� �����.
"""



number = 1
i = 1
prev_i = 0
prev = 0

while True:
    number = int(input())
    if number == 0:
        break
    if number == prev:
        i += 1
    else:
        i = 1
    if i > prev_i:
        prev_i = i
    prev = number
print(prev_i)

#-----------------------------------------------------------------


#task18------------------------------------------------------------
"""
���������� ����������� ���������� ��� ������ ������������������ ����������� �����, ������������� ������ 0.
"""



number = 1
n = 0
sum_elements = 0
sum_square_elements = 0
s = 0

while True:
    number = int(input())
    if number == 0:
        break
    sum_elements += number
    sum_square_elements += number**2
    n += 1

standart_deviation = ((sum_square_elements - (2 * (sum_elements ** 2))/n + n*(sum_elements/n)**2)/(n-1))**0.5
print(standart_deviation)

#-----------------------------------------------------------------


