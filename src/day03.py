filepath = "../data/day03.txt"

def get_path(data) :
    data = data.split(",")
    position = (0,0)
    path = [position]
    for dir in data:
        distance = int(dir[1:])
        if dir[0] == "L":
            for i in range(distance):
                position = (position[0] - 1, position[1])
                path.append(position)
        elif dir[0] == "U":
            for i in range(distance):
                position = (position[0], position[1] + 1)
                path.append(position)
        elif dir[0] == "R":
            for i in range(distance):
                position = (position[0] + 1, position[1])
                path.append(position)
        elif dir[0] == "D":
            for i in range(distance):
                position = (position[0], position[1] - 1)
                path.append(position)
    return(path)


def solver(path1,path2):
    crosses_at = list(set(path1).intersection(path2))[1:]
    shortest_dist, shortest_path = 99999, 99999

    for x,y in crosses_at:
        # For task 1
        if abs(x)+abs(y) < shortest_dist :
            shortest_dist = abs(x)+abs(y)

        # For task 2
        dist = path1.index((x,y)) + path2.index((x,y))
        if  dist < shortest_path:
            shortest_path = dist

    return (shortest_dist, shortest_path)


with open(filepath) as f:
    path1 = get_path(f.readline())
    path2 = get_path(f.readline())
    dist, pos = solver(path1, path2)
    print("Closest crossover with taxidistance is: {}\nShortest path to a crossover is {}".format(dist,pos))