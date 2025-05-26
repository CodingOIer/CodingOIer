import os
import shutil
import chess
import datetime


def appendLog(content):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('./documents/log.md', 'r') as f:
        log = f.read()
    log = f'`{time}`：{content}\n\n' + log
    log = log[:10000]
    with open('./documents/log.md', 'w') as f:
        f.write(log)


def init():
    os.remove('./chess-games/chess.txt')
    shutil.copy('./chess-games/init.txt', './chess-games/chess.txt')
    with open('./chess-games/must.txt', 'w', encoding='utf-8') as f:
        f.write('w')
    with open('./chess-games/end.txt', 'w', encoding='utf-8') as f:
        f.write('false')
    chess.updateReadme()


if __name__ == '__main__':
    appendLog('手动重置棋盘')
    init()
