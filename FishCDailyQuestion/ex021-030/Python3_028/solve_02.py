for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            if x + y + z == 15 and x <= y <= z:
                print(x, y, z)
