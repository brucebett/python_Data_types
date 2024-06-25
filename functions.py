def my_func():
    print("Hello welcome to my function")


my_func()


def mfunc():
    print("Are you sure you want to join?")
    print("Are you sure you want to join?")
    print("Are you sure you want to join?")


mfunc()
mfunc()
mfunc()


def my_string():
    hello = "Good morning sir, welcome back to my application"
    print(hello)


my_string()


def my_string1(name):
    print('Hello,' + name + 'welcome back to my application')


my_string1('john ')


def my_string2(name, age):
    print('Hello,' + name + ' Your age is ' + str(age) + 'years')


my_string2('Paul', 40)
my_string2('Njoki', 34)


def person(firstname, lastname, age):
    print('Hello, ' + firstname + '' + lastname + ' Your age is ' + str(age) + 'years')


person('Brian ', 'Bett', 20)
person(lastname='Kamau', age=34, firstname='Kelvin ')


def calc_multiple(x, y):
    return x * y
    print(calc_multiple(10, 20))
    print(calc_multiple(34, 56))


def calc_age(a, b):
    c = a + b
    return c


print(calc_age(10, 39))


def add_five(age):
    next_five_years = age + 5
    return next_five_years


specific_age = add_five(24)
print(specific_age)


def calc_your_age(name, age):
    if 5 < age < 7:
        print(f'{name} can move to garde 1')
    elif age == 5:
        print(f'{name} can join kindergarten')
    elif 4 >= age > 0:
        print(f'{name} can stay at home')


(calc_your_age('Judah', 6))
(calc_your_age('Eddah', 4))

