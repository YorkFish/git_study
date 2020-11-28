#!/usr/bin/env python3
# coding:utf-8

"""
 ----> (x, 0)
|
|
v
(0, y)
"""

def run(maze, entrance, export):
    trial = [export]
    right_way = {}
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    while True:
        t = trial.pop(0)
        if t == entrance:
            print("Over!")
            break
        for d in direction:
            new = (t[0]+d[0], t[1]+d[1])
            if -1 < new[0] < 6 and -1 < new[1] < 7:
                if maze[new[1]][new[0]] == 1 and new not in right_way:
                    print(new)
                    trial.append(new)
                    right_way[new] = t
    return right_way


def reproduce(way, entrance, export):
    tmp = way[entrance]
    while tmp != export:
        print(tmp)
        tmp = way[tmp]


if __name__ == "__main__":
    """
    1: path
    0: wall
    """
    maze = [[1, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 1]]

    entrance = (0, 0)
    export = (5, 0)

    res = run(maze, entrance, export)
    # reproduce(res, entrance, export)
