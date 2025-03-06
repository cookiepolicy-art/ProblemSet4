# Because emoji aren’t quite as easy to type as text, at least on laptops and desktops,
#  some programs support “codes,” whereby you can type, for instance, :thumbs_up:, 
# which will be automatically converted to 👍. Some programs additionally support aliases,
#  whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically
#   converted to 👍. 
# See
#  carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
#  for a list of codes with aliases. Implement a program that prompts the user for a str
#  in English and then outputs the “emojized” version of that str, converting any codes (or aliases)
#   therein to their corresponding emoji.  
# 
# Had to install the 'emoji' package. Used: py -m pip install emoji 
# To see the emojis, this code had to be run inside VSCode,
#  using the 'Run, Run Without Debugging' option above.  
# How to test: 
# Type :1st_place_medal: and press Enter. 
#      Your program should output:  Output: 🥇  
# Type :money_bag: and press Enter. 
#      Your program should output: Output: 💰 T
# Type :smile_cat: and press Enter. 
#      Your program should output: Output: 😸

import emoji

def main():
    input_text = input("Input: ")
    cleaned_text = input_text.lstrip().rstrip()
    #print(f"Cleaned_text is - {cleaned_text}")

    print(f"Output: {emoji.emojize(cleaned_text, language='alias')}")


main()