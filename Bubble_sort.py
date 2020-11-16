def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range (len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True

lst_input = []
lst_len = int(input('Enter number of elements in list: '))
print('Enter elements of list:')
for i in range(0, lst_len):
    elem = int(input())
    lst_input.append(elem)
bubble_sort(lst_input)
print('This is the list sorted with bubble algorithm: ')
print(lst_input)
