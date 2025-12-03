with open("input.txt",'r') as f:
    text = f.read()
text = text.split("\n")
s = 0
def search(a):
    if len(a)==2:
        return int(a)
    i=0
    j=1
    for n in range(1,len(a)-1):
        if int(a[n]) > int(a[i]):
            return search(a[n:])
        if int(a[n]) > int(a[j]):
            j=n
    if a[-1] > a[j]:
        j = len(a) - 1
    return int(a[i] + a[j])
for i in text:
    if len(i)>0:
        s += search(i)
print(s)
