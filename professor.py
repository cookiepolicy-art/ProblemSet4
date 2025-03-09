# implement a program that:
#    Prompts the user for a level, n.
#      If the user does not input 1, 2, or 3, the program should prompt again. 
#    Randomly generates ten (10) math problems formatted as X + Y = ,
#      wherein each of X and Y is a non-negative integer with digits.  
#    Prompts the user to solve each of those problems. 
#      If an answer is not correct (or not even a number),
#         the program should output EEE and prompt the user again, allowing the user 
#           up to three tries in total for that problem. If the user has still not
#           answered correctly after three tries, the program should output the correct answer. 
#         The program should ultimately output the user’s score: the number of correct answers out of 10.
#    Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user or a level and returns 1, 2, or 3,
#       and generate_integer returns a randomly generated non-negative integer with level digits 
#        or raises a ValueError if level is not 1, 2, or 3: 
# import random
# 
# def main():
#     ... 
# def get_level():
#     ... 
# def generate_integer(level): 
#     ... 
# if __name__ == "__main__": 
#     main()
from random import randint

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = check_answer(x,y)
        if answer == None:
            break

#        score += check_answer(x,y)
        score += answer

        print(f"Score: {score}")

def check_answer(x,y):
    tries = 0
    while tries < 3:
        try:
#            print(f"tries is {tries}")
            tries += 1
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            pass
        except KeyboardInterrupt:  #ctrl-c caught (ctrl-d does not work in windows)
            print()  #needed to move cursor down one line (make screen look nice)
#            break
            return None
    print(f"{x} + {y} = {x+y}")
    return 0
    


# level = -1
# def main():
#     level = get_level()
# #    print(f"******level is {level}")
#     problem_correct_count= 0
#     for p in range(0,3):
#         print(f"p is {p}======")
#         x = generate_integer(level)
# #        print(f"x is {x}")
#         y = generate_integer(level)
# #        print(f"y is {y}")
#         answer = x + y
#         tries = 0
#         while tries <= 2:
#             try:
#                 tries += 1
#                 input_ans = int(input(f"{x} + {y} = "))
#                 print(f"tries is {tries}")
#             except ValueError:
#                 pass
#             else:
# #                print(f"ans is {input_ans}")
#                 if input_ans == answer:
#                     problem_correct_count += 1
#                     break # break out of while with correct answer
#                 else:
#                     print("EEE")
#                     break
#         print("outside while loop")
        
#         if not tries <= 2:
#             print(f"{x}+{y} = {x+y}")

#         print(f"p is {p}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass
        except KeyboardInterrupt:  #ctrl-c caught (ctrl-d does not work in windows)
            print()  #needed to move cursor down one line (make screen look nice)
            break
# def get_level():
#     while True:
#         level = int(input("Level: "))
#         if level != 1 and level != 2 and level != 3:
#             continue
#         else:
#             return level
            
def generate_integer(level):
    # print("generate_integer(level)")
    # print(f"the type of level is {type(level)}")
    if level == 1:
        return randint(0,9)
    else:
        try:
            start = 10**(level-1)
            end = 10**level -1
            return randint(start, end)
        except TypeError:
            print(f"level has type {type(level)}")    
#    return randint(10**(level-1),10**level -1)


# def generate_integer(lvl):
# #    print(f"==========level is {lvl}")
#     try: 
#         if lvl != 1 and lvl != 2 and  lvl != 3:
#             raise ValueError
#         else:
#             start = 10**(lvl - 1)
#             end = 10**lvl - 1
# #            print(f"^^^^^start is {start}, end is {end}")

#             return random.randint(start, end)    
#     except ValueError:
#         print("value error in generate_integer")
#         pass
    # else:
    #     if not isinstance(level, int) or level <= 0:
    #         raise ValueError
    #     start = 10**(level - 1)
    #     end = 10**level - 1
    #     return random.randint(start, end)
    

if __name__ == "__main__":
    main()