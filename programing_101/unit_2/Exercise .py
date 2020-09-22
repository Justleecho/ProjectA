# display a welcome message to the user, for some context
print("Welcome! Please enter your address:")

# collect address fields
street = input("Street number: ")
city = input("City: ")
state = input("State: ")
zip_code = input('Zip: ')

# format address using an f-string
print(f'''
{street}
{city}, {state}
{zip_code}
''')