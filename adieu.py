# implement a program that prompts the user for names, one per line,
#  until the user inputs control-d. Assume that the user will input at least one name.
#  Then bid adieu to those names, separating two names with one and,
#  three names with two commas and one and, and names with commas and one and, as in the below: 
#     Adieu, adieu, to Liesl 
#     Adieu, adieu, to Liesl and Friedrich
#     Adieu, adieu, to Liesl, Friedrich, and Louisa 
#     Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt 
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
#  So basically it seems there are two special cases and then the most generic case:
#   Special case 1: Just one name - just print "Adieu, adieu to <name>"
#   Special case 2: Two names: - separate the two names with an 'and'
#   General case:  3 or more names - end all the names with a 'comma', (except the last one)
#       then display 'and' then display the last <name>

# Don't really understand why I need the 'inflect' package.
#  Because of its 'join' method, which does exactly what this problem asks for!
import inflect

names_list = []
p = inflect.engine()

def main():
    while True:
        try:
            name = input("Name: ")
            names_list.append(name)

        except KeyboardInterrupt:
            print()
            break

    print(f"Adieu, adieu, {p.join(names_list)}")

    


main()