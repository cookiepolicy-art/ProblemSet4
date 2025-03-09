#  implement a program that: 
#    Prompts the user for a level, .
#       If the user does not input a positive integer, the program should prompt again.  
#    Randomly generates an integer between 1 and , inclusive, using the random module.
#    Prompts the user to guess that integer. 
#      If the guess is not a positive integer, the program should prompt the user again. 
#     If the guess is larger than that integer, the program should output Too large!
#        and prompt the user again. 
#     If the guess is the same as that integer, the program should output Just right! and exit.
import random

level = -1
while True:
    level_input = input("Level: ")
    try:
        level = int(level_input)
    except ValueError:
        #apparently ... is a valid statement, the same as 'pass'
        pass
    except KeyboardInterrupt:  #ctrl-c caught (ctrl-d does not work in windows)
        print()  #needed to move cursor down one line (make screen look nice)
        break
    else:
        break
#print(f"level is {level}")
answer = random.randint(1,level)
#print(f"guess anwer is {answer}")
guess_level = -1 #need this to be able to test 'guess_level' in try block.
while True:
    try:
        guess_level = int(input("Guess: "))
        if guess_level <=0:
            raise ValueError

    except ValueError:
        if guess_level <= 0:
#            print("your guess must be positive")
            pass
    except KeyboardInterrupt:  #ctrl-c caught (ctrl-d does not work in windows)
        print()  #needed to move cursor down one line (make things look pretty)
        break

    else:
        if answer > guess_level:
            print("Too small.")
        elif answer < guess_level:
            print("Too large.")
        else:
            print("Just right!")
            break
