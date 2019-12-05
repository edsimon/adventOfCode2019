def solver(data, stdin):
    index_inc = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}
    program = data[:] # safe copy
    index = 0
    while not program[index] == 99:
        # pad with 0000 -> reverse -> take op_code -> take 3 first elements after op_code
        instr = ("0000" + str(program[index]))[::-1] # Pad for OOB and then reverse
        op_code = int(instr[0])
        modes = [int(i) for i in instr[2:5]]

        params = []
        for i in range(1, index_inc[op_code]):
            if modes[i-1] == 0:
                params.append(program[program[index+i]])
            else:
                params.append(program[index+i])

        if op_code == 1:
            program[program[index+3]] = params[0] + params[1]

        elif op_code == 2:
            program[program[index+3]] = params[0] * params[1]

        elif op_code == 3:
            program[program[index+1]] = stdin

        elif op_code == 4:
            if params[0] > 0:
                return params[0]
            print(params[0])

        elif op_code == 5:
            if params[0] != 0:
                index = params[1]
                continue

        elif op_code == 6:
            if params[0] == 0:
                index = params[1]
                continue

        elif op_code == 7:
            program[program[index+3]] = 1 if params[0] < params[1] else 0

        elif op_code == 8:
            program[program[index+3]] = 1 if params[0] == params[1] else 0

        index += index_inc[op_code]
    return params[0]


with open("../data/day05.txt") as f :
    data = list(map(int, f.readline().split(",")))
    print("the ID for the ship's air conditioner unit: {}\n"
          "Solution for the ship's thermal radiator controller is: {}"
          .format(solver(data, 1), solver(data, 5)))