from collections import defaultdict

def parse_input(input):
    return list(map(int, input.strip().split(",")))


class Amp:
    def __init__(self, program, input = []):
        self.memory = {}
        for i, b in enumerate(program):
            self.memory[i] = b
        self.input = input
        self.pc = 0
        self.offset = 0

    def get_address(self, mode, offset):
        if mode == 0:
            return self.memory[offset]
        elif mode == 1:
            return offset
        elif mode == 2:
            return self.memory[offset] + self.offset


    def get_parameters(self, num):
        modes = self.memory[self.pc] // 100
        params = []
        for i in range(0, num):
            m = modes % 10
            params.append(self.get_address(m, self.pc + i + 1))
            modes = modes // 10
        return params

    def run_until_complete(self, input=[]):
        result = []
        output = self.run_until_output(input)
        while output is not None:
            result.append(output)
            output = self.run_until_output()
        return result

    def run_until_output(self, input=[]):
        self.input.extend(input)
        while True:
            op_code = self.memory[self.pc] % 100
            if op_code == 1:
                params = self.get_parameters(3)
                self.memory[params[-1]] = self.memory[params[0]] + self.memory[params[1]]
                self.pc += len(params) + 1
            elif op_code == 2:
                params = self.get_parameters(3)
                self.memory[params[-1]] = self.memory[params[0]] * self.memory[params[1]]
                self.pc += len(params) + 1
            elif op_code == 3:
                params = self.get_parameters(1)
                self.memory[params[-1]] = self.input.pop(0)
                self.pc += len(params) + 1
            elif op_code == 4:
                params = self.get_parameters(1)
                self.pc += len(params) + 1
                return self.memory[params[0]]
            elif op_code == 5:
                params = self.get_parameters(2)
                if self.memory[params[0]]:
                    self.pc = self.memory[params[1]]
                else:
                    self.pc += len(params) + 1
            elif op_code == 6:
                params = self.get_parameters(2)
                if not self.memory[params[0]]:
                    self.pc = self.memory[params[1]]
                else:
                    self.pc += len(params) + 1
            elif op_code == 7:
                params = self.get_parameters(3)
                self.memory[params[-1]] = 1 if self.memory[params[0]] < self.memory[params[1]] else 0
                self.pc += len(params) + 1
            elif op_code == 8:
                params = self.get_parameters(3)
                self.memory[params[-1]] = 1 if self.memory[params[0]] == self.memory[params[1]] else 0
                self.pc += len(params) + 1
            elif op_code == 9:
                params = self.get_parameters(1)
                self.offset += self.memory[params[0]]
                self.pc += len(params) + 1
            elif op_code == 99:
                return None


def solve1(program):
    amp = Amp(program, [1])
    return amp.run_until_complete()


def solve2(program):
    amp = Amp(program, [2])
    return amp.run_until_complete()


if __name__ == "__main__":
    with open("../data/day09.txt") as f:
        input = f.read()
    program = parse_input(input)
    print("P1: {}".format(solve1(program)))
    print("P2: {}".format(solve2(program)))