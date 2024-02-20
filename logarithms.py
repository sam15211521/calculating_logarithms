import math
from time import sleep




#here is a dict of previous calculated logarithms
# [number : log(number)]

dict_of_logarithms = []

#This function is the User Interface


            
# Here are the functions

def gather_number():
#This function is used to input a number and check for the nubmer to be an integer
    while True:
        number = input(f"please input a number: ")
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

def calculating_square_roots(number):
    return round(math.sqrt(number),len(str(number)))


# Here are the User Interfaces

def calculating_logarithms_UI():
    while True:
        cal_log_UI_choice = input("Please choose an option")
        if cal_log_UI_choice == 1
            pass
        elif cal_log_UI_choice == 2
            pass
        else:
            print("Error, choice invalad")


def User_Interface():
    number = 0
    base_number = 0
    exponent = 0
    lower_bound = 0
    upper_bound = 0

    log_of_lower_bound = 0
    log_of_upper_bound = 0

    print("""\n\n\nWelcome to Logarithm Calculator: 
Please use the following menu to calcuate a logarithm.\n\n\n""")

    root_menu_string = (
"""enter the number corisponding with you choice
1) choose a number

""")
    while True:
        root_menu_choice = input(root_menu_string)
        if root_menu_string == 0:
            print("good bye")
            exit()
        if root_menu_string == 1:
            calculating_logarithms_UI()
        else:
            continue



#program starts here

User_Interface()
