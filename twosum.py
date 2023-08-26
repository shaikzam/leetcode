def two_sum(nums, target):
    num_to_index = {}  # Dictionary to store numbers and their indices
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    
    # If no solution is found, return an empty list or raise an exception
    return []
# changes
# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result) 