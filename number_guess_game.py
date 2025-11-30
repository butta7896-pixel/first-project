import random
import sys

def number_guessing_game():
    """A simple number guessing game where the player tries to guess a random number."""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Get difficulty level
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            max_num = 50
            max_attempts = 10
            difficulty = "Easy"
            break
        elif choice == "2":
            max_num = 100
            max_attempts = 7
            difficulty = "Medium"
            break
        elif choice == "3":
            max_num = 200
            max_attempts = 5
            difficulty = "Hard"
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    
    # Generate random number
    secret_number = random.randint(1, max_num)
    attempts = 0
    guessed = False
    
    print(f"\n🎯 Difficulty: {difficulty}")
    print(f"I'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    # Main game loop
    while attempts < max_attempts and not guessed:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            if guess < 1 or guess > max_num:
                print(f"⚠️  Please enter a number between 1 and {max_num}.")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                guessed = True
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            elif guess < secret_number:
                remaining = max_attempts - attempts
                print(f"📈 Too low! Try a higher number. ({remaining} attempts left)")
            else:
                remaining = max_attempts - attempts
                print(f"📉 Too high! Try a lower number. ({remaining} attempts left)")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    
    # Game over
    if not guessed:
        print(f"\n💔 Game Over! The number was {secret_number}.")
    
    # Ask to play again
    print("\n" + "=" * 50)
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        print("\n")
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye! 👋")
        sys.exit()

if __name__ == "__main__":
    try:
        number_guessing_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit()
