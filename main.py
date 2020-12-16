#Task 1
def devide(a, b):
    try:
        return a / b
    except Exception:
        return 'ZeroDivisionError'

#Task 2
def get_info_user(first_name, last_name, byear, city, email, phone):
    return f'Full name: {first_name} {last_name}, {byear}, city: {city}, email: {email} and phone number: {phone}'
get_info_user = lambda first_name, last_name, byear, city, email, phone: f'Full name: {first_name} {last_name}, {byear}, city: {city}, email: {email} and phone number: {phone}'
print(get_info_user(first_name='Nurken', last_name="Spashev", byear=1992, city='Lenger', email='s.nurken92@gmail.com', phone=87784096092))

#Task 3
max_el = lambda a, b, c: max(a, b, c)
print(max_el(41,9,20))

#Task 4.1
custom_pow = lambda x, y: x ** y 
print(custom_pow(3, 2))
#Task 4.2
def custom_pow(x, y):
    result = 1
    for i in range(1, y + 1):
        result *= x
    return result
print(custom_pow(5, 3))

#Task 5
def get_sum(args):
    sum = 0
    for item in args: 
        sum += item 
    return sum 

result = 0
break_flag = 0
while True: 
    num_list = []
    num = input('Enter numbers: ').split()
    for el in num:
        if el.isdigit():
            num_list.append(int(el))
        else:
            break_flag += 1
    result += get_sum(num_list)
    print(f'Sum: {result}')
    if break_flag > 0:
        break

#Task 6
int_func = lambda string: string.title()

print(int_func('hi'))
test_string = input('Enter string: ').split()
print(' '.join(list(map(int_func, test_string))))