#bicycles = ['task','readline','specialized']
#print(bicycles)
#
#name = ['wei','zhang','wang','bai']
#print(name[0])
#print(name[1])
#print(name[2])
#print(name[3])
#
#message = ' Hello'
#print(name[0] + message)
#print(name[1] + message)
#print(name[2] + message)
#print(name[3] + message)

#motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles)
#
#motorcycles.append('ducati')
#print(motorcycles)
#
#motorcycles = []
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#print(motorcycles)

#motorcycles = ['honda','yamaha','suzuki']
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)
#rem = motorcycles.remove('yamaha')
#print(motorcycles)
#print(rem)

#invite = ['bai','wang','zhang']
#print(invite[0])
#print(invite[1])
#print(invite[2])
#print('zhang can not engage')
#del invite[-1]
#invite.append('lin')
#for i in invite:
#    print(i)
#print('find a big desk\n')
#invite.insert(0,'li')
#num = len(invite)
#num = num // 2
#invite.insert(num,'Ha')
#invite.append('new')
#print(invite)
#
#print('sorry!\n')
#for i in invite[2:]:
#    print('Sorry,' + invite.pop())
#for i in invite[0:]:
#    print('keep down,' + i)
#del invite[0]
#del invite[0]
#print(invite)

#cars = ['bmw','audi','toyota','subaru']
#cars.sort()
#print(cars)
#
#cars.sort(reverse=True)
#print(cars)
#
#cars.sort(reverse=False)
#print(cars)
#
#cars = ['bmw','audi','toyota','subaru']
#print('Here is the original list: ')
#print(cars)
#
#print('\nHere is the sorted list: ')
#print(sorted(cars))
#
#print('\nHere is the original list:')
#print(cars)

#cars = ['bmw','audi','toyota','subaru']
#print(cars)
#print(len(cars))

#area = ['Chengdu','Hainan','Beijing']
#print(area)
#print(sorted(area))
#print(area)
#print(sorted(area,reverse=True))
#print(area)
#area.reverse()
#print(area)
#area.reverse()
#print(area)
#area.sort()
#print(area)
#area.sort(reverse=True)
#print(area)

#magicians = ['alice','david','carolina']
#for magician in magicians  :
#    print(magician)

#magicians = ['alice','david','carolina']
#for magician in magicians  :
#    print(magician.title() + ",that was a great trick!")
#    print("I can't wait to see you next trick, " + magician.title() + ".\n")
#print("Thank you,every one.That was a great magic show!")

    #message = 'Hello World!'   #错误，执行了不必要的缩进
    #print(message)             #错误，执行了不必要的缩进

#for value in range(1,5):
#   print(value)

#numbers = list(range(1,6))
#print(numbers)

#even_number = list(range(2,11,2))
#print(even_number)

#squares = []
#for value in range(1,11):
#    squares.append(value ** 2)
#print(squares)

#digits = [1,2,3,4,5,6,7,8,9,0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))

#squares = [value ** 2 for value in range(1,11)]
#print(squares)

#for i in range(1,21):
#    print(i)
#
#for i in range(1,1000):
#    print(i)
#Sum = 0
#for i in range(1,1000001):
#    Sum += i
#Min = min(range(1,1000001))
#Max = max(range(1,1000001))
#print(Min)
#print(Max)
#print(Sum)


#for i in range(1,21,2):
#    print(i)

#for i in list(range(3,31,3)):
#    print(i)


#print([value ** 3 for value in range(1,11)])

#for i in range(1,11):
#    print(i ** 3)

#players = ['charles','martina','michael','eli']
#print(players[0:3])

#players = ['charles','martina','michael','eli']
#print(players[1:4])

#players = ['charles','martina','michael','eli']
#print(players[:4])
#
#players = ['charles','martina','michael','eli']
#print(players[2:])
#
#players = ['charles','martina','michael','eli']
#print(players[-3:])
#
#players = ['charles','martina','michael','florence','eli']
#for player in players[:3]:
#    print(player)

#my_foods = ['pizza','falafel','carrot cake']
#friend_foods = my_foods[:]
#
#my_foods.append('cannoli')
#friend_foods.append('ice cream')
#
#print("My favorite foods are: ")
#print(my_foods)
#
#print("\nMy friend's favorite foods are: ")
#print(friend_foods)

#message = "The first three items in the list are:"
#print(message)
#print(message[:3])
#
#message = "Three items from the middle of the list are:"
#num = len(message) //  2
#print(message[num - 1:num + 2 ])
#
#message = "The last items in the list are"
#print(message[-3:])
#
#dimensions = [200,50]
#print(dimensions[0])
#print(dimensions[1])

#dimensions = (200,50)
#for dimension in dimensions:
#    print(dimension)

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


