'''
Unit 2
-Variables
-f-string
-input()
-intergers(whole numbers) /floats (desicmals)

'''

# Static string data

# Variables are named boxes that store data
# the data inside a variable can change
# variabels beacome the data ype they store
# #variables_name = som_+valve
# name = 'Eric'
# greeeting = "Hello"
# print(name)
# name ='Lime' # overrides name
# print(name)
# print ("Helloo "+name)

# # manipulate the date inside a variable
# print(name.upper())

'''
Varibles names in phythons
must start with a learter or a the underscore charcter
can only contain alpha0numeric characters adn the underscoores _
  A - Z a- z 0 - 9 andd _ they are case sesntives
  age, Age and AGE are all different variables


'''
'''
user_name = 'Dioysus'
user1 = 'hell'

#Rules of thumnb:
# variables names should be usually be lowercase words, lower case words if necessy
# variabels should be names to described data is

#invalid varibles
# can't start iwth number 
#2user

name = 'Eric'
city = 'Portland'


#print("Hello " + name + '! Today in ' + city)

# f-string f standed for f-strings allow sexpressions to be placed with curly brakcers{} f strigns started with a f before they opening quetea

message = f'Hello {name}! today is in {city} is cool and breezy'
#print(message)

#input(promput)message

# will pring the promt messages and wait for user to hit entter
# we need a variables to name to the user enter

#name = input('Ernter your name: ')
#print(f' Hello {name}')

'''

number = input("Please enter a number: ")
#number = int(number)
number = float(number)

print(f'{number} + 10 = {number + 10}')