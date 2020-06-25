import operations as op

print('\n--- Calculator ---')

while True:
    
    print("\nUnfortunelly we just can calculate two numbers for time.\n")
   
    exc = input('Insert two real numbers for the calculus: ').split(' ')
    num1 = float(exc[0])
    num2 = float(exc[1])
    
    rec = input('Wich operation do you wanna do (Sum = +, Subtration = -, Multiplication = x , Division = /) : ')
      
    op.operation(rec, num1, num2)
    
    cho = input('\nDo you wanna realize another calculus? ')
    if cho == 'yes' or cho == 'y' or cho == 'YES' or cho == 'Y':
        pass
    else:
        break

print('\nThank you! Hope see you next time')




        


    
