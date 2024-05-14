score = 0
# Ask the user their name and store it. Hello what is your name? 
name = input("Hello what is your name?")
print(name, "? What a lovely name lets start")
# Introduce the quiz and what it is about.
print("Welcome to my quiz, I will be asking serveral questions and you just have to answer!")

print("This quiz is Guess The Animal! I will be asking you to guess an animal based off of it's features and adjectives used to describeit. It's okay if you don't get it right.")
# Ask the user a question and get their response.
# Afterwards tell them the answer if it is wrong or right.
answer = input("What is this animal?" "It is a fluffy mammal, has four legs, it meows, fairly small, has whiskers and typically lives in a house.") 
if answer == "Cat" or answer == "cat":   
 print("Awesome! That's correct!")
 score += 1
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is cat!")
# Repeat untill quiz is finished.
answer = input("Okay, what is this animal now?" "It can vary from size, has four legs, usually fluffy, barks and is usally called 'Man's Best Friend.")
if answer == "Dog" or answer == "dog":   
 print("Awesome! That's correct!")
 score += 1
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Dog!")


answer = input("I will try make this harder now." "This animal has a long neck, eats leaves from tall trees, covered in spots and has a purple tongue." "What animal is this?")
if answer == "Giraffe" or answer == "giraffe":   
 print("Yes good job!")
 score += 1
elif answer == "":  
 print("Sorry I don't get it.")
else:   
 print("No sorry that isn't it.")
print("The answer is Giraffe!")

answer = input("This animal is powerful and has two horns on the top of it's head, it has four legs with hooves and are male but often get called by another name that starts with c and they are often said to be attracted to the colour red.")

# Leave with a sign off. 
if answer == "Bull" or answer == "bull":   
 print("Awesome! That's correct!")
 score += 1
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Bull!")

answer = input("This animal has no fur, it is scaly, not slimy and has no legs.")
if answer == "Snake" or answer == "snake":   
 print("Awesome! That's correct!")
 score += 1
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Snake!")

answer = input("This animalis fluffy, likes to swim, is the largest rodent in the world and is native to central South America.")
if answer == "Capybara" or answer == "capybara":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Capybara!")

answer = input("This animal weighs 1,000 kgs, they are native to the arctic circle, have two very large teeth and are quite lazy." "What animal do you think it is?")
if answer == "Walrus" or answer == "walrus":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Walrus!")

answer = input("This animal is one of Africa's most deadly killers, it is relatively the same size as a wolf, a fun fact about them is that they are born with a full set of teeth. They also like to laugh." "What is your guess?")
if answer == "Hyena" or answer == "hyena":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Hyena!")

answer = input("This next animal is cheeky and lives in trees, they eat fruit, seeds and some even eat meat. They also have have hands that they use to climb with. What do you guess?")
if answer == "Monkey" or answer == "monkey":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Monkey!")

answer = input("This animal can be quite large and scary, it spends most of it's time waiting for its next meal in the water and has a large set of teeth, this animal is a reptile. Your guess?")
if answer == "Alligator" or answer == "alligator":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Alligator!")


answer = input("Smaller than a typical wolf, this animal has almost an identical resemblence but is smaller,it howls barks and makes weird noises too. It is also native to america like the Grey Wolf and is a canine. What do you think it is?")
if answer == "Coyote" or answer == "coyote":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Coyote!")

answer = input("This animal is a type of insect typically potrayed in African themed films and likes to roll up balls of poop. It has a wide body with sturdy legs. Your guess?")
if answer == "Dung Beetle" or answer == "dung beetle":   
 print("Awesome! That's correct!")
 score += 2
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Dung Beetle!")

answer = input("This animal can be found in almost all continents of the word they have four legs, they are fluffy, usually hunted for their meat and because for some counties they are pests. They can extrude horns if they are male.")

if answer == "Doe" or answer == "doe":   
 print("Awesome! That's correct!")
 score += 1
elif answer == "":  
  print ("Not sure what you meant by that?!")
else:     
  print("Good job but that is wrong.")
print("The answer is Doe!")

question = "What is the current largest mammal on land?"
a = "Dinosaur"
b = "Elephant"
c = "Whale"
d = "Hippo"
answer = input("{}\nA.{} B.{} C.{} D.{}}".format(question, a, b, c, d)).lower()
# Check the user's answer
if answer == a or answer == "a": 
  print("Correct!")
score += 5
print("Well done {}!" "You finished my quiz!" "Here is your score. {}".format(name, score)) 

