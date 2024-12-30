import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100. Try to guess it!")
    
    
    random_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
           
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


guess_the_number()
