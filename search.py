def index_of(target, lst):
    found_index = -1
    i = 0
    while i < len(lst) and found_index == -1:
        if lst[i] == target:
            found_index = i
        i += 1
    return found_index

def index_of_by_index(target, lst, start):
    found_index = -1
    i = start
    while i < len(lst) and found_index == -1:
        if lst[i] == target:
            found_index = i
        i += 1
    return found_index

def index_of_empty(lst):
    return index_of("", lst)
