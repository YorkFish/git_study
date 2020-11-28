from itertools import permutations as pt

for each in pt(range(1, 10), 9):
    a, b, c, d, e, f, g, h, i = each
    if a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g:
        print('-' * 7, '\n', a, b, c, '\n', d, e, f, '\n', g, h, i)
print('-' * 7)

