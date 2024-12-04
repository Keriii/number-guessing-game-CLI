import random
from datetime import datetime

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

def select_difficulty():
    while True:
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        choice = input("Enter the difficulty level: ")
        if choice == '1':
            return 10, 'Easy'
        elif choice == '2':
            return 5, 'Medium'
        elif choice == '3':
            return 3, 'Hard'
        else:
            print("Invalid choice! Please select a valid difficulty level.")

def provide_hint(guess, number):
    if guess % 2 == 0 and number % 2 == 0:
        return "Hint: The number is even."
    elif guess % 2 != 0 and number % 2 != 0:
        return "Hint: The number is odd."
    elif abs(guess - number) <= 10:
        return f"Hint: You're very close! The number is within 10 of {guess}."
    else:
        lower_bound = max(1, number - 10)
        upper_bound = min(100, number + 10)
        return f"Hint: The number is between {lower_bound} and {upper_bound}."

def play_game(chances, level):
    number = random.randint(1, 100)
    attempts = 0
    start_time = datetime.now()

    print(f"Great! You selected {level} difficulty. You have {chances} chances.")
    print("Let's start the game!")

    while chances > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        attempts += 1
        if guess == number:
            time_taken = (datetime.now() - start_time).total_seconds()
            print(f"🎉 Congratulations! You guessed the correct number {number} in {attempts} attempts!")
            print(f"It took you {time_taken:.2f} seconds.")
            return attempts
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        chances -= 1
        print(f"You have {chances} chances left.")

        # Provide a hint every 2 incorrect guesses
        if chances > 0 and attempts % 2 == 0:
            print(provide_hint(guess, number))

    print(f"😞 Sorry, you've run out of chances. The number was {number}. Better luck next time!")
    return None

def main():
    display_welcome_message()
    best_scores = {'Easy': float('inf'), 'Medium': float('inf'), 'Hard': float('inf')}

    while True:
        chances, level = select_difficulty()
        result = play_game(chances, level)

        if result is not None:  # User guessed the number
            if result < best_scores[level]:
                best_scores[level] = result
                print(f"🎯 New best score for {level} difficulty: {result} attempts!")
            else:
                print(f"Your score: {result} attempts. Best score for {level} difficulty: {best_scores[level]} attempts.")
        else:
            print(f"Best score for {level} difficulty remains: {best_scores[level]} attempts.")

        play_again = input("Would you like to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Here's your summary:")
            for diff, score in best_scores.items():
                print(f"- {diff} difficulty: {score if score < float('inf') else 'No record'}")
            print("See you next time!")
            break

if __name__ == '__main__':
    main()