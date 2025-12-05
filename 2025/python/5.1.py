with open("input.txt", "r") as f:
    text = f.read().split("\n")
i = text.index("")
class interval():
    def __init__(self, inf, sup):
        self.inf=inf
        self.sup= sup
d={}
first = text[:i]
first = [list(map(int,i.split("-"))) for i in first]
second = text[i+1:]
sorted_intervals = sorted(first, key=lambda x: x[0])
merged = []
for interval in sorted_intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
first = merged
s = 0
for b in second:
    try:
        b=int(b)
    except:
        continue
    for i in first :
        if i[0]<=b:
            if i[1]>=b:
                s+=1
                break
        else:
            break
print(s)
