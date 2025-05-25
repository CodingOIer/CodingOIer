def read_board():
    with open('./chess-games/chess.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        board = [line.split('|') for line in lines]
    return board

def write_board(board):
    with open('./chess-games/chess.txt', 'w') as f:
        f.write('\n'.join(['|'.join(row) for row in board]))

def getPiece(x, y):
    board = read_board()
    row = 8 - x
    col = ord(y.upper()) - ord('A')
    return board[row][col]

def setPiece(x, y, piece):
    board = read_board()
    row = 8 - x
    col = ord(y.upper()) - ord('A')
    board[row][col] = piece
    write_board(board)

def checkMove(sx, sy, ex, ey, role):
    def col_to_num(c): return ord(c.upper()) - ord('A') + 1
    dest = getPiece(ex, ey)
    if dest != 'nn' and dest[0] == role[0]:
        return False
    sx, ex = int(sx), int(ex)
    sy_n, ey_n = col_to_num(sy), col_to_num(ey)
    dx, dy = ex - sx, ey_n - sy_n
    adx, ady = abs(dx), abs(dy)
    piece = role[1]
    def path_clear(step_x, step_y):
        x, y = sx + step_x, sy_n + step_y
        while (x, y) != (ex, ey_n):
            if getPiece(x, chr(y + ord('A') - 1)) != 'nn':
                return False
            x += step_x
            y += step_y
        return True
    if piece == 'R':
        if dx != 0 and dy != 0:
            return False
        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
        return path_clear(step_x, step_y)
    if piece == 'B':
        if adx != ady:
            return False
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        return path_clear(step_x, step_y)
    if piece == 'Q':
        if not (dx == 0 or dy == 0 or adx == ady):
            return False
        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
        return path_clear(step_x, step_y)
    if piece == 'N':
        return (adx, ady) in [(1, 2), (2, 1)]
    if piece == 'K':
        return max(adx, ady) == 1
    if piece == 'P':
        direction = 1 if role[0] == 'w' else -1
        if dx == direction and dy == 0 and dest == 'nn':
            return True
        start_row = 2 if role[0] == 'w' else 7
        if sx == start_row and dx == 2 * direction and dy == 0:
            mid = getPiece(sx + direction, sy)
            if mid == 'nn' and dest == 'nn':
                return True
            return False
        if dx == direction and ady == 1 and dest != 'nn' and dest[0] != role[0]:
            return True
        return False
    return False

def tryMove(x, y):
    sy = x[0]
    sx = int(x[1])
    ey = y[0]
    ex = int(y[1])
    piece = getPiece(sx, sy)
    if piece == 'nn':
        return 'FAIL-起始位置没有棋子'
    if not checkMove(sx, sy, ex, ey, piece):
        return 'FAIL-走法不合法'
    dest = getPiece(ex, ey)
    setPiece(ex, ey, piece)
    setPiece(sx, sy, 'nn')
    if dest != 'nn' and dest[1] == 'K':
        if dest[0] == 'w':
            return 'BLACK WIN'
        else:
            return 'WHITE WIN'
    return 'OK'

def updateReadme():
    readme = ''
    with open('./README.head.md', 'r', encoding='utf-8') as f:
        readme += f.read()
    with open('./README.chess.md', 'r', encoding='utf-8') as f:
        readme += f.read()
    with open('./chess-games/chess.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        cnt = 8
        for line in lines:
            pieces = line.split('|')
            row = 'a'
            for piece in pieces:
                piece = piece[:2]
                to = f'![](./chess-images/{piece}.svg)'
                readme = readme.replace(f'[{row}{cnt}]', to)
                row = chr(ord(row) + 1)
            cnt -= 1
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(readme)