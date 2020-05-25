print('\n--- Calculator ---')

while True:
    
    print("\nUnfortunelly we just can calculate two numbers for time.\n")
   
    exc = input('Insert two real numbers for the calculus: ').split(' ')
    num1 = float(exc[0])
    num2 = float(exc[1])
    
    rec = input('Wich operation do you wanna do (Sum = +, Subtration = -, Multiplication = x , Division = /) : ')
    
    if rec == '+':
        total = num1 + num2
        print(f'\n{num1} {rec} {num2} = {total}')

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
            if choice == 'no' or choice == 'n' or choice == 'NO' or choice == 'N': break
                
            else:
                print('\nSorry, you need to respond just with yes or no.')
   
    if rec == '-':
        total = num1 - num2
        print(f'\n{num1} {rec} {num2} = {total}') 
        
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
            if choice == 'no' or choice == 'n' or choice == 'NO' or choice == 'N': break
                
            else:
                print('\nSorry, you need to respond just with yes or no.')              

    if rec == 'x':
        total = num1 * num2
        print(f'\n{num1} {rec} {num2} = {total}')
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
            if choice == 'no' or choice == 'n' or choice == 'NO' or choice == 'N': break

            else:
                print('\nSorry, you need to respond just with yes or no.')

    
    if rec == '/':
        total = num1 / num2
        print(f'\n{num1} {rec} {num2} = {total}')
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
            if choice == 'no' or choice == 'n' or choice == 'NO' or choice == 'N': break
                
            else:
                print('\nSorry, you need to respond just with yes or no.')

    cho = input('\nDo you wanna realize another calculus? ')
 
    if cho == 'yes' or cho == 'y' or cho == 'YES' or cho == 'Y':
        pass
    else:
        break

print('\nThank you! Hope see you next time')




        


    
