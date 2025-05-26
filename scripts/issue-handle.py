import sys
import init
import chess
import datetime


def appendLog(content):
    open('./message.txt', 'w', encoding='utf-8').write(content)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('./documents/log.md', 'r') as f:
        log = f.read()
    log = f'`{time}`：{content}\n\n' + log
    log = log[:100000]
    with open('./documents/log.md', 'w') as f:
        f.write(log)


title = sys.argv[1]
author = sys.argv[2]

args = title.split('|')


def chessMove():

    x = args[1]
    y = args[2]

    response = chess.tryMove(x, y)

    if response == 'OK' or response[:4] == 'FAIL':
        appendLog(f'{author} 移动棋子从 {x} 到 {y}，结果是 {response}')
    elif response == 'BLACK WIN':
        appendLog(f'{author} 移动棋子从 {x} 到 {y}，黑棋胜利')
        open('./chess-games/end.txt', 'w', encoding='utf-8').write('true')
    elif response == 'WHITE WIN':
        appendLog(f'{author} 移动棋子从 {x} 到 {y}，白棋胜利')
        open('./chess-games/end.txt', 'w', encoding='utf-8').write('true')

    chess.updateReadme()


if __name__ == '__main__':
    end = open('./chess-games/end.txt', 'r', encoding='utf-8').read()

    if args[0] == '!move':
        if end == 'true':
            appendLog(f'{author} 移动棋子，但是棋局已经结束')
        else:
            chessMove()
    if args[0] == '!init':
        if end == 'false':
            appendLog(f'{author} 重置棋盘，但是棋局还未结束')
        else:
            appendLog(f'{author} 重置棋盘，成功')
            init.init()
