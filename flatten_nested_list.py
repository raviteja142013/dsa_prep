def flatten_nested_list(new_list: list) -> list :
    outlist = [ ]
    for i in new_list:
        if isinstance(i,list):
            outlist.extend(flatten_nested_list(i))
        else:
            outlist.append(i)
    return outlist   

nums = [5,5,6,[7,0,9],[1,2,3,[4,5]],8]
result = flatten_nested_list(nums)
print("Flattened list:", result)