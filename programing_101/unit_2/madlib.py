# >>> Give me an antonym for 'data': nonmaterial
# >>> Tell me an adjective: Bearded
# >>> Give me a sciency buzzword: half-stack
# >>> A type of animal (plural): parrots
# >>> Some Sciency thing: warp drive
# >>> Another sciency thing: Trilithium crystals
# >>> Sciency adjective: biochemical
# ...
# >>> Nonmaterial Scientist Job Description:
# >>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
# >>> Key responsibilities:
# >>> - Extract patterns from non-material
# >>> - Optimize warp drive
# >>> - Transform trilithium crystals into biochemical material.

# stnum1 = input("Street Number: ")
# stname1 = input('Street Name: ')
# city1 = input("City: ")
# state1 = input("State: ")
# zip1 = input('Zip: ')

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")