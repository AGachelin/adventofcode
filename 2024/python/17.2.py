n = 1
res = []

Program = [2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0]

def combo(j):
    match j:
        case 0 | 1 | 2 | 3 :
            return j
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C

A = n
B = 0
C = 0
res = []
k = len(Program)-1
while k!=0:
    print(k)
    while A%8 ^ 5^ A//2**5!=Program[k]:
        A+=1
    A*=8
    k-=1

print(A//8)