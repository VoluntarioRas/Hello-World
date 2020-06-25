#function for another calculation with the result

def again(total):
    while True:

        choice = input('\nDo you wanna realize one more operation with the result? ')
        
        if choice == 'yes' or choice == 'y' or choice == 'YES' or choice == 'Yes' or choice == 'Y':
            newnum = float(input('\nInsert the new number: '))
            rec = input('Wich operation do you wanna do (Sum = +, Subtration = -, Multiplication = x , Division = /) : ')

            if rec == '+':
                newtotal = total + newnum
                print(f'\n{total} {rec} {newnum} = {newtotal}')
                break

            if rec == '-':
                newtotal = total - newnum
                print(f'\n{total} {rec} {newnum} = {newtotal}')
                break
    
            if rec == 'x':
                newtotal = total * newnum
                print(f'\n{total} {rec} {newnum} = {newtotal}')
                break
            
            if rec == '/':
                newtotal = total / newnum
                print(f'\n{total} {rec} {newnum} = {newtotal}')
                break
        break
        if choice == 'no' or choice == 'n' or choice == 'NO' or choice == 'N': 
            break
                
        else:
            print('\nSorry, you need to respond just with yes or no.')

