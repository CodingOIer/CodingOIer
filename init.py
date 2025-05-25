import os
import shutil

import chess


os.remove('./chess-games/chess.txt')
shutil.copy('./chess-games/init.txt', './chess-games/chess.txt')

chess.updateReadme()