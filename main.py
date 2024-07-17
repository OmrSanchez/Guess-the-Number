#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


def compare():
	global chances
	chances -= 1
	if not guess == correct_number and chances == 0:
		print(f"You have {chances} chances remaining.\nYou Lose!\nThe number "
		      f"was {correct_number}")
		chances = 0
	elif guess == correct_number:
		print(f"That's correct you win!\nYou had {chances} left!\nNumber:"
		      f" {correct_number}")
		chances = 0
	elif guess > correct_number:
		print("Too High!")
	elif guess < correct_number:
		print("Too Low!")


def difficulty_level(d):
	global game_on
	if d == "easy":
		attempts = 10
	elif d == "hard":
		attempts = 5
	else:
		print("Invalid Input.")
		attempts = 0
	return attempts


def play_again():
	global game_on
	play_on = input("Do you want to play again? ")
	if play_on == "yes":
		play = game_on
	elif play_on == "no":
		play = not game_on
	else:
		play = not game_on
	return play


game_on = True
while game_on:
	print(logo)
	print(
		"Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100.")
	correct_number = random.randint(1, 100)
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
	chances = difficulty_level(difficulty)
	while chances > 0:
		print(f"You have {chances} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		compare()
	game_on = play_again()
