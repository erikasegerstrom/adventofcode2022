
raw = open('inputs/day1.txt').read()
elves = raw.split("\n\n")
elf_calories = []

for elf in elves:
    new_elf = elf.split('\n')
    elf_numbers = [int(n) for n in elf.split()]
    elf_calories.append(sum(elf_numbers))

print("Part 1: ", max(elf_calories))

elf_calories.sort(reverse=True)
print("Part 2: ", sum(elf_calories[0:3]))