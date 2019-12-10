import math

def create_board(data):
    astroids = []
    for y, line in enumerate(data):
        for x, c in enumerate(line.strip()):
            if c == "#":
                astroids.append((x, y))
    return astroids


def dist(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


def get_best_radar(astroids):
    best_count = 0
    best_pos = None

    for pos in astroids:
        x, y = pos
        count = 0
        angles = {(ax, ay): math.atan2(ay - y, ax - x) for ax, ay in astroids}
        for a in astroids:
            for b in astroids:
                if angles[a] == angles[b] and dist(a, pos) > dist(b, pos):
                    break
            else:
                count += 1
        if count > best_count:
            best_count = count
            best_pos = pos

    return best_pos, best_count


def find_200_astroid(best_pos, astroids):
    laser_angle = math.degrees(math.atan2(-1, 0)) % 360
    angles = {(ax, ay): math.degrees(math.atan2(ay - best_pos[1], ax - best_pos[0])) % 360 for ax, ay in astroids}

    def min_dist_ast(pos):
        return ((angles[pos] - laser_angle) % 360) * 10000000 + dist(pos, best_pos)

    for i in range(200):
        pos = min(astroids, key=min_dist_ast)
        laser_angle = (angles[pos] + 0.001) % 360
        astroids.remove(pos)

    return pos


with open("../data/day10.txt") as f:
    data = create_board(f)
    best_pos, best_radar = get_best_radar(data)
    pos = find_200_astroid(best_pos, data)
    print("Best position is {} where we can hit {} astroids.\n"
          "With this position the 200th astroid shot down are at position {} and result of task is: {}"
          .format(best_pos, best_radar, pos, pos[0]*100 + pos[1]))
