import urllib.parse
import datetime


def appendLog(content):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('./documents/log.md', 'r') as f:
        log = f.read()
    log = f'`{time}`：{content}\n\n' + log
    log = log[:100000]
    with open('./documents/log.md', 'w') as f:
        f.write(log)


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

    def col_to_num(c):
        return ord(c.upper()) - ord('A') + 1

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
    must = open('./chess-games/must.txt', 'r', encoding='utf-8').read()[0]
    if must != piece[0]:
        return f'FAIL-下一步需{'白' if must == 'w' else '黑'}棋走棋'
    if not checkMove(sx, sy, ex, ey, piece):
        return 'FAIL-走法不合法'
    dest = getPiece(ex, ey)
    setPiece(ex, ey, piece)
    if (ex == 1 or ex == 8) and piece[1] == 'P':
        appendLog(f'前往 {ey}{ex} 的棋子为兵，升变为了后')
        setPiece(ex, ey, 'wQ' if piece == 'wP' else 'bQ')
    setPiece(sx, sy, 'nn')
    must = open('./chess-games/must.txt', 'w', encoding='utf-8').write(
        'b' if must == 'w' else 'w'
    )
    if dest != 'nn' and dest[1] == 'K':
        if dest[0] == 'w':
            return 'BLACK WIN'
        else:
            return 'WHITE WIN'
    return 'OK'


def urlEncode(text):
    return urllib.parse.quote(text)


def getIssue(title):
    return f'https://github.com/CodingOIer/CodingOIer/issues/new?title={urlEncode(title)}&body={urlEncode(open('./documents/issue-body.md').read())}'


def genLink(id):
    link = open('./documents/link-init.md').read()
    with open('./chess-games/chess.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        cnt = 8
        for line in lines:
            pieces = line.split('|')
            row = 'a'
            for piece in pieces:
                piece = piece[:2]
                to = f'[![](../chess-images/{piece}.svg)]({getIssue(f'!move|{id.upper()}|{row.upper()}{cnt}')})'
                link = link.replace(f'[{row}{cnt}]', to)
                row = chr(ord(row) + 1)
            cnt -= 1
    open(f'./chess-links/{id.lower()}.md', 'w', encoding='utf-8').write(link)


def updateReadme():
    readme = ''
    with open('./documents/README.head.md', 'r', encoding='utf-8') as f:
        readme += f.read()
    with open('./documents/README.chess.md', 'r', encoding='utf-8') as f:
        readme += f.read()
    with open('./chess-games/chess.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        cnt = 8
        for line in lines:
            pieces = line.split('|')
            row = 'a'
            for piece in pieces:
                genLink(f'{row}{cnt}')
                piece = piece[:2]
                to = f'[![](./chess-images/{piece}.svg)](./chess-links/{row}{cnt}.md)'
                readme = readme.replace(f'[{row}{cnt}]', to)
                row = chr(ord(row) + 1)
            cnt -= 1
    readme = readme.replace(
        '[must]', '白' if open('./chess-games/must.txt').read()[0] == 'w' else '黑'
    )
    readme = readme.replace(
        '[must-en]',
        'WHITE' if open('./chess-games/must.txt').read()[0] == 'w' else 'BLACK',
    )
    readme = readme.replace(
        '[status]',
        (
            '正在对局'
            if open('./chess-games/end.txt').read() == 'false'
            else (
                '白棋胜利'
                if open('./chess-games/must.txt').read()[0] == 'b'
                else '黑棋胜利'
            )
        ),
    )
    readme = readme.replace(
        '[status-en]',
        (
            'PLAYING'
            if open('./chess-games/end.txt').read() == 'false'
            else (
                'White Wins'
                if open('./chess-games/must.txt').read()[0] == 'b'
                else 'Black Wins'
            )
        ),
    )
    readme = readme.replace('[issue-reset]', getIssue('!init'))
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
