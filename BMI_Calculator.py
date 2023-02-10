import colorama
from colorama import Fore

weight = float(input("enter your currently weight(Kg) : "))
height = float(input("enter your currently height(m) : "))
 
BMI = weight / (height * height)

print(Fore.RED+"Skinny-3rd | "+Fore.YELLOW+"Skinny-2rd | Skinny-1rd"+Fore.GREEN+" | Normal | "+Fore.YELLOW+"Fat-1rd | Fat-2rd"+Fore.RED+" | Fat-3rd |")

if BMI < 15:
    print(Fore.RED+"     +     |")
elif 15 < BMI < 16:
    print(Fore.RED+"           |"+Fore.YELLOW+"     +      |")
elif 16 < BMI < 18.5:
    print(Fore.YELLOW+"                        |     +"+Fore.GREEN+"      |")  
elif 18.5 < BMI < 25:
    print(Fore.GREEN+"                                     |    +   |       "+Fore.WHITE)
elif 25 < BMI < 30:
    print(Fore.YELLOW+"                                              |    +    |   ")
elif 30 < BMI < 35:
    print("                                                        |    +    |   ")
elif BMI > 35 :
    print(Fore.RED+"                                                                  |    +     |")

i = 0

best_weight = (21.6 * (height * height)) - 3

if BMI < 18.5: 
    while BMI < 18.5:
        i = i + 1
        weight = weight + 1
        if weight >= best_weight :
            break
    print(Fore.WHITE+"Best weight for you is "+Fore.GREEN+""+str(weight)+" kg")
    print(Fore.WHITE+"You should gain "+Fore.GREEN+""+str(i)+" kg")

if BMI > 25: 
    while BMI > 25:
        i = i + 1
        weight = weight - 1
        if weight <= best_weight :
            break
    print(Fore.WHITE+"Best weight for you is "+Fore.GREEN+""+str(weight)+" kg")
    print(Fore.WHITE+"You should lose "+Fore.GREEN+""+str(i)+" kg")