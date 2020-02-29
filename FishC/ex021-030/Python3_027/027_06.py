from itertools import permutations

allarrangement = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
for i in allarrangement:
    if sum(i[0:3]) == sum(i[3:6]) == sum(i[6:9]) == sum(i[0:9:3]) == sum(i[1:9:3]) == sum(i[2:9:3]) == sum(i[0:9:4]) == sum(i[2:8:2]):
        print("{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}\n".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
