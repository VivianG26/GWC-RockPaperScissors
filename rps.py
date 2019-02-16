import random

player = raw_input("rock, paper, or scissors?")

computer = random.randint(1,3)

#print computer

if (player == "rock" and computer == 3):
	print("computer chose scissors")
	print("player wins")

elif (player == "paper" and computer == 1):
	print("computer chose rock")
	print("player wins")
	
elif (player == "scissors" and computer == 2):
	print("computer chose paper")
	print("player wins")
	
elif (player == "rock" and computer == 2):
	print("computer chose paper")
	print("computer wins")
	
elif (player == "paper" and computer == 3):
	print("computer chose scissors")
	print("computer wins")
	
elif (player == "scissors" and computer == 1):
	print("computer chose rock")
	print("computer wins")
	
else:
	print("it's a tie!")
	
	