from math import sqrt

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


gettallelyn = r"{x: sqrt(3) >= x <= 4; x E R}"
gettallelyn = gettallelyn.replace("{", "").replace("}", "").replace(" ", "")

variable = gettallelyn.split(":")[0]
first_arg = gettallelyn.split(":")[1].split("x")[0]
second_arg = gettallelyn.split(":")[1].split("x")[1].split(";")[0]
num_type = gettallelyn.split(";")[-1].replace(f"{variable}E", "")

answers = []

for i in range(40):
    exec(f"""
if {first_arg} i-20 and i-20 {second_arg}: 
    if {num_type}(i-20): 
        answers.append(i-20)
    """)
        
        
print(answers)
