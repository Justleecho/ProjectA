
print('\nWelcome the Avgerage Test Calculator')
stop = int (1) #1st Start

#1 for go, 2 for Stop Program Loop
while stop != 2:
    zerocheck = int(0) # Zero Check Var
    #Checking for Zero
    while zerocheck == 0:
        # Int only
        while True:
            try:
                print('\n\nRemember 0 is not a good number and Only Whole Numbers!')
                total = int(input('\nHow many tests did you take? : '))
                zerocheck = total
                break
            except:
                print("\n\nReminder Whole Numbers are Allowed, Repeat Input! \n\n")


    totalcount = total # Counter var
    grade = 0  # Grade avg var
    testcount = 1 # Counter var

#Test Score Collection
    while totalcount != 0:
        # Float Only
        while True:
            try:
                gradesum = float(input(f'Test {testcount} Grade (0.00 - 100.00): '))
                break
            except:
                print("\n\nNumbers Only, Repeat Input! \n\n")
        while gradesum < 0 or gradesum > 100:
            print("\n\nOut of Range!! (0.00 - 100.00)\n\n")
            gradesum = float(input(f'Test {testcount} Grade (0.00 - 100.00): '))
        
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
    #Int Only
    while True:
        try:
            stop = int(input('\nDo you want to Try it again? 1 For Yes, 2 For No :'))
            break
        except:
            print("\n\nInvaid input! 1 For Yes, 2 For No, Repeat Input! \n\n")
    #1 or 2 Only
    while ((stop != 1 or stop == 2) and (stop == 1 or stop != 2)):   
         #Int Only
         while True:
            try:
                stop = int(input('\n\nInvaid input! To Try it again 1 For Yes, 2 For No :'))
                break
            except:
                print("\n\nInvaid input! 1 For Yes, 2 For No, Repeat Input! \n\n")

    zerocheck = int(0) # Zero Check Var

print('\n\n\nThanks For Running This Program Goodbye!\n\n\n')


