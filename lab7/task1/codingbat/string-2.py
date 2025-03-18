#1
def double_char(s):
    return ''.join(c * 2 for c in s)

#2
def count_hi(s):
    return s.count("hi")

#3
def cat_dog(s):
    return s.count("cat") == s.count("dog")

#4
def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == "co" and s[i+3] == "e":
            count += 1
    return count

#5
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)

#6
def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i+3] == "xyz":
            if i == 0 or s[i-1] != ".":
                return True
    return False
