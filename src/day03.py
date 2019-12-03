import operator

def get_path(data) :
    steps = {"L": (-1, 0), "R": ( 1, 0), "U": ( 0, 1), "D": ( 0,-1)}
    position = (0,0)
    path = [position]
    for dir in data.split(","):
        for i in range(int(dir[1:])):
            position = tuple(map(operator.add, position, steps.get(dir[0])))
            path.append(position)
    return path

def solver(path1,path2):
    crosses_at = list(set(path1).intersection(path2))[1:]
    shortest_dist, shortest_path = 99999, 99999
    for x,y in crosses_at:
        # For task 1
        if abs(x)+abs(y) < shortest_dist :
            shortest_dist = abs(x)+abs(y)

        # For task 2
        dist = path1.index((x,y)) + path2.index((x,y))
        shortest_path = dist if dist < shortest_path else shortest_path
    return (shortest_dist, shortest_path)

with open("../data/day03.txt") as f:
    path1 = get_path(f.readline())
    path2 = get_path(f.readline())
    dist, pos = solver(path1, path2)
    print("Closest crossover with taxidistance is: {}\nShortest path to a crossover is {}".format(dist,pos))