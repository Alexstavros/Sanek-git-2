#tuple_1 = 1, 2, 3
#tuple_2 = ('one, hello')
#tuple_3 = (3, 2.3, 'three')
#
#new_tuple = (tuple_1[0], 3, tuple_1[-1])
#print(new_tuple)
#
#
#print(tuple_1[1])
#print(type(tuple_1))
#print(tuple_2)
#print(tuple_3)

x = y = z = 12
x, y, z = 12, 13, 14

print(x, y, z)

person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple

print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(5))