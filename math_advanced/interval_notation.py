from math import *

def Z(num):
    if type(num) == int: 
        return True
    else:
        return False
def N(num):
    if type(num) == int and num > 0:
        return True
    else:
        return False

def N0(num):
    if type(num) == int and num >= 0:
        return True
    else:
        return False
    
def R(num):
    if round(num, 12) == num:
        return True
    else:
        return False

def intervalNotation(numberline: str, max_negative=-20, max_positive=20):

    class result:
        answers = []
        pass_arg1 = []
        pass_arg2 = []
        
    numberline = numberline.replace("{", "").replace("}", "").replace(" ", "")

    variable, rest = numberline.split(":")

    arg1, rest = rest.split(variable, 1)

    arg2, rest = rest.split(";")

    numType = rest.replace(f"{variable}E", "")


    max_negative = abs(max_negative)
    for i in range(max_negative+max_positive):
        exec(f"""
if {arg1} i-max_negative:
    result.pass_arg1.append(i-max_negative)
    if i-max_negative {arg2}: 
        result.pass_arg2.append(i-max_negative)
        if {numType}(i-max_negative): 
            result.answers.append(i-max_negative)""")

    return result
        
        


if __name__ == "__main__":
    numbers = []
    numberline = input(":: Input Interval Notation: ") # {x: sqrt(3) >= x <= 4; x E R}
    print("Found possible numbers:", intervalNotation(numberline).answers)


