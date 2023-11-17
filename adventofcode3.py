item_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_common_item(rucksack_content: str):
    """
    Find common item in two compartments = rucksack split in the middle
    """
    number_of_items = len(rucksack_content)
    items_per_compartment = int(number_of_items/2)
    compartment_1 = rucksack_content[0:items_per_compartment]
    compartment_2 = rucksack_content[items_per_compartment:number_of_items]
    common_items = []
    
    for i in range (0 , items_per_compartment):
        if compartment_1.count(compartment_2[i]) > 0: 
            common_items.append(compartment_2[i])
    if common_items != []:
        return list(set(common_items))

    return None

def find_common_badge(group_of_rucksacks: list):
    """
    Identify common item in rucksacks in groups of three
    """
    badge = []
    badge_tmp = []
    backpack_1 = group_of_rucksacks[0]
    backpack_2 = group_of_rucksacks[1]
    backpack_3 = group_of_rucksacks[2]

    # Check backpack 1 against backpack 2
    for i in range (0, len(backpack_1)):
        if backpack_2.count(backpack_1[i]) > 0:
            badge_tmp.append(backpack_1[i])

    # Check result against backpack 3
    for i in range (0, len(badge_tmp)):
        if backpack_3.count(badge_tmp[i]) > 0:
            badge.append(badge_tmp[i])
    
    return list(set(badge))

if __name__ == "__main__":
    with open("inputs/day3.txt") as f:
            priority_sum = 0
            inputs = [line.strip() for line in f]
            for input in inputs:
                items = find_common_item(input)
                if items != None:
                    for item in items:
                        priority_sum += item_list.find(item) +1
            print (priority_sum)
            
            start = 0
            inc = 3
            priority_sum_2 = 0
            for n_groups in range (0, int(len(inputs)/3)):
                start = n_groups * inc
                end = (n_groups + 1) * inc
                badge = find_common_badge(inputs[start: end])
                priority_sum_2 += item_list.find(badge[0]) +1
            print(priority_sum_2)
            