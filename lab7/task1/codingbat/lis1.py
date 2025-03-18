#1
def first_last6(lst):
    return (lst[0]==6 or lst[-1]==6)

#2
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

#3
def make_pi():
    return [3,1,4]

#4
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

#5
def sum3(lst):
    return sum(lst)

#6
def rotate_left3(nums):
    return nums[1:] + nums[:1]

#7
def reverse3(nums):
    return nums[::-1]

#8
def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    return [max_value] * 3

#9
def sum2(nums):
    return sum(nums[:2]) if nums else 0

#10
def middle_way(a, b):
    return [a[1], b[1]]

#11
def make_ends(nums):
    return [nums[0], nums[-1]]

#12
def has23(nums):
    return 2 in nums or 3 in nums

