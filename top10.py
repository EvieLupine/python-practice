TOP_TEN_ANSWERS = ["Femur", "Tibia", "Fibula", "Humerus", "Ulna", "Radius", "7th Rib", "8th Rib", ]

# ---------FUNCTIONS-----------

def introduction():
   #Ask the user their name
   name = input("Hello what is your name?")
   #Introduce them and the quiz topic
   print("Welcome to my quiz,", name)
   print("This quiz is about the Top Ten Most Immense Bones In Your Body.")

def getLives():
   while True:    
      lives = input("How many chances do you want?")
      try:   
            lives = int(lives)
            if lives >=0:   
                return lives
            else:   
                print("Please choose a positive number.")
      except:   
          print("That's not a number!")    

def isCorrect( answer, list):   
    if answer in list:  
        return True
    else:   
        return False
#-------------- MAIN CODE ----------------
introduction()
lives = getLives()
score = 0
# Start the questions 
while lives > 0:    
    answer = input("Can you name one of the top 10 biggest bones in your body?:\n").lower()
