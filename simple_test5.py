#filename = 'D:\pi_digits.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()

#for line in lines:
#    print(line.rstri#p())

#pi_string = ''
#for line in lines:
#    pi_string += line.strip()
#print(pi_string)
#print(len(pi_string))

#filename = 'D:\pi_digits.txt'
#
#with open(filename,'a') as file_object:
#    file_object.write("I love this\n")
#    file_object.write("I love creating new games.\n")

#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

#print("Given me two numbers,and I'll divide them.")
#print("Enter 'q' to quit.")
#
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print("You can't divide by 0!")
#    else:
#        print(answer)


#filename = 'D:\pi_digits.txt'
#try:
#    with open(filename) as f_obj:
#        contents = f_obj.read()
#except FileNotFoundError :
#    msg = "Sorry,the file " + filename + " does not exist."
#    print(msg)

#title = "Alice in Wonderland"
#print(title.split())

#def count_words(filename):
#    try:
#
#    except  FileNotFoundError:
#        pass
#    else:
#
#
#filenames = ['alice.txt','pi_digits.txt']
#for filename in filenames:
#    count_words(filenames)

import  json

#numbers = [2,3,5,7,11,13]
#filename = 'D:\\numbers.json'
#with open(filename) as f_obj:
#    numbers = json.load(f_obj)
#    print(numbers)
#    json.dump(numbers,f_obj)

#username = input("What is your nmae? ")

#filename = 'D:\\username.json'
#with open(filename,'w') as f_obj:
#    json.dump(username,f_obj)
#    print("We'll remember you when you come back, " + username + "!")

#with open(filename) as f_obj:
#    username = json.load(f_obj)
#    print(username)

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它

#def greet_user():
#    filename = 'D:\\username.json'
#    try:
#        with open(filename) as f_obj:
#            username = json.load(f_obj)
#    except  FileNotFoundError:
#        username = input("What is your name? ")
#        with open(filename,'w') as f_obj:
#            json.dump(username,f_obj)
#            print("We'll remember you can come back, " + username + "!")
#    else:
#        print("Welcome back, " + username + "!")
#
#greet_user()


#def get_formatted_name(first,last,middle=''):
#    if middle:
#        full_name = first + " " + middle + " " + last
#    else:
#        full_name = first + " "  + last
#
#    return full_name.title()
#