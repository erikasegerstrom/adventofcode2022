import sys

def contains_duplicate(substring: str) -> bool:
    x = filter(lambda x: substring.count(x) >= 2, substring)
    if len(list(x)) == 0:
        return False
    return True 


with open('inputs/day6.txt') as f:
    """
    Find first unique substring in slices of 4
    """
    raw = f.read()

    for i in range (0, len(raw)):
        #j = i + 4
        j = i + 14
        substring = raw[i:j]
        if not contains_duplicate(substring):
            print("Index = ", j)
            sys.exit()
        