filepath = "../data/day2.txt"

def solver(noun=12, verb=2):
    with open(filepath) as f:
        program = list(map(int, f.readline().split(",")))

        # 1202 fire alarm
        program[1] = noun
        program[2] = verb

        index = 0
        while not program[index] == 99 :
            opcode = program[index]

            one = program[program[index + 1]]
            two = program[program[index + 2]]
            pos = program[index + 3]

            program[pos] = one + two if opcode == 1 else one * two
            index += 4

    return program[0]


def solve_b():
    for noun in range(100) :
        for verb in range(100) :
            if (solver(noun, verb) == 19690720) :
                return 100*noun + verb


with open(filepath) as f :
    data = list(map(int, f.readline().split(",")))
    print("First task gives: {}\nSecond task gives: {}".format(solver(),solve_b()))