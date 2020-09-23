#------- Excerise 1.1 --------

print("Welcome! Please enter your address:")

# Variables Fields 
skip1 = input("Hit Enter For To Start Exercise 1.1 ")
print('Exercise 1.1 - Mailing Address without proper capitalize')
stnum1 = input("Street Number: ")
stname1 = input('Street Name: ')
city1 = input("City: ")
state1 = input("State: ")
zip1 = input('Zip: ')

# Format address using an f-string
print(f'''
{stnum1} {stname1}
{city1}, {state1}
{zip1}
''')

#------- Excerise 1.2 --------

skip2 = input("Hit Enter For Next Exercise 2.1 ")
print('Exercise 1.2 - Mailing Address with proper capitalize')
stnum2 = input("Street Number: ")
stname2 = input('Street Name: ')
city2 = input("City: ")
state2 = input("State: ")
zip2 = input('Zip: ')

stname2 = stname2.title()
city2 = city2.title()
state2 = state2.title()

# Format address using an f-string
print(f'''
{stnum2} {stname2}
{city2}, {state2}
{zip2}
''')

#------- Excerise 2.1 --------

word = 'bookkeeper'
letter = 'k'

letter_count = word.count(letter)

print(f"The letter '{letter}' occurs in the word '{word}' {letter_count} times.")

#------- Excerise 2.2 --------
word1 = input("In: ")