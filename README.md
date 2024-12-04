🎯 Number Guessing Game

A simple CLI-based number guessing game where the computer selects a random number between 1 and 100, and the user has to guess it within a limited number of attempts. The game offers multiple difficulty levels, a hint system, and tracks the best scores.
https://roadmap.sh/projects/number-guessing-game
    
## 📋 Features

- Difficulty Levels:\
Choose between Easy, Medium, and Hard, with varying numbers of attempts:
  - Easy: 10 attempts 
  - Medium: 5 attempts 
  - Hard: 3 attempts

- Hints System:\
Get helpful hints after every two incorrect guesses, such as:
  - Whether the number is even or odd. 
  - If you are within 10 numbers of the target. 
  - A narrowed range of possible numbers.
- High Scores:\
Tracks and displays your best score for each difficulty level.
- Timer:\
Displays the total time taken to guess the number correctly.
- Replay Option:\
Play multiple rounds until you decide to quit.

## 🛠️ Installation

1. Clone the repository:
``` bash
git clone https://github.com/Keriii/number-guessing-game-CLI.git
cd number-guessing-game
```

Ensure Python 3.9 is installed on your system.

Run the game:
```bash
python number_guessing_game.py
```
## 🚀 How to Play
1. Run the script and select a difficulty level:
```
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
```
2. Enter your guesses when prompted.
- If your guess is incorrect, you'll be told whether the number is higher or lower.
- Hints are provided every two incorrect guesses to assist you.
3. Continue guessing until you:
- Guess the correct number 🎉. 
- Run out of chances 😞.
4. After each round, decide whether to play again or quit.

📝 Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess what it is?

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter the difficulty level: 2
Great! You selected Medium difficulty with 5 chances.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.
You have 4 chances left.

Enter your guess: 25
Incorrect! The number is greater than 25.
Hint: You're very close! The number is within 10 of 25.
You have 3 chances left.

Enter your guess: 30
🎉 Congratulations! You guessed the correct number 30 in 3 attempts!
It took you 12.34 seconds.
Would you like to play another round? (yes/no): no

Thanks for playing! Here's your summary:
- Easy difficulty: No record
- Medium difficulty: 3 attempts
- Hard difficulty: No record
See you next time!
```