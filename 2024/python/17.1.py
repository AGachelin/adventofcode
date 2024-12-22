

A = 51571418
B = 0
C = 0

res = []
Program = 2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0

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
k = 0
while k<len(Program):
    i = Program[k]
    j = Program[k+1]
    ok = True
    match i:
        case 0:
            A = A//(2**combo(j))
        case 1:
            B = B^j
        case 2:
            B = combo(j)%8
        case 3:
            if A!=0:
                k = j
                ok = False
        case 4:
            B = B^C
        case 5:
            res.append(combo(j)%8)
        case 6:
            B = A//(2**combo(j))
        case 7:
            C = A//(2**combo(j))
    if ok:
        k+=2

print("".join(str(i)+"," for i in res))