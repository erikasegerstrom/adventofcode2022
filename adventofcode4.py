def make_pair_ranges(pairs) -> list:
    """
    Split input into int list
    """
    split_pairs = pairs.split(",")
    range_1 = split_pairs[0].split("-")
    range_2 = split_pairs[1].split("-")
    pair_ranges = [int(range_1[0]), int(range_1[1]), int(range_2[0]), int(range_2[1])]

    return pair_ranges

def does_contain(pair: list) -> bool:
    """
    Check if pair of ranges contains each other
    """
    if (pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[2] >= pair[0] and pair[3] <= pair[1]):
        return True
    return False

def does_overlap(pair: list) -> bool:
    """
    Check if pair of ranges overlap
    """
    if max(pair[0], pair[2]) <= min(pair[1], pair[3]):
        return True
    return False

with open('inputs/day4.txt') as f:
    raw = f.read()
    n_contains = 0
    n_overlaps = 0
    for pairs in raw.splitlines():
        pair_ranges = make_pair_ranges(pairs)
        if does_contain(pair_ranges): 
            n_contains += 1
        if does_overlap(pair_ranges): 
            n_overlaps += 1

print(n_contains)
print(n_overlaps)