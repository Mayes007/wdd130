#Python 

print("This is line one.", end="")
print("This is line two.")

word="commitment"

favorite_letter=input("What is your favorite letter? ")


for letter in word:
    if letter.lower()=="favorite_letter()":
        print(letter.upper(), end="")
    else:
     print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower()== favorite_letter.lower():
        print("_", end="")
else:
   print(letter.lower(), end="")
   print()


   quote= "In coming days, it will not be possoble to survive spiritually without the guiding, directing, comforting, and contand influece of the Holy Ghost."
   run_again= "yes"

   while run_again== "yes":
      user_number=int(input("Please enter a number: "))
      for i, letter in enumerate(quote):
         if i% user_number==0:
            print(letter.upper(), end="")
         else:
            print(letter.lower(), end="")
            print()

            run_again=input("Would you like to enter another number? ")

            print("Goodbye")