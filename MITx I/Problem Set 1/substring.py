from itertools import count
def longeststring(string):
    m = string[0]
    for x in range(len(string)):
        for k in count(x + len(m) + 1):
            s = string[x:k]
            if len(s) != (k - x):
                break
            if sorted(s) == list(s):
                m = s
    return m
r = (longeststring(s))
print("Longest substring in abc order is: ", r)
