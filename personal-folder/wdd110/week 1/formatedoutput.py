#python

first_name=input('what is your first name ')
last_name=input('what is your last name ')
middle_name= input('what is your middle name ')

print(first_name, last_name, middle_name)

print(f'Hi {first_name}, its nice to meet you.')
print(f'Your full name is: {first_name} {middle_name} {last_name}')
my_formated_string=f'Your full name is: {first_name} {middle_name} {last_name}'
print(my_formated_string)

my_long_formated_string=f"""this is my long string that is similar to my homework assignment this weekwnd.
{first_name}- it is nice to meet you.
your full name is: {first_name},{middle_name}, {last_name}"""

print=(my_long_formated_string)