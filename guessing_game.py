import random 
import time
while True:
    start_time = time.time()
    number = random.randint(1, 100) 
    print("Guess a number between 1 and 10") 
    guess = int(input())
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    if guess == number: 
        print("You win!") 
    else: 
        print(f"Wrong! The number was {number}") 
    print(f"Time taken: {time.time() - start_time:.2f}s")

