from datetime import datetime

for y in range(1006, 1997, 10):
    date = datetime(y, 1, 26)
    if date.weekday() == 0:
        if date.year % 4 == 0:
            print(date.year)
