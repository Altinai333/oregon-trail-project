import random
from random import randint
distance = 0
energy = 50
sleep = 50 
totaltravel = 0
print ("Welcome to the immigration journey\nYou are a Mexican immigrant that wants to live in Florida")
print ("Your journey will be long and hard, therefore you will have to make choices")

while totaltravel <= 300: 
  longtravel = randint(20,30)
  travel = randint(10,20)
  rest = randint(10,20)
  

  list = ["Monterey", "Houston", "Baton rouge", "Tallahasse"]
  location = list [distance]
  
  print ("\nA. Travel at a slow pace \nB. Travel at a fast pace \nC. Eat for energy \nD. Rest for a day \nE. Check your location \nF. Learn about Mexican immigration \nG. Check your status \nQ. Quit")

  game = input("\nMake a choice ")
  
  if game.upper() == "A":
    energy -= 5
    sleep -= 5
    totaltravel += travel 
    print("You traveled", travel, "miles")
    print("You traveled", totaltravel, "miles in total")
    
  
  elif game.upper() == 'F':
    list = ["There were 10.9 million Mexican immigrants in the US in 2023", "More than half of Mexican immigrants in the United States live in California or Texas", "Mexicans immigrate to the US for better job and growth opportunity"]
    f = list 
    computer = random.choice(list)
    print(computer)

 
  elif game.upper() == 'B':
    energy -= 10
    sleep -= 5
    totaltravel += longtravel
    print("You traveled", longtravel, "miles")
    print("You traveled", totaltravel, "miles in total")
    


  elif game.upper() == 'C':
    energy += 20
    print("Your energy is", energy)
    
  
  elif game.upper() == 'D':
    sleep += rest
    print("You rested for a day")
    print("Your energy is now at", sleep )
    

 
            
  elif game.upper() == 'E':
   if totaltravel < 70:
       distance = 0
       print("You are in",(list[distance]))
   elif totaltravel < 150 and totaltravel > 69 :
       distance = 1
       print ("You are in",(list[distance]))
   elif totaltravel < 250 and totaltravel > 149:
       distance = 2
       print ("You are in",(list[distance]))
   elif totaltravel < 300 and totaltravel > 299:
       distance = 3
       print ("You are in",(list[distance]))
    
  if energy < 1:
    print("You are dead")
    quit()

  if sleep < 1:
    print("You are dead")
    quit()

  if game == 'Q':
    quit()
    

  if game.upper() == 'G':
   print("Your status is:") 
   print("Your energy is", energy)
   print("Your sleep is", sleep)
   print("You traveled", totaltravel,"miles")
   print("You have", (300 - totaltravel) , "miles left")
  if totaltravel > 299:
        print ("Congratulations !")
        print ("You are in Tallahasse, Florida")
        print("You can now enjoy your new life in America")