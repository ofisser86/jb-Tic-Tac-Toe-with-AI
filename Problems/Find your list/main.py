def find_my_list(all_lists_, my_list):
    for index_, lst in enumerate(all_lists_):
        # Change the next line
        if id(lst) == id(my_list):
            return index_
    return None
