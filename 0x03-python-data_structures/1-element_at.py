#!/usr/bin/python3

def element_at(my_list, idx):
    my_list = [my_list[idx] if idx >= 0 and len(my_list) > 0 else "None"]
    return my_list
