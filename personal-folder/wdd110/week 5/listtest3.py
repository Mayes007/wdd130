#Python

#movies={'Star wars', "Startrek", "Captian America"}

#print(movies)
#for movie in movies:
  #  print(movie)

    #movies.append('The Grinch')

weekly_cost=[]

new_cost=-1.0
while new_cost!=0.0:
    new_cost=float(input("please input your weelly cost (0 to quit)"))
    if new_cost!=0:
        weekly_cost.append(new_cost)
        
        for coat in weekly_cost:
            print(cost)
        
        total_cost=0

        for cost in weekly_cost:
            total_cost+= cost
            print(f'Your total weekly cost was: ${total_cost}')
            print(f' Your adverage was: ${total_cost/len(weekly_cost)}')
