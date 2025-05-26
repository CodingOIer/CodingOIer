import os
import shutil

import chess


def init():
    os.remove('./chess-games/chess.txt')
    shutil.copy('./chess-games/init.txt', './chess-games/chess.txt')
    with open('./chess-games/must.txt', 'w', encoding='utf-8') as f:
        f.write('w')
    with open('./chess-games/end.txt', 'w', encoding='utf-8') as f:
        f.write('false')
    chess.updateReadme()


if __name__ == '__main__':
    init()
