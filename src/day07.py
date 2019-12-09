import itertools

def parse_input(input: str):
    return list(map(int, input.split(",")))


def get_parameters(memory, pc, modes, num):
    params = []
    for i in range(0, num):
        m = modes % 10
        modes = modes // 10
        if m == 0:
            params.append(memory[memory[pc + 1 + i]])
        elif m == 1:
            params.append(memory[pc + 1 + i])
        else:
            raise ValueError("Bad param mode: {} pc: {}".format(m, pc))
    return params


class Amp:
    def __init__(self, program, input):
        self.memory = program.copy()
        self.pc = 0
        self.input = input

    def run_until_output(self, input=[]):
        self.input.extend(input)
        while True:
            op_code = self.memory[self.pc] % 100
            if op_code == 1:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 2)
                self.memory[self.memory[self.pc + 3]] = params[0] + params[1]
                self.pc += 4
            elif op_code == 2:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 2)
                self.memory[self.memory[self.pc + 3]] = params[0] * params[1]
                self.pc += 4
            elif op_code == 3:
                self.memory[self.memory[self.pc + 1]] = self.input.pop(0)
                self.pc += 2
            elif op_code == 4:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 1)
                self.pc += 2
                return params[0]
            elif op_code == 5:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 2)
                if params[0]:
                    self.pc = params[1]
                else:
                    self.pc += 3
            elif op_code == 6:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 2)
                if not params[0]:
                    self.pc = params[1]
                else:
                    self.pc += 3
            elif op_code == 7:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 3)
                self.memory[self.memory[self.pc + 3]] = 1 if params[0] < params[1] else 0
                self.pc += 4
            elif op_code == 8:
                params = get_parameters(self.memory, self.pc, self.memory[self.pc] // 100, 3)
                self.memory[self.memory[self.pc + 3]] = 1 if params[0] == params[1] else 0
                self.pc += 4
            elif op_code == 99:
                return None
            else:
                raise ValueError("Unknown op_code: {} at {}".format(op_code, self.pc))


def calculate_output1(program, phase_settings):
    output = 0
    for p in phase_settings:
        amp = Amp(program, [p, output])
        output = amp.run_until_output()
    return output


def solve1(program):
    highest_output = None
    base_phase_settings = list(range(5))
    for phase_settings in itertools.permutations(base_phase_settings):
        output = calculate_output1(program, phase_settings)
        if highest_output is None or output > highest_output:
            highest_output = output
    return highest_output


def calculate_output2(program, phase_settings):
    output = 0
    amps = [Amp(program, [p]) for p in phase_settings]
    while True:
        for amp in amps:
            output_or_none = amp.run_until_output([output])
            if output_or_none is None:
                return output
            output = output_or_none


def solve2(program):
    highest_output = None
    base_phase_settings = list(range(5, 10))
    for phase_settings in itertools.permutations(base_phase_settings):
        output = calculate_output2(program, phase_settings)
        if highest_output is None or output > highest_output:
            highest_output = output
    return highest_output


if __name__ == "__main__":
    with open("../data/day07.txt") as f:
        input = f.read()
    program = parse_input(input)
    print("P1: {}".format(solve1(program)))
    print("P2: {}".format(solve2(program)))