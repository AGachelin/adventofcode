themap = [
"#############################################################################################################################################",
"#.........#.........#...........#.....#.............#.........................#.........#.............#...#.#.........#...................#E#",
"#.#.#####.#.###.###.###.###.#.#.#.#.###.#########.#.#.###.#######.#.#########.#.#####.#.#.#####.#####.#.#.#.#.###.#.#.#.#######.#########.#.#",
"#.#.....#.......#.#.....#.......#.#.#...#...#.#...#.#...#.#.#...#.#.#.....#.#.#.#.....#.#.#...#.....#...#.#.....#...#.#.#.#...#.....#...#.#.#",
"#.#####.###.#####.#.#######.#.###.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.###.#.#.###.###.#.#.###.#####.#####.###.###.#####.#.#.#.#####.#.#.#.#.#",
"#.....#.....#...#...#.......#.#...#.#...#.#...#...#...#.#.#...#...#...#...#.......#.#...#.#.....#...#...#...#.#...#.......#.#.....#.#.#...#.#",
"#########.#.#.###.###.#####.###.###.###.#.#.#####.###.#.#.#.###########.#####.#####.#.#.#.#.###.#.###.#.###.###.#.#.#######.#####.#.###.###.#",
"#...........#.....#...#...#.......#...#.#.#.#...#...#...#.#...#.#.....#...#...........#.#...#.#.....................#.#...#.#.#...#...#.....#",
"#.#########.#.#####.###.#.#.#######.###.#.###.#.###.#.###.###.#.#.#.#.###.#.#.#.###.###.#####.#.#########.#######.###.#.#.#.#.#.#####.#####.#",
"#...#...#...#.....#...#.#.#...#.....#...#.#...#.....#...#...#.#...#.#.....#.#.#.#...#...#.......#...#...#.#...#...#...#.#...#.........#...#.#",
"###.#.#.#.#.#######.#.#.#.#.#.#.#####.#.#.#.#.#####.#.#.###.#.#####.#####.#.#.#.#.#####.#.#######.#.#.###.#.#.#.#.###.#.###############.#.#.#",
"#...#.#...#.....#...#.#.#...................#.#...#...#...#.#...........................#.#.....#.#.#...#.#.#...#.....#.#...............#.#.#",
"#.###.#########.#.#.#.#.#.#####.#.#.#.#.#.#.###.#.###.###.#.#########.#.###.#.#.###.###.#.#.#.#.#.#.#.#.#.#.#####.###.#.#.###.###########.#.#",
"#.#...#.....#.#.#.#...#.#.#...#...#.#...#.#.....#...#.#...#...#...#...#.....#.#.#...#...#.#.#.#...#.#.#.#.#.#.....#...#.........#...#.....#.#",
"#.#.###.###.#.#.#.#####.###.#.#####.#####.#########.#.#.#####.#.#.#.#########.#.###.#.#.#.###.#####.###.#.#.###.#.#.#########.#.#.#.#.#######",
"#.#...#...#...#.#...#.....#.#...#.......#...#.....#.....#...#...#.#.....#...........#...#.#...#...#.....#.#.....#...#.....#...#...#.#.......#",
"#.###.###.###.#.###.#.###.#.###.#.#####.###.#.###.#########.#####.#####.#.###########.###.#.#####.#####.#.#######.###.###.#.#######.#######.#",
"#...#...#.#...#.....#.....#.#.....#.........#.#...#.........#...#.......#.#.....#.....#...#.....#.#.....#...#.....#...#.#.#.........#.......#",
"###.###.#.#.###.#.#.#.#####.#####.#.#########.#.#######.###.###.###.###.#.#.###.#.#####.#######.#.#.#######.#.#####.###.#.#########.#.#####.#",
"#.........#...#.#.#.#...........#.#.....#.#...#...#.....#.#...#...#.....#.....#.....#...#.......#...#.....#...#.....#...........#.....#.....#",
"#.###.#####.#.#.###.#####.#####.#.#.#.#.#.#.#.###.#.#####.###.###.#.###.###.#.#####.#.###.#######.###.###.###.###.#.#.#########.#.#.###.#####",
"#.............#...#.........#...#.#...#.#.....#.#...#.........#...#.#.#.....#.....#.#.#...#.....#.#.#.#.#...#.....#.#...#.#...#...#...#...#.#",
"#.###.#.#.#.#####.#########.#.###.#####.#####.#.#.#####.#######.#.#.#.#####.#####.#.#.#.#####.#.#.#.#.#.###.#####.#.###.#.#.#.#####.#.###.#.#",
"#.#.#.#.#...#.....#...#.....#.#.......#.......#...#...#.........#.#.#.....#...#...#.#.#...#...#.#...#.#...#.....#.#.#.....#.............#...#",
"#.#.#.###.#.#.###.#.###.#####.#.#####.#.#.###.#####.#.###########.#.###.#.###.#.###.#.###.#.#####.###.#.#######.###.#######.###.#####.#.###.#",
"#.#.#.....#...#.#...#.....#...#.#.#.....#.#.#.#.....#.#.........#.#...#.#...#.#.#...#.....#.......#...#.....#.#.....#.......#...#...#.#...#.#",
"#.#.#.#####.###.###.#.#####.###.#.#.#####.#.#.#.#####.#.#########.###.#####.#.#.###########.#######.###.#.#.#.###.#.#.#######.###.#.###.###.#",
"#.........#.#.....#.#.#.#...#.#...#.....#.#.#.#...#...#...#.....#.#.#.#...#.#.#...#.....#...#.....#.#...#.#...#...#.#.#.....#.#...#.#...#...#",
"#.###.#####.#.#.###.#.#.#.###.###.#####.#.#.#.###.#.###.#.#.###.#.#.#.#.#.#.#.#.#.#.###.#.###.###.#.#####.###.###.#.#.#.###.#.#.###.#.###.###",
"#.#.........#.#.#...#.#.#.#...#...#.....#.#.#.#...#.#...#...#.#...#.#.#.#...#...#...#...#.....#...#.#.....#.......#.#.....#.#.#.#.....#...#.#",
"###.#.#########.#.###.#.#.#.###.###.#.###.#.#.#.###.###.#####.#####.#.#.#####.#.#####.###.#####.###.#.###########.#.#######.#.#.#####.#.###.#",
"#...#...........#.#.....#.#.......#...#...#...#...#...#.#.....#...#.#.#.......#.#...#.....#...#.#...#.#.....#...#.#...#...#.#.#.....#.#...#.#",
"#.#########.#####.#.#####.#####.#####.#.#####.###.###.#.###.#.#.#.#.#.#.#.#.###.###.#######.#.#.#.###.#.###.#.#.#.###.#.#.#.#.#.###.#####.#.#",
"#...#.....#.......#...#...#...#.#.....#.............#.#.....#...#.....#.#.....#.........#.#.#...#.#.#...#...#.#.#.#...#.#.#.#.#...#.........#",
"###.#.###.###########.#.###.#.###.###################.#############.#.#######.#########.#.#.#.###.#.#.###.#.###.#.#.###.#.#.#.###.#####.###.#",
"#...#.#.#.............#...#.#.#...............#...#...#...#.....#...#.....#.#...#.....#...#.#.............#...#...#.#.#.#...#.#.#.....#...#.#",
"#.###.#.#################.#.#.#.#############.#.#.#.###.#.#.###.#.#####.#.#.###.#.#######.#.#######.#######.#.#####.#.#.#####.#.#.#.###.#.#.#",
"#.#...#.....#...........#...#.....#.....#.......#...#...#.#.#.#.#.#...#.#.#.#...#.....#...#.#...#...#.....#.#.....#...#...#...#.....#...#.#.#",
"#.#.###.###.#.###############.#.#.#.###.#########.#.#.###.#.#.#.###.#.#.#.#.#.###.###.#.###.#.#.#####.###.#.#####.###.###.#.#####.###.#.#.###",
"#...#...#...#.........#.....#.....#.#.#.#.......#...#.#.....#.#...#.#.#.....#...#...#...#...#.#.#.......#...#...#.......#.#.#...#.....#.#...#",
"#.###.#.#.#######.#.#.#.###.#####.#.#.#.#.#####.###.#.#######.###.#.#.###.#.###.#########.###.#.#.#######.#.###.#########.#.#.#.#.#####.###.#",
"#...#.#.#.......#.#.#...#...#...#.#.#.#...#...#.#...#...#...#.....#.#.....#...#.........#.....#.#.#.......#...#.....#...#.#...#...#.....#...#",
"###.#.#.#####.#.#.#.#####.###.###.#.#.#####.#.#.#######.#.#.#.#####.#######.#########.#.#.#####.#.#.#########.#.###.#.#.#.#.#####.#.#.###.#.#",
"#...#.#...#.......#...#.....#.#...#.#.......#.#.......#.#.#.#.......#.#.................#.#...#...#.....#.....#...#.#.#...#.#...#...#.#...#.#",
"#.#######.#.#.#######.#.###.#.#.###.#######.#.#######.#.#.#.###.#####.#.#####.#.###.#######.#.#####.###.#.#.#######.#.#####.#.#.#.#.###.###.#",
"#.........#.#.#...#...#...#.#.#.....#.......#.#.....#...#.......#.....#.#.....#...#.........#.#...#.#...#.........#.#.....#.#.#...#.#...#...#",
"#######.###.#.#.#.#.###.###.#.#.#.###.#######.#.#.#######.###.###.###.#.#.###.###.###########.#.#.###.###########.#.#####.###.###.#.#.###.#.#",
"#...#.....#...#.#.#.#.#...#.#...#.#.#.....#.......#.....#.#.#.....#.#.#.#...#...#.......#...#...#.....#...#.............#.....#.............#",
"#.#.#.###.###.#.#.#.#.#.#.#.#####.#.#.###.#.#######.#.#.#.#.#####.#.#.#.###.###.#.###.#.#.#.#######.###.#.###.#####.###########.#.#.#####.#.#",
"#.............#.#.#.....#.#.#.....#...#...#...#.....#.#.#.#.#...#...#.#...#.#.......#.#.#.#.......#.#...#...#.#...#.#.....#.....#.#.#...#.#.#",
"#.###.#.#.###.#.#.#.#.###.#.#.#####.###.#######.#####.###.#.#.#.#####.###.###.#.#####.#.#.#.#######.#.#####.###.#.###.###.#.#####.#.#.#.###.#",
"#.#...#.....#...#...#...#.#.#.#...#...#.......#...#.#...#...#.#...#.....#.....#.#...#.#.....#.......#.#.........#.....#.#.#...#...#.#.#...#.#",
"#.#.###.#.#.#.#.#######.#.#.#.#.#####.###.###.###.#.###.###.#.###.#.#.###.#####.#.#.#.#####.#.###.#.#.#################.#.#.#.###.#.#.###.#.#",
"#...#...............#...#...#.#.....#...#.#...........#...#.#...#...#.#...#...#.#.#...#.....#.......#.#.....#.....#.....#.#.#.#...#.#.#.....#",
"#.###.#.#.#.#.###.#.#.###.#.#.###.#.###.#.#.#.#.#######.#.#.###.#####.#.###.#.#.#.#######.###.#.#####.#.###.#.#.###.###.#.###.#.#.#.#.#####.#",
"#.#.......#.#...#.#.#...#...#...#.#.....#.#.#.#.#.........#...#.#...#.#...#.#.#.#...#...#.#.#...#...#.....#.#.#.....#.....#...#.....#.....#.#",
"#.#######.#.#.#.#.#.###.#.#.###.###.#####.#.###.#.###.#######.#.#.#.#.###.#.#.#####.#.#.#.#.###.#.#.#######.#########.#.#.#.###.###.#####.###",
"#.#.......#...#...#.#...#.#...#...#.#.....#.....#.#...#.....#.....#.#.#...#.#.....#...#.#.....#...#...#.....#.........#.#.#.......#.....#...#",
"#.#.#####.#.#.#####.#.###.###.###.#.###.#.#######.#.#.#.#.###.#####.###.###.###.#.#.###.#####.#####.###.#####.#.#######.#.#####.#.#####.###.#",
"#.#.....#...#...#...#.#.#...#.....#.....#.#.......#.#.........#.#...#...#...#.#...#...#.#...#.......#...#.#...#.........#.............#...#.#",
"#.#.###.#.###.###.###.#.###.#############.#.#######.#.#######.#.#.###.###.#.#.#.#######.#.#.###.#####.###.#.#.###.#############.#.#.#####.#.#",
"#.#...#.....#.#...#.#...#.#.....#.......#.#.#...#.#.#.#.....#...#.......#.......#.......#.#.........#.#.....#...#.....#...#...#...#.......#.#",
"#.#.#.###.#.#.#.###.###.#.#####.#.#.###.#.#.#.#.#.#.#.#.#.#.###############.#.###.#.#####.###########.#.#######.#.#.###.#.#.#.#.###.#####.#.#",
"#.#.....#.#.#.#.#.....#...#...#...#...#.#.#...#.#...#...#.#.....#.........#.#...#.#.........#...#.....#.#.......#...#...#...#...#...#.....#.#",
"#.#.###.#.#.#.#.###.#.###.#.###.#####.###.#####.###.###.#.#####.#.#######.#.###.#.###########.#.#.#####.###.#.#.#####.#######.#.#.###.###.#.#",
"#.#...#...#.#.#...#.#...#.#.........#.....#...#...#...#.#.......#...#.......#.#.#.....#.......#.#.....#.....#.#.........#.....#...#...#.....#",
"#.#.#.###.#.#####.#.#.#.#.#######.#.#######.#####.#####.#####.#.###.#.#####.#.#.#####.#.#######.#####.#################.#.###.#.#####.###.#.#",
"#...............#.#.#.#.#.......#.#...#.....#...#.....#.#.....#.....#...#...#.#...#.#.#...#...#.....#.........#.........#...#.#.....#...#.#.#",
"#####.#.#.###.###.###.#.#######.#.###.#.###.#.#.#####.#.#.###.###.#.#####.#.#.###.#.#.###.#.#######.#.#######.#.#######.###.#.#.###.#.#.#.#.#",
"#...#.#...#...#...#...#...#.....#...#.#...#.#.#.....#...#.#.........#.....#.#.....#.....#.#.........#.#...#...#.#...#.....#.#.#.....#.#.#.#.#",
"#.###.###.#.#.#.###.#######.#######.#.#.#.#.#.###.#######.#.#########.#####.#.#######.###.#.#########.###.#.###.#.#.#.###.#.#.#.#####.#.#.#.#",
"#...#.#...#.#.#.#...........#.......#.#...#...#...#.......#...#.......#...#.#.......#.#...#.#.......#.....#.#.....#.#...#...#.#.....#.#.#.#.#",
"#.#.#.#.#.#.#.#.#.###########.#######.###.#####.#.#.#.#####.#.#.#########.#.#######.###.###.#.###########.#.#######.#.#.###########.###.#.#.#",
"#.#...#.....#.#.#.#.........#...#...#.#...#.#...#.#.#.#.....#.#.........#.#...#...#.#...#...#...........#.#.......#...#.#.........#.....#.#.#",
"#.#####.#.#.###.#.#########.#.#.#.#.###.#.#.#.###.#.###.###.#.#########.#.###.#.#.#.#.###.#########.#.###.#######.#####.#.###.###########.#.#",
"#.......#...#...#.........#...#...#.#...#...#...#.#.....#.#.#.....#...#.#.....#.#.#...#.#.#.......#.#...#...#...#...#...#.#.#...#.......#...#",
"#########.###.###.#.#####.#.#######.#.###.#.###.#########.#.#####.#.#.#.#########.#.###.#.#.#####.#####.###.#.#.###.#.###.#.###.#.#####.#.###",
"#.......#...#...#.#...#.#.#.....#...#...#.#...#...#.......#.#...#.#.#.#.#...........#...#...#...#...#.....#.#.#.#.#.#...#.....#.......#...#.#",
"#.###.###.#.###.###.#.#.#.#####.#.#.###.#####.###.#.#.#####.#.#.#.###.#.#.###.#.#.###.#.#####.#####.#.#.###.#.#.#.#.#.#.#####.#####.#.#####.#",
"#.#.#.......#.#.....#.#...#.....#.#...#.........#...#.#...#...#.#.....#...#...#...#...#...#...#.....#.#.#...#.#...#.#.#.....#...#...#.#.....#",
"#.#.#########.#######.#.#######.#.###.#.#######.#####.#.#.#####.#########.#.#######.###.#.#.#.#.#####.###.###.###.#.#.#####.###.#####.#.###.#",
"#.#.#.........#.......#.......#.#...#...#...#.#...#.#...#...#...#.....#...#.....#...#...#.....#.....#.#...#...#.#.#.#.#...#...#.....#.....#.#",
"#.#.#.#####.#.#.#############.#.#.#.#####.#.#.###.#.#####.#.#.###.###.#.#.###.#.#.###.#############.#.#.#####.#.#.#.#.#.###.#.#####.#######.#",
"#...............#.....#.......#.#.#.#.....#.#.....#.#.....#.#.#...#.#.#.....#.#.#.#.#...............#...#.....#...#.#.#.#.......#.#.........#",
"#.#.#.#.#######.###.#.#.#.#.#.#.#.#.#.#####.###.#.#.#.#####.#.#.###.#.#####.###.#.#.#####.###########.#####.###.###.#.#.#.#####.#.#########.#",
"#.#.............#...#.....#.#.#...#.....#.#...#.....#...#...#.#...#.#.......#...#.#...#.....................#.#.#.#.#...#.#.#...#...#...#...#",
"#.#.#.#######.#.#.#.###.#.###.#########.#.###.#####.###.#####.###.#.###.#####.#.#.#.###.###########.#########.#.#.#.#.#.#.#.#.###.#.#.###.###",
"#.#...#.......#.#.#.....#.....#.........#...#...#...#...#...............#.....#.#.#.....#...#.....#.#.....#.......#.#...#.#...#...#...#...#.#",
"#.###.#.#######.#.#####.#.#.###.###########.###.#####.###.###.###.#.###.#####.#.#.#.#.###.###.###.###.###.#.#######.#.###.#.###.#.#####.###.#",
"#...#...#.......#.#...#.#.......#.........#...#.....#...#...#.#...#...#.#...#.#.#...#.#.....#.#.....#.#.#.#...#.....#.#...#...#.#.....#.....#",
"###.#.###.#######.###.#.#.#######.#.#####.###.#####.###.###.#.#.###.#.#.#.#.#.#.###.#.#####.#.#####.#.#.#.#####.###.###.#####.#.#.###.#####.#",
"#.............#...#...#...#.......#.#...#.....#.....#...#...#.#...#.#.#...#...#.#...#.....#.#...#.....#.........#.#.....#.....#.#...#.......#",
"#.#.#.#.#####.#.#.#.#.###.#.#########.#.#.###.#.#####.###.###.###.#.#.#.#########.#######.#.###.#.#####.#########.#.#.#######.#.#.#.#########",
"#.......#.....#.....#.#...#.#.........#.#...#.#...#...#...#.#...#.#.#.#.#...#.........#...#.....#.#...#.#.......#...#.......#.....#.#.......#",
"#.#.#.#.#.###.#######.#.###.#.#########.#.#.#####.#.###.###.#.#.#.###.#.#.#.#.#######.#.###.#.#####.#.###.###.#.#.#########.#####.#.#.#####.#",
"#.........#.....#.....#.#.......#.....#...#.......#.#...#.......#...#.#...#...#.....#...#...#.......#.....#.....#.#.......#.........#.....#.#",
"#.###.#.#.#######.#####.#######.#####.#####.#####.#.#.###.#########.#.#.#.#######.#.###.#.#########.#.#####.#####.#.#.###.#######.###.###.#.#",
"#...#...#...#.....#.....#...#.............#.#...#...#.#...#.#.......#.#.#.#.....#.#...#...#.........#.....#.....#...#.#...#...............#.#",
"#.#.#.#.#.#.#.#####.#####.#.###.#########.#.#.#.#####.#.###.#.#######.#.#.###.#.#.###.#####.#######.#####.#####.#####.#.###.#.###.#.#.#.###.#",
"#.#.#.....#.......#.......#...#...#.....#.#.#.#.....#.#.....#...#.....#.#.....#...#.#.......#...#...#.#...#.#...#.....#...#.#.#...#...#.#...#",
"#.###.###.###################.#.#.#####.#.#.#.#####.#.#########.#.###.#############.#########.###.###.#.###.#.###.###.###.#.#.#.#.#####.#####",
"#.....#.........#...........#.#.#.......#...#.....#...#...#.....#.#...#.......................#...#.....#...#.#.#.#.#...#.#.#.#...#.....#...#",
"#.#####.#.#####.#.#########.#.#.###########.#####.#.###.#.#.#######.###.#.#.#############.#####.###.#####.#.#.#.#.#.#.###.###.###.#.#####.#.#",
"#.....#.......#...#.....#.....#.#.................#.....#...#.......#...#.#.#.......#...#.#.....#.#.#.....#.#.#.#...#...#.#...#...#...#...#.#",
"#####.###.###.#####.#.#.#.###.#.#.###############.#.#.#######.#####.#.###.###.###.#.#.#.###.#####.#.###.###.#.#.###.###.#.#.###.###.#.#.###.#",
"#...#.#.......#.......#.#.....#.#.#...#.....#.....#.#...#.#...#...#.#...#...#.#...#.........#.....#...#.#...#.#.#.....#.#.#...#...#.#.....#.#",
"#.#.###.#.#####.#####.#.#.#.###.#.#.#.#.###.#.#.###.###.#.#.#.#.#.#####.###.#.#.#.#############.#####.###.#.#.#.#.#####.#.###.###.#####.###.#",
"#.#.....#.......#...#.#.....#...#.#.#.......#.....#.#...#...#...#.#.......#.....#...#.........#.#...#.....#.#.#...#.....#.....#...#...#.#...#",
"#.#######.#.###.#.#.#########.#.#.#.###.###.#####.###.###.#######.#.###############.#######.#.#.#.#.#####.###.#.###.###.#######.###.#.###.#.#",
"#.#...........#.#.#.....#.....#...#...#.....#...#...#...#.#.....#.#.#...........#.#.........#.#.#.#.#.....#...#.#...#.#.#.....#...#.#...#.#.#",
"#.#.#####.#.#.#.#.#####.#.###########.#.###.#.#.###.###.#.#.#####.#.#.#########.#.###########.#.#.#.#.#####.#####.###.#.#.###.###.#.###.#.#.#",
"#...#.......#.#.#.#...#.#.....#...#...#...#.#.#...#...#.#...#...#...#.#.......#.#.#.....#.....#...#...#...#.#.....#.....#.#...#...#...#...#.#",
"#.#######.#.#.###.#.#.#.#####.#.#.#####.#.#.#.#####.#.#.#####.#.#.#.#.#.###.#.#.#.#.#.###.#############.#.#.#.#.###.#####.#.###.###.#.###.#.#",
"#.........#.#.#...#.#.#...#.#...#.....#.#.#...#.....#.#.......#.#.#...#...#.#.#.#...#...#.#.........#...#...#.....#...#.......#.............#",
"#####.###.#.#.#.###.#.###.#.#########.###.#.###.#####.#########.###.#####.#.###.#.#.###.#.#####.###.#.###########.###.###.###.###.###.#.#.###",
"#...#.#.....#.#.#...#...#.#.........#.....#.#...#.............#...#.#.....#...#.#.....#.#.......#.#...#.......#...#.#.........#.#.#...#.#...#",
"#.#.#.#.#.#.#.#.#.###.###.#.#.#####.#####.###.#####.#########.###.#.#.#######.#.#######.#########.#########.#.#.###.#######.###.#.#.###.#.###",
"#.#...#...#...#.#.#...#.....#.#...#.....#.#...#.........#...#...#...#.#.....#.#.#...........#...............#...#.........#...#.#...#...#...#",
"#.#######.#.###.#.#.###.###.###.#.#######.#.###.#######.#.#.#.#########.###.#.#.#.#####.#.#.#.#.#############.###.###.#######.#.#####.###.#.#",
"#.#...#...#.....#.#...#...#.....#.........#.#...#.....#...#.#.#.......#.#.....#.#...#...#.#...#.....#.........#...#...#.....#.....#.#.#...#.#",
"#.#.#.#.###.#####.###.###.#.#############.#.#.###.#########.###.###.#.#.#######.###.#####.#########.#.#######.###.#.#.#.#.#######.#.#.###.#.#",
"#...#.#.#...#.....#.....#.#...#...#.....#.#...#...........#.....#.#.#.....#...#...#.#.....#.#.....#.........#...#.#.#.#.#.#.....#...#.#.....#",
"#######.#.#.#.#####.#####.###.###.#.###.#########.#####.#.#######.#.#.###.#.#.###.#.#.#####.#.#.#####.#.###.###.#.#.###.#.#.###.###.#.#.#.###",
"#.....#.#.#...#...#...#...#...#...#...#.........#.#.....#.#.......#.#.....#.#.....#...#...#...#.....#...#...#...#.#.....#.#.#.......#.#.....#",
"#.###.#.#.#.#####.###.#.###.###.#.###.###.#####.###.#####.#.#####.#.#####.#.#######.#####.#.#####.#.#####.#.#.###.#######.#.#.#######.###.#.#",
"#...#...#.#.#.......#.#...#.#...#...#...#...#.#...#...#...#.#...#.#.....#.#.#.....#.#.....#.....#.#...#...#.#...#.......#...#...#...#.......#",
"#.#.#.###.#.#.###.###.###.#.###.#.#####.###.#.###.#.#.###.#.###.#.#####.###.#.###.#.#.#.###.#####.###.#.###.#.#.#######.#######.#.#.#######.#",
"#.#.#.#...#...#...#.....#.#.....#.#.....#.#.#.....#.#.....#...#.#.....#.....#...#.#.#.......#.....#.#...#.#.#.#.#.....................#...#.#",
"###.#.#.###.###.###.#####.#####.###.#####.#.###.###.#####.###.#.#.###.#######.#.#.#.#.#.###.#.#####.###.#.#.#.#.#.#.###.#.#######.#.#.#.###.#",
"#...#.#.....#.....#.....#.....#.#...#.....#...#.#...#.......................#.#.#.#.#.#.#...#...#.#.......#.#.#.#.#...#...#...#...#.#...#...#",
"#.#########.#.#####.###.#####.#.#.#####.#.###.#.#####.###.#.###.#.#.#.###.###.#.###.#.#.#.#.###.#.#.###.###.#.#.#.###.#.###.#.#.###.#####.###",
"#...........#.#...#...#.....#.#...#.....#.#...#.......#...#.#...#...................#...#.#.....#...#.#...#...#.#...#.......#.#.#...#...#...#",
"#.#######.#####.#.#####.#####.#.###.#####.#.#.#########.#.#.###.#.#.#.#.#.#.###########.#.#.#####.###.#.#.###.#.###.###.#####.#.#.###.#.###.#",
"#.......#.......#.....#.#...#.............................#.....#.#.#.#...#.#.............#.#.....#.....#.#...#...#.#...#.....#.#...#.#.....#",
"#######.#.#.#########.#.#.#.#######.#.###.#.#######.#####.#######.#.#.#####.###.#######.###.#.#####.###.#.#.###.#.#.###.#.#####.###.#.#######",
"#.....#.....#.....#...#...#.......#.#...#.#.......#.#.............#.#.#...#...#.....#...#...#.....#.....................#.................#.#",
"#####.###.###.###.#.###.###.#####.#.#.#.#.#######.###.###.#.#######.#.#.#.###.#####.###.#.#.#####.#.#.#.#.#.#.#.#######.###.#.#####.#####.#.#",
"#.....#...#...#.#.#.#.....#...#.#.#.#.#...#...#.............#.................#...#...#.#.#.......#.#.#...#...#.......#...#...#.......#...#.#",
"#.#####.#.#.###.#.#.#########.#.#.#.#.#####.#.#.#######.#####.###########.#.###.#.###.#.#.#.#######.#.#.#####.#######.#.#.#####.#######.###.#",
"#S......#.......#.............#.....#...................................#.......#.....#.............#...............#.........#.............#",
"#############################################################################################################################################",
]

