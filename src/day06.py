# 42
import itertools
dic = {}

test = ["COM)B","B)C","C)D","D)E","E)F","B)G"
    ,"G)H","D)I","E)J","J)K","K)L"]

test2 = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H"
    ,"D)I","E)J","J)K","K)L","K)YOU","I)SAN"]

total = 0

def create_dic(data):
    dic = {}
    for str in data:
        key, value = str.split(")")
        if not dic.get(key) == None:
            dic.get(key).append(value)
        else:
            dic[key] = [value]
    return dic

def start(data):
    dic = create_dic(data)
    tot_unique = list(itertools.chain(*list(dic.values())))
    planets = dic.get("COM")
    rekt(dic, planets, 0, tot_unique, set())


def rekt(dic, planets, count, tot_unique, settis):
    count += 1

    if (planets == None and len(settis) == tot_unique):
        return 0

    elif (planets != None):
        for planet in planets:
            global total
            total += count
            settis.add(planet)
            if planet != None :
                rekt(dic, dic.get(planet), count, tot_unique, settis)

    else :
        return 0



you = []
san = []
def start2(data):
    global dic
    dic = create_dic(data[:])
    planet = "COM"
    loop("YOU", planet, dic, [])
    loop("SAN", planet, dic, [])
    print(get_dist())


def loop(person, planet, dic, li):
    global you
    global san
    run = True
    while run:
        if planet == person:
            #li.append(planet)
            if person == "YOU":
                you = li
            else:
                san = li
            #print(li)
            run = False

        elif dic.get(planet) == None or dic.get(planet) == []:
            remove(planet, dic)
            loop(person, "COM", dic, [])
            run = False

        else:
            li.append(planet)

            planet = dic.get(planet)[0]


def remove(planet, dic):
    for key, value in dic.items():
        if planet in value:
            value.remove(planet)
            dic[key] = value


def get_dist():
    global you
    global san
    union = set(you).union(set(san))
    inters = set(you).intersection(set(san))
    return len(union.difference(inters))


with open("../data/day06.txt") as f:
    #f = test2
    data = [row.rstrip("\n\r") for row in f]
    start2(data[:])
