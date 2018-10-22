#Stone Paper Scissors
import random

print("Welcome to stone paper scissor")


k = '0'

while k == '0':
# Get Guess

 def get_guess():
     return input("What is your guess? : ")


 x = get_guess()

# Generate Code

 def generate_code():

      spc = ['stone','paper','scissor']

      random.shuffle(spc)
 #return first choice
      return spc[0]

 y = generate_code()

 if x == y :

      print("Draw")

 elif x == 'stone' and y == 'scissor':

      print("You won")

 elif x == 'stone' and y == 'paper':

      print("You lose")

 elif x == 'scissor' and y == 'paper':

      print("You won")

 elif x == 'scissor' and y == 'stone':

      print("You lose")

 elif x == 'paper' and y == 'stone':

      print("You won")

 elif x == 'paper' and y == 'scissor':

      print("You lose")

 else:

      print("Nothing")

 k = input("Press 0 to continue or anything else to exit : ")
