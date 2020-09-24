
print('\nWelcome the Avgerage Test Caculaator')
stop = int (1) #Program Loop

while stop != 2:
    zerocheck = int(0) # Zero Check Var
    #Checking for Zero
    while zerocheck == 0:
        total = input('\nHow many tests did you take? : ')
        total = int(total)
        zerocheck = total

    totalcount = total # Counter var
    grade = 0  # Grade avg var
    testcount = 1 # Counter var

#Test Score Collection
    while totalcount != 0:
        gradesum = input(f'Test {testcount} Grade (0.00 - 100.00): ')
        gradesum = float(gradesum)
        while gradesum < 0 or gradesum > 100:
            print("\nYou inputed an Invaid Grade try again!")
            gradesum = input(f'Test {testcount} Grade (0.00 -100.00): ')
            gradesum = float(gradesum)
        grade = grade + gradesum
        testcount = testcount + 1
        totalcount = totalcount - 1

    grade = grade / total # Grade avg 

    #Grade Check
    if grade >= 90 and grade <= 100:
        message = 'A'
    elif grade >= 80 and grade <= 89:
        message = 'B'
    elif grade >= 70 and grade <= 79:
        message = 'C'
    elif grade >= 60 and grade <= 69:
        message = 'D'
    else:
        message = 'F'
        
    grade = round(grade, 2) # Rounds to 2 Dec.
    print(f'\nAfter taking {total} test(s) you have an avg of {grade} Getting you a {message}!')
    stop = input('\nDo you want to Try it again? 1 For Yes, 2 For No :')
    stop = int(stop)
    
    while ((stop != 1 or stop == 2) and (stop == 1 or stop != 2)):   
        stop = input('\nInvaid input! Do you want to Try it again? 1 For Yes, 2 For No :')
        stop = int(stop)
   
    zerocheck = int(0) # Zero Check Var

print('\nThanks For Running This Program!\n\n')


