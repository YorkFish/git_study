#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def find_way(w, h, pix, entrance, export):
    right_way={}
    trial = [export]
    white = (255, 255, 255, 255)
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    try:
        while True:
            t = trial.pop(0)
            if t == entrance:
                print("Find over!")
                print(len(right_way))  # 194941
                break
            for d in direction:
                new = (t[0]+d[0], t[1]+d[1])
                if -1 < new[0] < w and -1 < new[1] < h:
                    if pix[new[0],new[1]] != white and new not in right_way:
                        trial.append(new)
                        right_way[new] = t
        return right_way
    except Exception as e:
        print(e)


def reproduce(pix, way, entrance, export):
    t = (0, 255, 0, 255)
    if way:
        p = entrance
        data = []
        while p != export:
            data.append(pix[p[0],p[1]][0])
            p = way[p]

    print(len(data))  # 44622
    with open("maze.zip", "wb") as f:
        f.write(bytes(data[1::2]))


if __name__ == "__main__":
    img = Image.open("maze.png")
    w, h = img.size
    pix = img.load()
    entrance = (639, 0)
    export = (1, 640)

    way = find_way(w, h, pix, entrance, export)
    reproduce(pix, way, entrance, export)
