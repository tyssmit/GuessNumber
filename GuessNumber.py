import random
#import random class

rand_int=random.randint(1,20)
#testing random integer 
print (rand_int)

while(True):
    print("Guess a number between 1 & 20")
    print("Hint it is a whole number")
    print("-------------------------")

    try:
        user=int(input())
        #user input for guessed number
    except ValueError:
        print("that was not a number try again")
        continue
    #error handeling for non ints

    print("")
    if(user==rand_int):
        print("winner winner chicken dinner")
        print("To play again press Y if not press anything else")
        choice=input()
        #users choice to play again
        if(choice=='y' or choice=='Y'):
            print("")
            print("Awesome lets play again!")
            print("")
            continue
        else:
            print("Thank you for playing!")
            break
    else:
        print("")
        print("that is not correct try again")
        print("")
        continue

