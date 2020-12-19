# Task 1
from sys import argv


def calculate_salary(args):
    if len(args) > 3:
        return (int(args[1]) * int(args[2])) + int(args[3])
    else:
        return 'Не хватаете аргументов'

print(calculate_salary(argv))

# Task 2
from random import randint

arr = [ randint(1, 100) for i in range(randint(15, 30))]
print(arr)

def get_largest(a):
    x, y = a
    if x < y:
        return x, y

list_tuple = list(filter(get_largest, list(zip(arr[::2],arr[1::2]))))

result = []
for item in list_tuple:
    a, b = item
    result.append(a)
    result.append(b)

print(result)

# Task 3
from random import randint

print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0 ])


# Task 4
arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in arr if arr.count(el) == 1 ])

# Task 5
from functools import reduce

arr = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(lambda a, b: a * b, arr))
print(reduce(lambda a, b: a + b, arr))

# Task 6.1
from itertools import count, cycle
from random import randint
a = int(input('Enter number(n < 100): '))
for n in count(a):
    if n == 100:
        break
    print(n)

# Task 6.2
arr = [randint(10, 20) for el in range(5, 20)]

i = 0
for item in cycle(arr):
    if i == 100:
        break
    print(item)
    i += 1

# Task 7

def fact(n):
    a = 1
    b = 1
    for item in range(1, n + 1):
        a = a * b
        b += 1
        yield a

for i in fact(5):
    print(i)