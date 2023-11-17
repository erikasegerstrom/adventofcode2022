class Stack():
    """
    Stack of crates
    """
    def __init__(self, id: int, crates: list) -> None:
        self.id = id
        self.crates = crates

    def add_crate(self, crate):
        self.crates.append(crate)

    def remove_crate(self):
        self.crates.pop()

    def return_top_crate(self):
        return self.crates[-1]
    
    def add_slice(self, added_crates):
        self.crates = self.crates + added_crates


def make_move(stacks: list[Stack], n_items: int, stack_from_id: int, stack_to_id: int) -> None:
    """
    Move crates, one by one, from one stack to another
    """
    for i in range (0, n_items): 
        stacks[stack_to_id].add_crate(stacks[stack_from_id].return_top_crate())
        stacks[stack_from_id].remove_crate()


def move_slice(stacks: list[Stack], n_items: int, stack_from_id: int, stack_to_id: int) -> None:
    """
    Move all crates at the same time, keeping the order
    """
    slice = stacks[stack_from_id].crates[-n_items:]
    stacks[stack_to_id].add_slice(slice)
    for i in range (0, n_items):
        stacks[stack_from_id].remove_crate()


"""TEST CRATES
stack_1 = Stack(id = 1, crates = ["Z", "N"])
stack_2 = Stack(id = 2, crates = ["M", "C", "D"])
stack_3 = Stack(id = 3, crates = ["P"])
stacks = [stack_1, stack_2, stack_3]
"""

stack_1 = Stack(id = 1, crates = ["W", "R", "F"])
stack_2 = Stack(id = 2, crates = ["T", "H", "M", "C", "D", "V", "W", "P"])
stack_3 = Stack(id = 3, crates = ["P", "M", "Z", "N", "L"])
stack_4 = Stack(id = 4, crates = ["J", "C", "H", "R"])
stack_5 = Stack(id = 5, crates = ["C", "P", "G", "H", "Q", "T", "B"])
stack_6 = Stack(id = 6, crates = ["G", "C", "W", "L", "F", "Z"])
stack_7 = Stack(id = 7, crates = ["W", "V", "L", "Q", "Z", "J", "G", "C"])
stack_8 = Stack(id = 8, crates = ["P", "N", "R", "F", "W", "T", "V", "C"])
stack_9 = Stack(id = 9, crates = ["J", "W", "H", "G", "R", "S", "V"])
stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]


with open('inputs/day5.txt') as f:
    """
    Run make_move and move_slice separately
    """
    raw = f.read()
    moves = raw.split("\n")
    for move in moves:
        rearrange = move.split(" ")
        n_items = int(rearrange[1])
        stack_from_id = int(rearrange[3])-1
        stack_to_id = int(rearrange[5])-1
        #make_move(stacks, n_items, stack_from_id, stack_to_id)
        move_slice(stacks, n_items, stack_from_id, stack_to_id)

for i in range (0, len(stacks)):
    """
    Print result
    """
    print(stacks[i].return_top_crate())