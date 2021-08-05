another_string = 'I want to lern Python'
print(another_string)
some_string  = 'I\'programer'
print(some_string)

string_with_new_lines = "Hello! \n         \rMy name is Ivan"
print(string_with_new_lines)

numbers = "1\t23\t4567"
print(numbers)
some_text = "\t Hello! /nI'm very glat to see you"
print(some_text)

string_with_triple_quotes = """this is ' with text "triple quotes" """
anoter_string_with_triple_quotes = '''this is ' with text "triple quotes '''
print(string_with_triple_quotes)
print(anoter_string_with_triple_quotes)

greeting = 'hello python!'
greeting_length = len(greeting)
print(len(greeting))

print(greeting[1])
print(greeting[6])
print(greeting[-1])
print(greeting[-4])

print(greeting[2:5])
print(greeting[6:10])
print(greeting[6:10])
print(greeting[7:13])
print(greeting[0:12])
print(greeting[-5:-2])
print(greeting[5: ])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

first_name = 'Jake'
print(first_name[2])
first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)


new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello!'
greeting = greeting + ' Python!'
print(greeting)


yummy = 'Yum'
print(yummy * 3)

yummy = 'Yum'
print(yummy * 2)

print(yummy.upper())
print(yummy.lower())
print(yummy)

long_string = 'This is the long string'
print(long_string.split())

print(1 + 1)
print('1' + '1')
age = 23
print('Jack is ' + str(age) + 'years old.')
print('Jack is ' + str(23) + 'years old.')

name = 'jack'
age = 23
name_and_age = 'my name is {0}.I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'my name is {0}.I\'m {1} years old.'.format('jack', 23)
print(name_and_age)
name_and_age = 'my name is {}.I\'m {} years old.'.format('jack', 23)
print(name_and_age)
week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'\
.format'('Monday', 'Tuesday', 'Wetnesday', 'Thusday', 'Friday', 'Saturday', 'Sunday')

