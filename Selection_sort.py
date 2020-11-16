def sorted_list(lst):
    for i in range(len(lst)):
        low_value_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[low_value_index]:
                low_value_index = j
            lst[i], lst[low_value_index] = lst[low_value_index], lst[i]

lst_input = []
lst_len = int(input('Enter number of elements in list: '))
print('Enter elements of list:')
for i in range(0, lst_len):
    elem = int(input())
    lst_input.append(elem)
sorted_list(lst_input)
print('This is the list sorted with sorted algorithm: ')
print(lst_input)
