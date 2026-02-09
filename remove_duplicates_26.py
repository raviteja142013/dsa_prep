# given a sorted array containing duplicates, remove duplicates and retutn list as:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def remove_dupes(x: list[int]):
    length = len(x)
    p = set(x)
    out_list =[]
    out_list.extend(p)
    for i in range(length - len(p)):
        out_list.append("_")
    return out_list

print(remove_dupes([0,0,1,1,1,2,2,3,3,4]))

