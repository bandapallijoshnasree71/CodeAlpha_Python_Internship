import random

def play_hangman():
    # 1. Setup our data
    words = ["python", "coding", "syntax", "modular", "variable"]
    secret_word = random.choice(words)
    
    # Create a list of underscores to represent the hidden word
    display = ["_"] * len(secret_word)
    
    lives = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    # 2. Main Game Loop
    while "_" in display and lives > 0:
        print(f"\nWord to guess: {' '.join(display)}")
        print(f"Lives remaining: {lives}")
        print(f"Letters guessed: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()

        # Validation: Check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        # Check if already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
            
        guessed_letters.append(guess)

        # 3. Check the guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the display with the correct letter at every index it appears
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    display[index] = guess
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not there. You lost a life.")

    # 4. End Game Logic
    if "_" not in display:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
    else:
        print(f"\nGame Over. You ran out of lives. The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
  Initial commit for Task 1
