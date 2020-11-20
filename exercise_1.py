# exercise No 1
# Print all numbers <5 from inputed list

lst1 = []
lst_len = int(input('Input list length: '))
print('Input list elements:')
for i in range(0, lst_len):
    lst_elem = int(input())
    lst1.append(lst_elem)
print(lst1)

print('Elements from list < 5')
for lst_elem in lst1:
    if lst_elem < 5:
        print(lst_elem)


