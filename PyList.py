lst1 = []
lst2 = []
lst_sum = 0
elem_num = int(input('Enter the number of elements:  '))
print('Enter list elements')
for i in range(0, elem_num):
    elem = int(input())
    lst1.append(elem)
    lst_sum = lst_sum + elem
    if elem % 2 == 0:
        lst2.append(elem)
print('This is the full list')
print(lst1, '\n')
print('This is the enum numbers list')
print(lst2, '\n')
print('This is the sum of elements of main list')
print(lst_sum, '\n')
print('Thank you for testing this program !!!')
