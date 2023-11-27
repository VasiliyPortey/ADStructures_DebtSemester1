start_list = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 6, 7, 7, 8, 9, 9, 9]
finish_dictionary = {i:start_list.count(i) for i in start_list}
print(finish_dictionary)