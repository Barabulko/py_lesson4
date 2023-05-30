'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

n = int(input("enter n: "))
m = int(input("enter m: "))
list1 = []
list2 = []
print("enter 1st list:")
for i in range(n):
    list1+=[int(input())]

print("enter 2nd list:")
for i in range(m):
    list2+=[int(input())]

set1 = set(list1)
set2 = set(list2)
set3 = set1&set2

list3 = list(set3)
list3.sort

print(list3)