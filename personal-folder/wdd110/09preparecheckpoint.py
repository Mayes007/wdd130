#python 
friends=[]

name=None

while name!= "end":
    name=input("Type the name of a friend: ")

    if name!="end":
        friends.append(name)

        print()
        print("Your friends are:")

        for friend in friends:
            print(friend)