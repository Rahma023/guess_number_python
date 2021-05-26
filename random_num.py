import random

def guess_number(r):
    random_number=random.randint(1, r)
    guess=0
    while guess != random_number:
        guess=int(input("Guess a number between 1 and {r}"))
        if guess < random_number:
            print("Sorry, too low, guess again")
        elif guess > random_number:
            print("Sorry, too high, guess again")

    print("Congrats you have guessed the number {random_number} correctly")

def computer_guess(r):
    low=1
    high=r
    feedback=""
    while feedback != "c":
        if low != high:
           guess=random.randint(low, high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H) too low (L) or correct (c) !!").lower()
        if feedback=="h":
            high=guess-1
    
        elif feedback=="l":
            low=guess+1
    print("Congrats! The computer guessed your number {guess} correctly")

computer_guess(400)          

        
    
