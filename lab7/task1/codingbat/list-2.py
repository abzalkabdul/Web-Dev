#1
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

#2
def big_diff(nums):
    return max(nums) - min(nums)

#3
def centered_average(nums):
    nums.sort()
    trimmed = nums[1:-1]
    return sum(trimmed) // len(trimmed)

#4
def sum13(nums):
    total = 0
    skip = False 

    for num in nums:
        if num == 13:
            skip = True  
            continue
        if skip:
            skip = False
            continue
        total += num 

    return total

#5
def sum67(nums):
    total = 0
    skip = False

    for num in nums:
        if num == 6:
            skip = True 
        if not skip:
            total += num  
        if num == 7 and skip:
            skip = False 

    return total

#6
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
