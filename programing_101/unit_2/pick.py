
print('I am bad at Madlibs so you are going on hike instead!')

#Name input
name = input("What is your name: ")

PickNum = input('Pick a number 1-10 or else... ')
PickNum  = int(PickNum)

#If Else Test
if PickNum  < 1 or PickNum  > 10:
    print("Guessing you don't listen, I will pick for you! Zero")
    PickNum  = ('Zero')
else: 
    PickNum  = int(PickNum)


#String Inputs
city = input("Enter a city: ")
item1 = input("Enter tool in your backpack: ")
item2 = input('Enter food in your backpack: ')

#Tittle Strings
name = name.title()
city = city.title()
item1 = item1.title()
item2 = item2.title()

#Using Print f
print(f'''
{name} wanted to on a hike in the city of {city}
{name} brought the following items:
- {item1} 
- {item2}
- {PickNum} Bottle(s) of Water
''')
end = input("Hit Enter to End Program......")
