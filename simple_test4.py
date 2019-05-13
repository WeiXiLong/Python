#def greet_user(username):
#    """显示简单的问候语"""
#    print('Hello,'+ username.title() + '!')
#greet_user('jesse')

#def describe_pet(animal_type,pet_name):
#    """显示宠物的信息"""
#    print("\nI have a " + animal_type + '.')
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(pet_name='harry',animal_type='hamster')
#describe_pet('hamster','harry')

#def describe_pet(pet_name,animal_type = 'dog'):
#    describe_pet('willie')
#    describe_pet(pet_name='willie')
#
#    describe_pet('harry','hamster')
#    describe_pet(pet_name='harry',animal_type='hamster')
#    describe_pet(animal_type='hamster',pet_name='harry')

#def get_formatted_name(first_name,last_name):
#    """返回整洁的姓名"""
#    full_name = first_name + ' ' + last_name
#    return full_name.title()
#
#musician = get_formatted_name('jimi','hendrix')
#print(musician)


#def get_formatted_name(first_name,last_name,middle_name=''):
#    """返回整洁的姓名"""
#    if middle_name:
#        full_name = first_name + " " + middle_name + " " + last_name
#    else:
#        full_name = first_name + ' ' + last_name
#    return full_name.title()
#musician = get_formatted_name('jimi','hendrix')
#print(musician)
#musician = get_formatted_name('john','hooker','lee')
#print(musician)

#def build_person(first_name,last_name):
#    """返回一个字典，其中包含有关一个人的信息"""
#    person = {'first': first_name,'last':last_name}
#    return person
#musician = build_person('jimi','hd=endrix')
#print(musician)

#def get_formatted_name(first_name,last_name):
#    """返回整洁的姓名"""
#    full_name = first_name + " " + last_name
#    return full_name.title()
#
#while True:
#    print("\nPlease tell me your name: ")
#    print("enter 'q' at any time to quit")
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#    l_name = input("Last name: ")
#    if l_name  == 'q':
#        break#
#    formatted_name = get_formatted_name(f_name,l_name)
#    print("\nHello, " + formatted_name)

#unprinted_designs = ['iphone case','rebot pendant','dodecahedron']
#completed_models = []
#
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("Printing model : " + current_design)
#    completed_models.append(current_design)
#
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)

#def make_pizza(*toppings):
#    print(toppings)
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

#def build_profile(first,last,**user_info):
#    profile = {}
#    profile['first_name'] = first
#    profile['last_nmae'] = last
#    for key,value in user_info.items():
#        profile[key] = value
#    return profile
#
#user_profile = build_profile('albert','einstein',
#                             location = 'princeton',
#                             filed = 'physics')
#print(user_profile)

#import pizza
#pizza.make_pizza(16,'pepperoni')
#pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#from pizza import  func_name
#func_name()
#
#from pizza import make_pizza
#make_pizza(16,'pepperoni')

#from pizza import make_pizza as mp
#mp(16,'pepperoni')

#import pizza as p
#p.make_pizza(12,'mushrooms')
#p.func_name()

#from pizza import *
#make_pizza(12,'mushrooms')
#func_name()

#class Dog():
#    """一次模拟小狗的简单尝试"""
#    def __init__(self,name,age):
#        """初始化属性name和age"""
#        self.name   = name
#        self.age    = age
#
#    def sit(self):
#        """模拟小狗被命令时蹲下"""
#        print(self.name.title() + " is now sitting")
#
#    def roll_over(self):
#        """模拟小狗被命令时打滚"""
#        print(self.name.title() + " roll over!")
#
#my_dog = Dog('willie',6)
#your_dog = Dog('lucy',3)
#
#print("My dog's name is " + my_dog.name.title() + ".")
#print("My dog's age is " + str(my_dog.age) + " years old.")
#my_dog.sit()
#my_dog.roll_over()



#print("\nYour dog's name is " + your_dog.name.title() + ".")
#print("Your dog's age is " + str(your_dog.age) + " years old.")
#your_dog.sit()
#your_dog.roll_over()