with open("./input.txt",'r') as f:
    text = f.read()
text = text.split("\n")

s = 0
def search(a):
    if len(a)==12:
        return int(a)
    
    l=[i for i in range(12)]

    for n in range(1,len(a)):
        for k in range(max(0, 12-len(a)+n),min(n,12)):
            if int(a[n])>int(a[l[k]]) and (l[k-1]<n or k==0):
                l = l[:k] + [n + i for i in range(12-k)]
                break
    return int("".join(a[i] for i in l))

for i in text:
    if len(i)>0:
        s += search(i)
print(s)
