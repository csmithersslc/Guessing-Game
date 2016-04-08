#Christina Smithers
#
#04/07/2016



#This is just a little guessing game
#The player picks a range of numbers with an upper limit.
#The player can also choose the number of attemps they will make as long as 
#it's under than range limit. It will tell the player if their guess is too
#high, too low, or just right.  Then they can have a clean exit.



#let's also do a clean exit so import sys
#import sys

#player gets 5 tries
tries = 5



#start out with the person's name
print("===============================================================")
print("==========           GUESSING GAME     ========================")
print("===============================================================")
print ("\nHello!  Welcome to the Guessing Game.  Can I get your name?")
playerName = input()

#Tell the player the game
print ("Thanks,%s. This is a game where I think of a number which you will guess. You can choose the upper limit." % playerName)

#setup the range

print ("Okay, let's begin.  What will be the upper limit?")
upperLimit = int(input())

#picks a random number now that it has the limit
randomNumber = randint(1, upperLimit)

#start the game
print ("Well, here goes the game. I am thinking of a number between 1 and ", upperLimit)
#number has to be within the specified number of tries until it's guessed
print ("What do you think the number is?")

for try_num in range (1,tries+1):
		guess = int(input(">")
	#too high
			if guess < randomNumber:
				print("Higher...")
	#too low
	
			elif guess > randomNumber:
				print("Lower...")

	else guess == randomNumber:
		print("*****************CONGRATULATIONS***********************")
		print("Yay!  You got it!  The number was ", randomNumber)
		print("You guessed it after ", tries, "guesses")
		break
else:
	print("Sorry,  You've run out of guesses.  I was thinking of ", randomNumber," .")

break
			
	


#clean exit out
#input("\n\n Hit 0 to exit the game.")
#sys.exit(0)







