#1
name = input()
print(f'Hello {name}!')

#2
a, b = input(), input()
print(f"{a}{b}{b}{a}")

#3
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

#4 
def make_out_word(str):
    return f"<<{str}>>"

#5
def extra_end(s):
    return s[-2:] * 3

#6
def first_two(s):
    return s[:2]

#7
def first_half(s):
    return s[:len(s) // 2]

#8
def without_end(s):
    return s[1:-1]

#9
def combo_string(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

#10
def non_start(a, b):
    return a[1:] + b[1:]

#11
def left2(s):
    return s[2:] + s[:2]

