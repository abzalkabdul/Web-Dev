#1
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - min(big, goal // 5) * 5 <= small

#2
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

#3
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

#4
def fix_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n

#5
def round10(num):
    return (num + 5) // 10 * 10
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

#6
def close_far(a, b, c):
    def close(x, y): return abs(x - y) <= 1
    def far(x, y): return abs(x - y) >= 2

    return (close(a, b) and far(b, c) and far(a, c)) or (close(a, c) and far(c, b) and far(a, b))

#7
def make_chocolate(small, big, goal):
    max_big_bars = min(big, goal // 5)
    remaining = goal - max_big_bars * 5

    if remaining <= small:
        return remaining
    return -1
