#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def find_way(img, entrance, export):
    w, h = img.size
    pix = img.load()
    right_way={}
    trial = [export]
    white = (255, 255, 255, 255)
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    try:
        while True:
            t = trial.pop(0)
            if t == entrance:
                print("Find over!")
                print(len(right_way))
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


def reproduce(img, way, entrance, export):
    new_img = img.copy()
    t = (0, 255, 0, 255)  # green
    if way:
        p = entrance
        while p != export:
            new_img.putpixel(p, t)
            p = way[p]
        new_img.putpixel(p, t)
    new_img.save("24_maze_route.png")


if __name__ == "__main__":
    img = Image.open("maze.png")
    entrance = (639, 0)
    export = (1, 640)

    way = find_way(img, entrance, export)
    reproduce(img, way, entrance, export)
