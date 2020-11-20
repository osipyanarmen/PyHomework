# print common elements from two lists

lst1 = []
lst2 = []
lst12_len = int(input('Input length of lists: '))
print('Input elements of list1: ')
for elem1 in range(0, lst12_len):
    lst1.append(int(input()))
print('Input elements of list2')
for elem2 in range(0, lst12_len):
    lst2.append(int(input()))

result_lst = list(filter(lambda elem: elem in lst1, lst2))
print('This is the result list:')
print(result_lst)
