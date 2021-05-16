rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',  'purple', 'indigo'}

print(rainbow_colors)
print(type(rainbow_colors))

empy_set = set()
print(empy_set)
print(type(empy_set))

empy_set = set()
print(empy_set)
print(type(empy_set))

number_list = [1, 43, 56, 3, 3, 3]
text_tuple = ('sdada', 'adada', 'sasdssad', 'hi', 'hi', 'hi')
set_from_list =set(number_list)
set_from_tuple =set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777)
set_from_tuple.add('hello')

set_from_list.pop()

print(set_from_list)
print(set_from_tuple)