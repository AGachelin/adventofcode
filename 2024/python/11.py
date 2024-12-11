from math import log, floor
from functools import cache # for part 2

line = "4 4841539 66 5279 49207 134 609568 0".split(" ")
line = map(int, line)

@cache # for part 2
def stone(i, n):
    if n==0:
        return 1
    else:
        if i==0:
            return stone(1, n-1)
        elif floor(log(i, 10))%2 == 1:
            i = str(i)
            return stone(int(i[:len(i)//2]), n-1) + stone(int(i[len(i)//2:]), n-1)
        else:
            return stone(i*2024, n-1)
res = 0
for i in line:
    res += stone(i, 75) # 25 for part 1
print(res)