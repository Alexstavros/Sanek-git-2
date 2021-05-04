#name = 'Alex'
#age = 12
#name_and_age = 'My name is {0}. I\'m  {1} years old.'. format(name, age)
#print(name_and_age)
#name_and_age = F'My name is {name}. I\'m  {age} years old.'
#print(name_and_age)

#print('My name is %s. %s %d years old' % (name, "I'm" , age))
#########################################################################################################################################

number_list = [32, 21, 48, 34.56]
print(number_list)
some_list = [12, 34.334, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
print(another_list)
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list
########################################################################################
#new_list[5] = 'new item'
new_list.append('new item')
new_list.insert(0, 'start')
new_list.insert(2, 13)
#########################################################################################
new_list.pop(-1)
new_list.pop(0)
new_list.pop(-3)


#########################################
print(new_list)