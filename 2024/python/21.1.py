inp = [
"826A",
"341A",
"582A",
"983A",
"670A",
]

inp = [
"029A",
"980A",
"179A",
"456A",
"379A",
]
i = 3
j = 2
i1 = 0
j1 = 2
i2 = 0
j2 = 2
R = 0

K = {"7":(0,0), "8":(0,1), "9":(0,2), "4":(1,0), "5":(1,1), "6":(1,2), "1":(2,0), "2":(2,1), "3":(2,2), "0":(3,1), "A":(3,2)}
K1 = {"^":(0,1), "A":(0,2), "v":(1,1), "<":(1,0), ">":(1,2)}

def r(k, robot, m, n):
    c = ""
    a, b = robot[k]
    for _ in range(abs(m-a)):
        if m>a:
            c+="^"
        else:
            c+="v"
    for _ in range(abs(n-b)):
        if n>b:
            c+="<"
        else:
            c+=">"
    c+="A"
    return c, a, b

def test(code, robot, i, j):
    codeA, a, b = r(code[0], robot, i, j)
    codeB, a, b = r(code[-1], robot, i, j)
    if len(codeA)>len(codeB):
        m = -1
        n = -1
    else:
        m = 1
        n = 0
    return m, n

for code in inp:
    res = 0
    for k in code:
        code1, i, j = r(k, K, i, j)
        for k1 in range(0, len(code1)-1):
            if k1==0:
                m1, n1 = test(code1, K1, i1, j1)
            code2, i1, j1 = r(code1[m1*k1+n1], K1, i1, j1)
            for k2 in range(0, len(code2)-1):
                if k2==0:
                    m2, n2 = test(code2, K1, i2, j2)
                code3, i2, j2 = r(code2[m2*k2+n2], K1, i2, j2)
                res += len(code3)
            code3, i2, j2 = r(code2[-1], K1, i2, j2)
            res+=len(code3)
        code2, i1, j1 = r(code1[-1], K1, i1, j1)
        for k2 in range(0, len(code2)-1):
            if k2==0:
                m2, n2 = test(code2, K1, i2, j2)
            code3, i2, j2 = r(code2[m2*k2+n2], K1, i2, j2)
            res += len(code3)
        code3, i2, j2 = r(code2[-1], K1, i2, j2)
        res+=len(code3)
    R+=res*int(code[:-1])
print(R)
