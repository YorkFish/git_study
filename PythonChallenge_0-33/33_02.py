from PIL import Image

img = Image.open("beer2.png")
ashes = list(img.getdata())
max_value = max(ashes)
for i in range(33):
    data = [ash == max_value for ash in ashes]
    side = int(len(data) ** 0.5)
    res = Image.new('1', (side, side))
    res.putdata(data)
    res.save(f"./beer/33_{i+1:0>2}.png")
    ashes = [ash for ash in ashes if ash < max_value-1]
    max_value = max(ashes, default=-1)
