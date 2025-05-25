import os
import shutil
import secrets

import chess


os.remove('./chess-games/chess.txt')
shutil.copy('./chess-games/init.txt', './chess-games/chess.txt')

with open('./chess-games/lock.txt', 'w', encoding='utf-8') as f:
    f.write(secrets.token_hex(4))

chess.updateReadme()