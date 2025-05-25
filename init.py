import os
import shutil

import chess


os.remove('./chess-games/chess.txt')
shutil.copy('./chess-games/init.txt', './chess-games/chess.txt')
with open('./chess-games/must.txt', 'w') as f:
    f.write('w')

chess.updateReadme()