def get_ggf(numbers, log=False):
    numbers.sort()
    smol_num = numbers[0]
    div_num = smol_num
    good = 0
    for i in range(smol_num):
        for number in numbers:
            if i == 1 and number == numbers[0]:
                div_num = (div_num+1)/2
            if good == len(numbers):
                break
            if number % div_num == 0:
                if log == True: 
                    print(f"Trying {number} / {div_num} | DIVISABLE | number / div_num = {number / div_num}")
                good += 1
                good_number = div_num
            else:
                good = 0
                if log == True:
                    print(f"Trying {number} / {div_num} | NOT DIVISABLE | number / div_num = {number / div_num}")
                break
        div_num -= 1
    return good_number

if __name__ == "__main__":
    numbers = []
    try:
        for num in input(":: Input Number Sequence (Split with semicolon): ").split(";"): numbers.append(int(num)) 
    except: print("Incorrect data. Please double check your syntax and format."); quit()
    log = True
    print("Found number:", get_ggf(numbers))

