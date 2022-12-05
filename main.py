instructions_file = open("instructions.txt", "r")

instructions = instructions_file.readlines()

for i in range(len(instructions)):
    instructions[i] = instructions[i].replace("\n", "")

stacks = []

contents = [["P", "F", "M", "Q", "W", "G", "R", "T"], ["H", "F", "R"], ["P", "Z", "R", "V", "G", "H", "S", "D"],
            ["Q", "H", "P", "B", "F", "W", "G"], ["P", "S", "M", "J", "H"], ["M", "Z", "T", "H", "S", "R", "P", "L"],
            ["P", "T", "H", "N", "M", "L"], ["F", "D", "Q", "R"], ["D", "S", "C", "N", "L", "P", "H"]]

for i in range(9):
    stacks.append(contents[i])

instruction_sets = []

for instruction in instructions:

    # Initialise a variable to store each boundary of the ranges

    section = ""

    # Initialise lists for the boundaries of each range

    instruction_set = []

    # Iterate over the characters of each line

    for char in instruction:

        # Add each boundary to the range and then to the list of ranges

        try:
            int(char)
            section += char

        except ValueError:

            instruction_set.append(int(section))
            section = ""

    instruction_set.append(int(section))

    instruction_sets.append(instruction_set)

# Part 1

for instruction in instruction_sets:
    for i in range(int(instruction[0])):
        stacks[int(instruction[2]) - 1].append(stacks[int(instruction[1]) - 1].pop())

for i in range(9):
    print(stacks[i][-1])

print()

# Part 2

stacks = []

contents = [["P", "F", "M", "Q", "W", "G", "R", "T"], ["H", "F", "R"], ["P", "Z", "R", "V", "G", "H", "S", "D"],
            ["Q", "H", "P", "B", "F", "W", "G"], ["P", "S", "M", "J", "H"], ["M", "Z", "T", "H", "S", "R", "P", "L"],
            ["P", "T", "H", "N", "M", "L"], ["F", "D", "Q", "R"], ["D", "S", "C", "N", "L", "P", "H"]]

for i in range(9):
    stacks.append(contents[i])

for instruction in instruction_sets:
    stacks[int(instruction[2]) - 1].extend(stacks[int(instruction[1]) - 1][-int(instruction[0]):])
    for i in range(int(instruction[0])):
        stacks[int(instruction[1]) - 1].pop()

for i in range(9):
    print(stacks[i][-1])
