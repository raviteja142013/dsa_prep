# given a sorted array [-3,-2,-1,2,9,11] and a target 7, return the indices of elements that make up the target

def sorted_two_sum(nums:list[int], target:int)-> tuple[int,int]:
    n = len(nums)
    l=0
    r = n-1
    while(l<r):
        if(target == nums[l]+nums[r]):
            return (l,r)
        elif(target > nums[l]+nums[r]):
            l+=1
        else:
            r-=1
    return None



print(sorted_two_sum([-3,-2,-1,2,9,11],7))
