x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
print(' 1.+\n', '2.-\n', '3./\n', '4.*')
ch_operator = int(input('Choose what you want to do: '))
if ch_operator == 1:
    print('X + Y = ', x+y)
elif ch_operator == 2:
    print('X - Y = ', x-y)
elif ch_operator == 3:
    print('X / y = ', x/y)
elif ch_operator == 4:
    print('X * Y = ', x*y)
