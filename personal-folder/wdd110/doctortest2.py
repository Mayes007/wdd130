#python

count=0
while count<=100:
    print(count)
    count+=1

    print(f'The final count is: {count}')

recieve_correct_input=False
while not recieve_correct_input:

    response=input("you see a Moose - RUN or HIDE")
    
    if response.lower() == 'run':
        print('Run like a Charles Dickens')
        recieve_correct_input=True
    elif response.lower()=='hide':
        print('find a good place quickly')
        recieve_correct_input=True
    else:
        print('invalid input')