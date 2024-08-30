import random
def guess(x):
    random_num = random.randint(1,x)
    guess=0
    while random_num!=guess:
        guess=int(input(f"Enter a number between 1 and {x}:"))
        if(guess>random_num):
            print("It is too high")
        elif(guess<random_num):
            print("It is too low")
    print(f"Congrats! the number you have guessed {random_num} is correct")
guess(10)

