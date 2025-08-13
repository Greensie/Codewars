#https://www.codewars.com/kata/5899a4b1a6648906fe000113/train/python
from collections import defaultdict

def find_routes(routes):
    destinations_map = defaultdict()
    connections_map = defaultdict()
    ret_route = []
    n = len(routes)
    for dest in routes:
        destinations_map[dest[1]] = dest[0]
        connections_map[dest[0]] = dest[1]

    start_point = connections_map.keys() - destinations_map.keys()


    str_start_point = str(start_point)
    str_start_point_cleared = str_start_point.replace("{'","").replace("'}","")
    ret_route.append(str_start_point_cleared.replace("'",""))
    x = str_start_point_cleared
    while(n>0):
        curr_dirr = connections_map.get(x)
        ret_route.append(curr_dirr)
        x = curr_dirr
        n -= 1

    ret_str = ''
    for x in ret_route:
        ret_str += x.replace("'","")
        ret_str += ", "

    ret_str2 = ret_str[:-2]
    return ret_str2


def solution_smarter(routes):
    d = dict(routes)
    res = list(d.keys()-d.values())
    pass

routes = [('MNL','TAG'), ('CEB','TAC'), ('TAG','CEB'), ('TAC','BOR')]
print(find_routes(routes))
