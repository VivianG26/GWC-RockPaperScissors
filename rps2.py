import random

user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:

	user_choice = raw_input("Rock, Paper, Scissors?")

	computer_choice = random.randint(1,3)

	if computer_choice == 1:
		computer_word = "Rock"
	elif computer_choice == 2:
		computer_word = "Paper"
	elif computer_choice == 3:
		computer_word = "Scissors"
		
	if user_choice == "Rock" and computer_word == "Paper":
		print("Computer Wins")
		computer_wins = computer_wins + 1
	elif user_choice == "Scissors" and computer_word == "Rock":
		print("Computer Wins!")
		computer_wins = computer_wins + 1
	elif user_choice == "Paper" and computer_word == "Scissors":
		print("Computer Wins!")
		computer_wins = computer_wins + 1
	elif user_choice == "Rock" and computer_word == "Scissors":
		print("User Wins!")
		user_wins = user_wins + 1
	elif user_choice == "Paper" and computer_word == "Rock":
		print("User Wins!")
		user_wins = user_wins + 1
	elif user_choice == "Scissors" and computer_word == "Paper":
		print("User Wins!")
		user_wins = user_wins + 1
	else:
		print("Tie")
		
if computer_wins == 
		
	