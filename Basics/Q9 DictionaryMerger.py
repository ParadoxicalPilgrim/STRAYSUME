def dict_merge(dict1, dict2):
    hold = dict1.copy()
    
    for key, value in dict2.items():
        if key in hold:
            if type(hold[key]) is list:
                hold[key].append(value)
            else:
                hold[key] = [hold[key], value]
        else:
            hold[key] = value
            
    return hold

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b':5,'c': 3, 'd': 4}
merged_dict = dict_merge(dict1, dict2)
print("The merged dictionary is:", merged_dict)
