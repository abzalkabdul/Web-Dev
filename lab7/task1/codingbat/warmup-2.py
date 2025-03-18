#1
def string_times(str, n):
  result = ""
  for i in range(n):
    result += str
  return result

#2
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]

  result = ""
  for _ in range(n):
    result += front
  return result

#3
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#4
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return result

#5
def last2(str):
  if len(str) < 2:
    return 0

  last2 = str[len(str)-2:]
  count = 0

  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count += 1

  return count

#6
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1

  return count

#7
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):
    if nums[i] == 9:
      return True
  return False

#8
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

#9
def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count += 1

  return count


