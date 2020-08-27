from random import randint
from time import sleep

while True:

    number = randint(0, 10)
    
    print("\033[0;33m=-\033[m" * 30)
    print("\033[0;36mI am thinking in a number between 0 and 10...\033[m")
    print("\033[0;33m=-\033[m" * 30)  
    number_guess = int(input("\033[0;36mGuess the number that i am thinking now:\033[m "))

    sleep(2)
    print("\n\033[31;47mPROCESSING...\033[m\n")
    sleep(2)
    
    if number_guess == number:
        print("\033[0;36mYou did it!! Congratulations!!!\033[m")
    else:
        print(f"\033[0;36mSorry, it's wrong, i was thinking in the number {number}.\nMaybe next time!\n\033[m")

    choice = input("\033[0;36mDo you want to try again?(y/n): \033[m")
    no = ['No', 'no', 'n', 'N', 'NO', 'nO']

    if choice in no:
        break
    else:
        print()

sleep(1)
print("\033[0;36mThanks for playing!\033[m")
