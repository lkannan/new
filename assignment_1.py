name = input('Please enter your name: ')
age = int(input('Please enter your age: '))


def print_name_age():
    print(name + ' ' + str(age))


def concat_print(arg1, arg2):
    print(arg1 + ' ' + arg2)


def decades_lived():
    return age//10


print_name_age()
concat_print(input('enter a string: '), input('enter another string: '))
print(decades_lived(), 'decades')
