with open("input.txt") as f:
    text = f.readlines()
operators = text[-1].strip().split(" ")
operators  = [i for i in operators if i != '']
problems = text[:-1]
problems = [i.strip().split(" ") for i in problems]
for j, problem in enumerate(problems):
    problems[j] = [int(i) for i in problem if i != '']
s=0
for i, k in enumerate(operators):
    if k == "*":
        s1 = 1
        for j in range(len(problems)):
            s1 = s1 * problems[j][i]
        s = s + s1
    else:
        s2 = 0
        for j in range(len(problems)):
            s2 = s2 + problems[j][i]
        s = s + s2
print(s)