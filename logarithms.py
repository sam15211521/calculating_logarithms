import math
from time import sleep
import os

#here are the variables 
global_number = 0
golbal_base_number = 0
global_exponent = 0
global_lower_bound = 1
global_upper_bound = 10

log_of_lower_bound = 0
log_of_upper_bound = 1

current_best_log_of_number = (log_of_lower_bound + log_of_upper_bound)/2





#here is a dict of previous calculated logarithms
# [number : log(number)]

dict_of_logarithms = []



            
# Here are the functions

def Error_not_a_number():
    os.system('cls')
    print("""\n____________________________\nERROR: Not a number
_____________________""")

def Error_Not_available():
    os.system('cls')
    print("""\n____________________________\nERROR: Choice not available yet
\n____________________________""")

def Error_Not_a_choice():
    os.system('cls')
    print("""\n____________________________\nERROR: Not a choice
\n____________________________""")





def already_have_number_check():
    global global_number

    if global_number != 0:
        while True:
            os.system("cls")
            flag = input(f""""You already have a number : {global_number}
Do you want to continue? y/n  \n""")
            if flag.lower() == 'y':
                return True
            elif flag.lower() == 'n':
                return False
            else:
                Error_Not_a_choice()

 

def gather_number(optional_text=''):
#This function is used to input a number and check for the number to be an 
#integer
    while True:
        number = input(f"\nplease input a number {optional_text}:\n")
        return_number = 0
        try:
            return_number = int(number)
            sleep(.333)
            os.system("cls")
            return return_number
        except:
            try:
                return_number = float(number)
                sleep(.333)
                os.system("cls")
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

def calculating_logarithm_itterations_UI():
    global global_number
    global global_base_number
    global global_exponent 
    global global_lower_bound
    global global_upper_bound
    global log_of_lower_bound
    global log_of_upper_bound
    global current_best_log_of_number

    working_number_tupal = convert_to_ones(global_number)

    global_base_number = working_number_tupal[0]
    global_exponent = working_number_tupal[1]

    calculating_logarithm_itterations_flag_string = (
f"""\n____________________________\n 

your number is:             the value of your number is:

{global_number}                               {global_base_number}

the logarithm of this number is:

log({global_base_number}) + {global_exponent} = {current_best_log_of_number + 1}

The logarithm of this number is found between:

{log_of_lower_bound} < {current_best_log_of_number} < {log_of_upper_bound}

the value of the base base number is between:

{global_lower_bound} < {global_base_number} < {global_upper_bound}

how do you want to procede? 
1) undergo one itteration
2) undergo two itterations
3) undergo five itterations
4) undergo ten itterations
0) Exit my number is close enough
__________________________________
""")
    calculating_logarithm_itterations_flag = input(
                                calculating_logarithm_itterations_flag_string)
    if calculating_logarithm_itterations_flag == "1":
        pass
    elif calculating_logarithm_itterations_flag == "2":
        pass
    elif calculating_logarithm_itterations_flag == "3":
        pass
    elif calculating_logarithm_itterations_flag == "4":
        pass
    elif calculating_logarithm_itterations_flag == "0":
        os.system("cls")
        return

    else:
        Error_Not_a_choice()



def calculating_square_roots_UI():
    pass




def calculating_logarithms_UI():

    global global_number


   
    cal_log_UI_choice_string = (
"""
_____________________

Please coose an option
1) Choose a number
2) Begin calculations
0) Exit
""")
    while True:
        if global_number != 0:
            print(f"\n\nnumber you are looking at:    {global_number}")

        cal_log_UI_choice = input(cal_log_UI_choice_string)
        if cal_log_UI_choice == "1":
            number_check_flag = already_have_number_check()
            if number_check_flag is True:
                global_number = gather_number()
                os.system("cls")
            elif number_check_flag is False:
                os.system("cls")
                continue
            else:
                os.system("cls")
                global_number = gather_number()
                os.system("cls")

        elif cal_log_UI_choice == "2":
            if global_number != 0:
                os.system("cls")
                calculating_logarithm_itterations_UI()
            else: 
                os.system("cls")
                print("\n\nplease choose a number first\n\n")

        elif cal_log_UI_choice == "0":
            os.system("cls")
            return
        else:
            os.system("cls")
            Error_Not_a_choice()


def User_Interface():
    os.system("cls")
    global global_number
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
        if global_number != 0:
            print(f"\n\nnumber you are looking at:    {global_number}")
            print(
f"\n\nThe current best log of your nunber is:   {current_best_log_of_number}")
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
            os.system("cls")
            Error_Not_available()
        else:
            os.system("cls")
            Error_Not_a_choice()
            continue



#program starts here

User_Interface()
#print(calculating_square_roots(number=35, aproximation=gather_number(
#            f"""\nA number closer to the real value will be fastest""")))
