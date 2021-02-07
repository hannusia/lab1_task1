def read_file(path: str) -> list:
    with open(path) as board_file:
        board = board_file.read().splitlines()
    return board
def check_lines(board: list) -> bool:
    lines = {0: [], 1: [], 2: [], 3: [], 4: [],
             5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    for i in range(len(board)):
        for j in board[i]:
            if j in '123456789':
                lines[i] = [j]
    for i in lines:
        if len(set(lines[i])) != len(lines[i]):
            return False
    return True
print(check_lines(["*******","***1***","****3**","**4*1*9","*****8*","*61**35",\
        "3**8***","*******","**2*5**","***2***","*******"]))