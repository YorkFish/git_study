from PIL import Image

img = Image.open("beer2.png")
ashes = list(img.getdata())
n = len(ashes)
lights = img.getcolors()
lights.reverse()

wall = []
for num, _ in lights:
    n -= num
    tmp = n ** 0.5
    if tmp == int(tmp):
        wall.append(tmp)
print(lights)
print(len(lights))
print(wall)
print(len(wall))
