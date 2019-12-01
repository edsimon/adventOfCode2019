filepath = "../data/day1.txt"

def calc_fuel(mass):
    return int((mass/3)-2)

def read_file(filepath):
    first_sum, second_sum = 0, 0
    with open(filepath) as f:
        line = int(f.readline())
        while line:

            # Calculate the first part of the task
            first_sum += calc_fuel(line)

            # Calculate the second part of the task
            fuel = calc_fuel(line)
            temp_sum = 0
            while fuel > 0:
                second_sum += fuel
                fuel = calc_fuel(fuel)

            # Takes a new line and handles the empty string
            line = f.readline()
            line = 0 if line == "" else int(line)


    print("Sum of the first problem is {}\nSecond problem gives {}".format(first_sum, second_sum))


read_file(filepath)