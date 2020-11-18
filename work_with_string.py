# Count the symbols, count upper case and lower case in inputed text
txt = input('Input text: ')
txt_length = len(txt)
upper_case = 0
lower_case = 0
for symbol in txt:
    if symbol.isupper():
        upper_case += 1
    else:
        lower_case += 1
print('Your text contains ' + str(txt_length) + ' symbols')
print('Your text contains ' + str(upper_case) + ' upper case symbols')
print('Your text contains ' + str(lower_case) + ' lower case symbols')

# Reverse the inputed text and print
print('The reverse of your text is: ')
while txt_length != 0:
    print(txt[txt_length-1], end='')
    txt_length -= 1
print('\n')

# Print each word from text in new line
print('Each word from text on new line:')
for i in range(0, len(txt)):
    if txt[i] != ' ':
        print(txt[i], end='')
    else:
        print('')

