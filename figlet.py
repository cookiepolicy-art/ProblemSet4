# implement a program that: 
# Expects zero or two command-line arguments: 
#   Zero if the user would like to output text in a random font. 
#   Two if the user would like to output text in a specific font,
#      in which case the first of the two should be -f or --font,
#      and the second of the two should be the name of the font.  
#   Prompts the user for a str of text. 
#   Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or
#     the second is not the name of a font,
#     the program should exit via sys.exit with an error message.
#  I had to install the 'pyfiglet' package with pip: (py -m pip install pyfiglet) first

from pyfiglet import Figlet
#for access to command line:
import sys
import random

def main():
    figlet = Figlet()
    print("Loading figlet fonts, please wait...", end="")
    font_list = figlet.getFonts()
    print("done.")
    cl_params_dict = validate_commandline(font_list)
    if cl_params_dict == None:
        print("No cla provided")
    else:
        print(f"cl_params_dict is {cl_params_dict}")
        # figlet.setFont(font=cl_params_dict["font"])
        # print(figlet.renderText("Hello"))
#        render_text(figlet, font_list, cl_params_dict)
        print("Output: ")
        if cl_params_dict["font"] == -1:
            print("Render with random font")
            render_text_random_font(figlet, font_list)
        else:
            render_text(figlet, cl_params_dict)

def render_text_random_font(fglt,f_list):
    font_to_render_with = random.choice(f_list)
    print(f"font used is {font_to_render_with}")
    fglt.setFont(font=font_to_render_with)
    text = input("Input: ")
    print("Output: ")
    print(fglt.renderText(text))



def render_text(fglt, p_dict):
    fglt.setFont(font=p_dict["font"])
    text = input("Input: ")
#    print("Output: ")
    print(fglt.renderText(text))

#    if valid_commandline()
#    commandline_args_test()
    # Get past the commandline usage restrictions, then ask for the text to print:

def validate_commandline(f_list):
    param_dict = {}
    len_params = len(sys.argv)-1 #this is number of params provided
    print(f"len_params is {len_params}")
    # len_params is 2
    print(f"cla is {sys.argv[1:]}")
    # cla is ['-f', 'block']
    # if len_params == 1:
    #     #font_list = f.getFonts()
    #     print(f_list[:6])
    #     return None

    if len_params != 0 and len_params != 2:
        sys.exit("Not enough parameters: Usage is py figlet.py [[-f | --font] <font_name>]")
    elif len_params == 0: #render with random font
         param_dict["font"] = -1
         return param_dict
    
    elif len_params == 2:
        cla = sys.argv[1:]
        print(f"first cla is {cla[0]}")
        # first cla is -f
        # first cla is --font
        if cla[0] == '-f' or cla[0] == '--font':
            if cla[1] in f_list:
                print(f"2nd cla is {cla[1]}")
                param_dict["font"] = cla[1]
                return param_dict
            else:
                sys.exit(f"font '{cla[1]}' not in available list.")
        else:
            sys.exit("Invalid input")
        # elif cla[0] == '--v':
        #     #font_list = f.getFonts()
        #     print(font_list[:6])
        #     return None
        

        #return param_dict


def commandline_args_test():
    #see how 'sys.argv' provides cmd line args
    #I used 'py figlet.py 3 32 1'
    print(sys.argv)
    #['figlet.py', '3', '32', '1']
    # 'sys.argv' is a list starting with the program name, followed by any program args.
    len_cla = len(sys.argv)
    print(f"Length of 'sys.argv' is = {len_cla}")
    # Length of 'sys.argv' is = 4
    print(f"There are {len_cla-1} provided parameters.")
    # There are 3 provided parameters.
    params = sys.argv[1:]
    print(f"  which are {params}")
    #   which are ['3', '32', '1']



main()