# state = [[0 for _ in range(3)] for _ in range(3)]

# num_to_cell = lambda num: ((num - 1) % 3, 2 - (num - 1) // 3)
# cell_to_num = lambda x, y: (2 - y) * 3 + x + 1
# display = lambda numbers: print("\033c", end='') or ([print(("---+---+---\n" if i > 0 else "") + "|".join(
#     [" " + ("\033[36m" + str(cell_to_num(j, i)) + "\033[0m" if numbers and x == 0 else " XO"[x]) + " " for j, x in
#      enumerate(state[i])])) for i in range(3)] and None)
# userinput = lambda: [
#     (list(iter(lambda: (display(True) or xin.__setitem__(0, input(">> ")) or True) and xin[0] in valid,
#                True)) and False) or [state[y].__setitem__(x, 1) for x, y in [num_to_cell(int(xin[0]))]]
#     for xin, valid in [([""], [str(cell_to_num(j, i)) for i in range(3) for j in range(3) if state[i][j] == 0])]
# ]
# check_state = lambda: \
#     ([row[0] for row in state if row == [1] * 3 or row == [2] * 3] or
#      [col[0] for col in zip(*state) if col == (1,) * 3 or col == (2,) * 3] or
#      ([state[0][0]] if state[0][0] == state[1][1] == state[2][2] != 0 else []) or
#      ([state[2][0]] if state[2][0] == state[1][1] == state[0][2] != 0 else []) or
#      [-1 if any([state[y][x] == 0 for x in range(3) for y in range(3)]) else 0])[0]

# old_aimove = lambda: [
#     list(iter(lambda: (
#             value[0] is not None and state[value[0][1]][value[0][0]] == 0 or
#             value.__setitem__(0, (random(), random())) and False), True))
#     and False or value[0]
#     for value, random in [([None], lambda: __import__("random").randint(0, 2))]
# ][0]

# aimove = lambda: ([
#     (k, j)
#     for i in [2, 1] for j in range(3) for k in range(3) for l in range(4)
#     if (l == 0 and state[j][k] == 0 and state[j][(k+1)%3] == i and state[j][(k+2)%3] == i) or
#        (l == 1 and state[j][k] == 0 and state[(j+1)%3][k] == i and state[(j+2)%3][k] == i) or
#        (l == 2 and j == k and state[j][k] == 0 and state[(j+1)%3][(k+1)%3] == i and state[(j+2)%3][(k+2)%3] == i) or
#        (l == 3 and j + k == 2 and state[j][k] == 0 and state[(j+1)%3][(k+2)%3] == i and state[(j+2)%3][(k+1)%3] == i)
# ] + ([(1, 1)] if True and state[1][1] == 0 else []) + [
#     list(iter(lambda: (
#         value[0] is not None and state[value[0][1]][value[0][0]] == 0 or
#         value.__setitem__(0, (random(), random())) and False), True))
#     and False or value[0]
#     for value, random in [([None], lambda: __import__("random").randint(0, 2))]
#     ]
# )[0]


(lambda: [
    [
        [
            list(iter(lambda: (
                    (userinput() and False or check_state() == -1 and [state[y].__setitem__(x, 2) for x, y in
                                                                       [aimove()]]) and False or
                    check_state() != -1
            ), True)) and
            display(False) or
            print(["Draw!", "You won!", "Computer won!"][check_state()])
            for userinput, aimove in [[
                lambda: [
                    (list(iter(lambda: (display(True) or xin.__setitem__(0, input(">> ")) or True) and xin[0] in valid,
                               True)) and False) or [state[y].__setitem__(x, 1) for x, y in [num_to_cell(int(xin[0]))]]
                    for xin, valid in [([""], [str(cell_to_num(j, i)) for i in range(3) for j in range(3) if state[i][j] == 0])]
                ],
                lambda: ([
                    (k, j)
                    for i in [2, 1] for j in range(3) for k in range(3) for l in range(4)
                    if (l == 0 and state[j][k] == 0 and state[j][(k+1)%3] == i and state[j][(k+2)%3] == i) or
                       (l == 1 and state[j][k] == 0 and state[(j+1)%3][k] == i and state[(j+2)%3][k] == i) or
                       (l == 2 and j == k and state[j][k] == 0 and state[(j+1)%3][(k+1)%3] == i and state[(j+2)%3][(k+2)%3] == i) or
                       (l == 3 and j + k == 2 and state[j][k] == 0 and state[(j+1)%3][(k+2)%3] == i and state[(j+2)%3][(k+1)%3] == i)
                ] + ([(1, 1)] if True and state[1][1] == 0 else []) + [
                    list(iter(lambda: (
                        value[0] is not None and state[value[0][1]][value[0][0]] == 0 or
                        value.__setitem__(0, (random(), random())) and False), True))
                    and False or value[0]
                    for value, random in [([None], lambda: __import__("random").randint(0, 2))]
                    ]
                )[0]
            ]]
        ]
        for display, check_state in [[lambda numbers: print("\033c" if ansi else "", end='') or ([print(("---+---+---\n" if i > 0 else "") + "|".join(
    [" " + (("\033[36m" if ansi else "") + str(cell_to_num(j, i)) + ("\033[0m" if ansi else "") if numbers and x == 0 else " XO"[x]) + " " for j, x in
     enumerate(state[i])])) for i in range(3)] and None),
    lambda: ([row[0] for row in state if row == [1] * 3 or row == [2] * 3] or
     [col[0] for col in zip(*state) if col == (1,) * 3 or col == (2,) * 3] or
     ([state[0][0]] if state[0][0] == state[1][1] == state[2][2] != 0 else []) or
     ([state[2][0]] if state[2][0] == state[1][1] == state[0][2] != 0 else []) or
     [-1 if any([state[y][x] == 0 for x in range(3) for y in range(3)]) else 0])[0]]]
    ]
    for state, num_to_cell, cell_to_num, ansi in [(
        [[0 for _ in range(3)] for _ in range(3)],
        (lambda num: ((num - 1) % 3, 2 - (num - 1) // 3)),
        (lambda x, y: (2 - y) * 3 + x + 1),
        True
    )]
] and None)()

# list(iter(lambda: (
#         (userinput() and False or check_state() == -1 and [state[y].__setitem__(x, 2) for x, y in
#                                                            [aimove()]]) and False or
#         check_state() != -1
# ), True)) and
# display(False) or
# print(["Draw!", "You won!", "Computer won!"][check_state()])

