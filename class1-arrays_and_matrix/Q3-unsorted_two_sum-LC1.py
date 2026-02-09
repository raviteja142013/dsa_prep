#find indices i,j where nums[i]+nums[j] = target, nums is an unsorted array

def two_sum(nums:list[int], target:int)-> tuple[int,int]:
    store = {}
    for idx,i in enumerate(nums):
        if target-i in store:
            return (idx,store[target-i])
        else:
            store[i]=idx
    return None

    # for idx,i in enumerate(nums):
    #     if store.get(target-i) !=None:
    #         return (idx,store[target-i])
    #     else:
    #         store[i]=idx
    # return None


print(two_sum([3,3],6))