anten = [
    "..................................................",
    ".r................................................",
    "..........................I.......................",
    "........................I.........................",
    "................................................M.",
    "............h......................A..............",
    "..7....................I.........h................",
    "......7..................................M....9...",
    ".o.....U..........................................",
    "......................................O...........",
    "....c.................J................O...M...A..",
    "..................................................",
    "...R...7..........................................",
    "..............r...................................",
    "...................J..................9...........",
    "...7..K......UJ...................................",
    "......0...U.........................x.............",
    ".......R.......0..B......................x........",
    ".......................k.....Z.......9............",
    ".......L.........I.....J............m.............",
    ".....K.BR........r.0.C............................",
    ".......K.BR......c................................",
    "..................h....m....Al...........H........",
    "..............L..k.......h...m..........x..9......",
    "........................Z.....m........xO.........",
    "..........0................l......................",
    ".6..................b.............................",
    "............k...o..............Z..................",
    "........4.....o...........L.......................",
    "....................Xo............................",
    "...........8..B..L.........i......................",
    "..z...............bX..........A...................",
    "j........z...X......C.......i........5............",
    ".b...H6.......................U.......l...........",
    "..................X...............................",
    "...6......................Z..........a............",
    "....6........c............5.........1.............",
    ".4.......................5........................",
    "..........k.......H1l.............................",
    "2.................C.......i...................u...",
    ".............a....2...............................",
    ".....z....H.......1..8.....................u......",
    "...........j...b..................................",
    "3.........j.........................a.............",
    "...4................a.............................",
    "..M................j.....1..........5.............",
    "............................................u.....",
    "..4..3...........i................................",
    "z3.................2..............................",
    "..........8..................2.C..................",
]


def check1(x):
    return x >= 0 and x < len(anten[0])


def check2(x):
    return x >= 0 and x < len(anten)


pos = set()
ants = {}
for i in range(0, len(anten)):
    for j in range(0, len(anten[i])):
        letter = anten[i][j]
        if letter != ".":
            if letter in ants:
                ants[letter].append((i, j))
            else:
                ants[letter] = [(i, j)]

for i in ants:
    for k in range(0, len(ants[i])):
        for l in range(k + 1, len(ants[i])):
            a, b = ants[i][k]
            c, d = ants[i][l]
            e, f = a - c, b - d
            if check1(a + e) and check2(b + f):
                pos.add((a + e, b + f))
            if check1(c - e) and check2(d - f):
                pos.add((c - e, d - f))

print(len(pos))
