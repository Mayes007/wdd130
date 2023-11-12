grade=int(input("what is your grade precent? "))

if grade>=90:
    letter="A"
elif grade>=80:
    letter="B"
elif grade>=70:
    letter="C"
elif grade>=60:
    letter="D"
else:
    letter="F"

print(f"Your letter grade is {letter}")

if grade>=70:
    print(f"Congradulations! you have passed the class")
else:
    print(f'Stay focused and you\'ll get it next time! ')

sign=""
last_digit= grade % 10
if last_digit>=7:
    sign="+"
elif last_digit<3:
    sign="-"
else:
    sign=""

if grade>=93:
    sign=""
    
if letter=="f":
    sign=""
    print(f'Your letter grade is {letter} {sign}')

if grade>=70:
    print('Congradulations you pass the class')
else:
    print('Stay focused and you\'ll get it next time')
