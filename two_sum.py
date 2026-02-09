# def two_sum(nums, target):
#     """
#     Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

#     Args:
#     nums (List[int]): List of integers.
#     target (int): The target sum.

#     Returns:
#     List[int]: Indices of the two numbers that add up to `target`.
#     """
#     numToIndex = {}
#     for i,num in enumerate(nums):
#         complement = target - num
#         if complement in numToIndex:
#             return [numToIndex[complement],i]
#         numToIndex[num] = i
#         return []
    
# nums_input = input("Enter numbers separated by spaces: ")
# target_input = input("Enter target value: ")

# # Convert inputs
# nums = list(map(int, nums_input.strip().split()))
# target = int(target_input.strip())

# # Call and print result
# result = two_sum(nums, target)
# print("Indices of two numbers:", result)
