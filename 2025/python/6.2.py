with open("input.txt") as f:
    text = f.readlines()
operators = text[-1].strip().split(" ")
operators  = [i for i in operators if i != '']
problems = text[:-1]
new_problems = [[]]
for i in range(len(problems[0])-2, -1, -1):
    prob = ""
    for j in range(len(problems)):
        if problems[j][i] != ' ':
            prob += problems[j][i]
    if prob != "":
        new_problems[-1].append(prob)
    else:
        new_problems.append([])
new_problems = new_problems[::-1]
s=0
for i, k in enumerate(operators):
    if k == "*":
        s1 = 1
        for j in new_problems[i]:
            s1 = s1 * int(j)
        s = s + s1
    else:
        s2 = 0
        for j in new_problems[i]:
            s2 = s2 + int(j)
        s = s + s2
print(s)