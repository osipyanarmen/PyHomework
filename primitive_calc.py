#primitive calculatur

def calculator(x: int, y: int, oper:str):
    if oper == '+':
        print(x+y, '\n')
    elif oper == '-':
        print(x-y, '\n')
    elif oper == '*':
        print(x*y, '\n')
    elif oper == '/':
        print(x/y, '\n')
    else:
        print('No such operand')

a = int(input('X = '))
b = int(input('Y = '))
while True:
    print('Input the operator to make calculation,\n or input "N" for new values,\n or input "Q" to EXIT')

    operand = input('Choose operand (+, -, /, *): ')
    if operand in ['+', '-', '*']:
        print('X ' + operand + ' Y = ', end=' ')
        calculator(a, b, operand)
    elif operand == '/' and b == 0:
        print("You can't divide by 0, please input new value for Y")
        b = int(input('Y = '))
        print('X ' + operand + ' Y = ', end=' ')
        calculator(a, b, operand)
    elif operand.upper() == 'Q':
        break
    elif operand.upper() == 'N':
        a = int(input('X = '))
        b = int(input('Y = '))
    else:
        print('Wrong input \n')
        continue
