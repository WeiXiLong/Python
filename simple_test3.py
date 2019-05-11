#cars = ['audi','bmw','subaru','toyota']
#
#for car in cars:
#    if car == 'bmw':
#        print(car.upper())
#    else:
#        print(car.title())

#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')

#if 'a' == 'b':
#    print('True')
#else :
#    print('False')

#alien_0 = {'color':'green','points':5}
#
#print(alien_0['color'])
#print(alien_0['points'])
#print(alien_0)
#
#alien_0['x_positon'] = 0
#alien_0['y_position'] = 25
#print(alien_0)
#del alien_0['points']
#print(alien_0)

user_0 = {
    'username' : 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'medium': 'fermi'
}
#for key,value in user_0.items():
#    print("\nKEY: " + key)
#    print("Value: " + value )

#for key in user_0.keys():
#    print(key.title())

#for name in sorted(user_0.keys()):
#    print(name)

#for value in user_0.values():
#    print(value)
#
#for name in set(user_0.values()):
#    print(name.title())

#alien_0 = {'color':'green','points':5}
#alien_1 = {'color':'yellow','points':10}
#alien_2 = {'color':'red','points':15}
#aliens = [alien_0,alien_1,alien_2]
#print(aliens)

#aliens = []
#for aline_number in range(0,30):
#    new_alien = {'color':'green','points':5,'speed':'slow'}
#    aliens.append(new_alien)
#for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = '10'
#for alien in aliens[0:5]:
#    print(alien)
#print('...')

#pizza = {
#    'crust' : 'thick',
#    'toppings' : ['mushrooms','extra cheese']
#}
#
#print('You ordered a ' + pizza['crust'] + '-crust pizza' + 'with the following toppings:')
#for topping in pizza['toppings']:
#    print('\t' + topping)

#favorite_languages = {
#    'jen' : ['python','ruby'],
#    'sarah': ['c'],
#    'edward' : ['ruby','go'],
#    'phil' : ['python','haskell']
#}
#
#for name,languages in favorite_languages.items():
#    print('\n' + name.title() + "'s favorite languages are: ")
#    for language in languages:
#       print('\t' + language.title() )

#users = {
#    'aeinstrin' : {
#        'first' : 'albert',
#        'last' : 'einstein',
#        'location' : 'princeton'
#    },
#    'mcurie' : {
#        'first' : 'marie',
#        'last' : 'curie',
#        'location' : 'paris'
#    }
#}
#
#for name,user_info in users.items():
#    print('\nUsername:' + name)
#    full_name = user_info['first'] + ' ' + user_info['last']
#    location = user_info['location']
#    print('\t Full name : ' + full_name.title() )
#    print('\t Location  : ' + location.title())

#prompt = "\nTell me something,and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

#prompt = "\nTell me something,and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#active = True
#while active:
#    message = input(prompt)
#    if(message == 'quit'):
#        active = False
#    else:
#        print(message)

