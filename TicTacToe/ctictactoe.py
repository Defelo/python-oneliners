state = [[0 for _ in range(3)] for _ in range(3)]


def num_to_cell(num: int) -> (int, int):
    return (num - 1) % 3, 2 - (num - 1) // 3


def cell_to_num(x: int, y: int) -> int:
    return (2 - y) * 3 + x + 1


def display(numbers: bool):
    print("\033c", end='')
    for i in range(3):
        if i > 0:
            print("---+---+---")
        print("|".join([" " + ("\033[36m" + str(cell_to_num(j, i)) + "\033[0m" if numbers and x == 0 else " XO"[x]) + " " for j, x in
                        enumerate(state[i])]))


def userinput():
    valid = [str(cell_to_num(j, i)) for i in range(3) for j in range(3) if state[i][j] == 0]
    x = ""
    while x not in valid:
        display(True)
        x = input(">> ")
    x, y = num_to_cell(int(x))
    state[y][x] = 1


def aimove():
    for y in range(3):
        for x in range(3):
            if state[y][x] == 0:
                state[y][x] = 2
                return


def check_state() -> int:
    for row in state:
        if row == [1] * 3 or row == [2] * 3:
            return row[0]
    for col in zip(*state):
        if col == (1,) * 3 or col == (2,) * 3:
            return col[0]
    if state[0][0] == state[1][1] == state[2][2] != 0:
        return state[0][0]
    if state[2][0] == state[1][1] == state[0][2] != 0:
        return state[2][0]
    for x in range(3):
        for y in range(3):
            if state[y][x] == 0:
                return -1
    return 0


while check_state() == -1:
    userinput()
    if check_state() == -1:
        aimove()
display(False)
print(["Draw!", "You won!", "Computer won!"][check_state()])
