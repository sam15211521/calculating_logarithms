import math
from time import sleep
import os

#here are the variables 
global_number = 0
golbal_base_number = 0
global_exponent = 0
global_lower_bound = 0
global_upper_bound = 0

log_of_lower_bound = 0
log_of_upper_bound = 0




#here is a dict of previous calculated logarithms
# [number : log(number)]

dict_of_logarithms = []



            
# Here are the functions

def Error_Not_available():
    print("""\n____________________________\nERROR: Choice not available yet
\n____________________________""")
    os.system('cls')

def gather_number(optional_text=''):
#This function is used to input a number and check for the number to be an 
#integer
    while True:
        number = input(f"please input a number {optional_text}:\n")
        return_number = 0
        try:
            return_number = int(number)
            sleep(.333)
            return return_number
        except:
            try:
                return_number = float(number)
                sleep(.333)
                return round(return_number,len(number)-1)
            except:
                print("\n\n\n Error: not a number\n")

def convert_to_ones(number):
    exponent = 0
    return_number = number
    while return_number < 1 or return_number > 10:
        if return_number < 1:
            return_number = return_number * 10
            exponent += -1
        elif return_number > 10 :
            return_number = return_number / 10 
            exponent += 1
    return_number = round(return_number, len(str(number)) )
    return return_number, exponent

def calculating_square_roots(number, aproximation):
    new_aproximation = (aproximation + number/aproximation) / 2
    return number, round(new_aproximation, len(str(number))+5)




# Here are the User Interfaces

def calculating_logarithms_UI():

    global global_number


    if global_number != 0:
        print(f"number you are looking at:    {global_number}")
    
    cal_log_UI_choice_string = (
"""
_____________________

Please coose an option
1) choose a number
2)
0) Exit
""")
    while True:
        cal_log_UI_choice = input(cal_log_UI_choice_string)
        if cal_log_UI_choice == "1":
            global_number = gather_number()

        elif cal_log_UI_choice == "2":
            pass
        elif cal_log_UI_choice == "0":
            os.system("cls")
            return
        else:
            print("Error, choice invalad")


def User_Interface():
    os.system("cls")

    print("""\n\n\nWelcome to Logarithm Calculator: 
Please use the following menu to calcuate a logarithm.\n\n\n""")
    sleep(1.5)

    root_menu_string = (
"""enter the number corisponding with you choice

1) Begin logarithm calculation

2) View current logarithm calculation 

0) Exit

""")
    while True:
        print("""\n\n _____________________\n\nMain Menu\n\n""")
        root_menu_choice = input(root_menu_string)
        if root_menu_choice == "0":
            print("good bye")
            os.system("cls")
            exit()
        elif root_menu_choice == "1":
            os.system("cls")
            calculating_logarithms_UI()

        elif root_menu_choice == "2":
            Error_Not_available()
        else:
            continue



#program starts here

User_Interface()
#print(calculating_square_roots(number=35, aproximation=gather_number(
#            f"""\nA number closer to the real value will be fastest""")))
