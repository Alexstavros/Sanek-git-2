#car_prices = {'opel' : 5000, 'tayota' : 7000, 'bmw' : 10000}
#print(car_prices)
#print(car_prices['tayota'])
#car_prices['mazda'] = 4000
#print(car_prices)
#car_prices['opel'] = 2000
#print(car_prices)
#del car_prices['tayota'] 
#print(car_prices)
#car_prices.clear()
#print(car_prices)
###############################################################

person = {
    'first name' : 'Jack',
    'last name' : 'Brown',
    'age' : 43,
    'hobbies': ['football', 'singing', 'phone'],
    'children' : {'son': 'Mickhael', 'dauther': 'Pamela', } 
}
print(person['age'])
print(person['hobbies'])
print(person['hobbies'][2])

children = person['children']
print(person['children']['son'])

person['car'] = 'Mazda'
person['hobbies'][0] = 'basketball'

print(person.keys())
print(person.values())
print(person.items())