themap = [
"###############",
"#.......#....E#",
"#.#.###.#.###.#",
"#.....#.#...#.#",
"#.###.#####.#.#",
"#.#.#.......#.#",
"#.#.#####.###.#",
"#...........#.#",
"###.#.#####.#.#",
"#...#.....#.#.#",
"#.#.#.###.#.#.#",
"#.....#...#.#.#",
"#.###.#.#.#.#.#",
"#S..#.....#...#",
"###############",
]

for a in range(0, len(themap)):
    for b in range(0, len(themap[a])):
        if themap[a][b] == "S":
            i=a
            j=b

to_explore = [(i, j, 0, 0, i, j)]
explored = {}
score = {}
E = []
def calc(d, d1):
    if d!=d1:
        return 1
    else:
        return 0

while to_explore != []:
    i, j, dir, r, i1, j1 = to_explore.pop(0)
    if themap[i][j] == "E":
        E.append(r)
    else:
        if ((i, j) in score and score[(i, j)] > r) or (i, j) not in score:
            if themap[i+1][j] !="#":
                res = calc(dir, 1) * 1000 + 1
                to_explore.append((i+1, j, 1, r + res, i, j))
            if themap[i-1][j] !="#":
                res = calc(dir, 3) * 1000 + 1
                to_explore.append((i-1, j, 3, r + res, i, j))
            if themap[i][j+1] !="#":
                res = calc(dir, 0) * 1000 + 1
                to_explore.append((i, j+1, 0, r + res, i, j))
            if themap[i][j-1] !="#":
                res = calc(dir, 2) * 1000 + 1
                to_explore.append((i, j-1, 2, r + res, i, j))
            explored[(i, j)] = i1, j1
            score[(i, j)] = r
print(min(E), E)
