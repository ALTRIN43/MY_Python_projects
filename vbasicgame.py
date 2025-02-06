from random import randint

logo = """
    _           __           __  _ ____            
   (_)___  ____/ /__  ____  / /_(_) __/_  __       
  / / __ \/ __  / _ \/ __ \/ __/ / /_/ / / /       
 / / / / / /_/ /  __/ / / / /_/ / __/ /_/ /        
/_/_/ /_/\__,_/\___/_/ /_/\__/_/_/  \__, /         
  / /_/ /_  ___                    /____/          
 / __/ __ \/ _ \                                   
/ /_/ / / /  __/             __              ______
\__/_/_/_/\___/ ______ ___  / /_  ___  _____/ / / /
     / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/ / / / 
    / / / / /_/ / / / / / / /_/ /  __/ /  /_/_/_/  
   /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/  (_|_|_)   

"""
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5


# function to check user's fuess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty leve. Type 'easy' or 'hard' :")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN


def game():
    print(logo)
    # choosing a random number between 1 and 100
    print("Welcom to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess : "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of chance. you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
