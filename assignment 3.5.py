def sort_list_of_strings(lst):
    return sorted(lst, key=lambda s: s.lower())
lst = ['cat', 'apple', 'Dog', 'banana', 'Zebra']
print(sort_list_of_strings(lst))  # output: ['apple', 'banana', 'cat', 'Dog', 'Zebra']
