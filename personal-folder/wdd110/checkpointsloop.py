#Python

number=int(input("Please type a positive number: "))

while number<0:
    print("Sorry, that is a negitive number. Please try again.")
    number=int(input("Please type a positive number: "))

    print(f"The number is: {number}")

    answer=""
    while answer !="yes":
        answer=input("May I have a piece of candy? ")

        print("Thank you.")