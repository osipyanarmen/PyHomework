#primitive calculatur

def calculator(x: int, y: int, oper:str):
    if oper == '+':
        print(x+y)
    elif oper == '-':
        print(x-y)
    elif oper == '*':
        print(x*y)
    elif oper == '/':
        print(x/y)
    else:
        print('No such operand')


a = int(input('X = '))
b = int(input('Y = '))
operand = input('Choose operand (+, -, /, *): ')
print('X '+operand+' Y = ', end=' ')
calculator(a, b, operand)
