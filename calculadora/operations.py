#fuctions of the operations 
import again_fuction as af

def operation(rec, num1, num2):
    
    if rec == '+':
        total = num1 + num2
        print(f'\n{num1} {rec} {num2} = {total}')

        af.again(total)

    if rec == '-':
        total = num1 - num2
        print(f'\n{num1} {rec} {num2} = {total}')

        af.again(total)

    if rec == 'x':
        total = num1 * num2
        print(f'\n{num1} {rec} {num2} = {total}')

        af.again(total)

    if rec == '/':
        total = num1 / num2
        print(f'\n{num1} {rec} {num2} = {total}')


