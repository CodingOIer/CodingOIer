import sys
import chess
import datetime

def appendLog(content):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('./log.md', 'r') as f:
        log = f.read()
    log = f'`{time}`：{content}\n\n' + log
    log = log[:10000]
    with open('./log.md', 'w') as f:
        f.write(log)

title = sys.argv[1]
author = sys.argv[2]

if title[:7] != '!chess|':
    exit(0)

args = title.split('|')

x = args[1]
y = args[2]

response = chess.tryMove(x, y)
chess.updateReadme()

if response == 'OK' or response[:4] == 'FAIL':
    appendLog(f'{author} 移动棋子从 {x} 到 {y}，结果是 {response}')
elif response == 'BLACK WIN':
    appendLog(f'{author} 移动棋子从 {x} 到 {y}，黑棋胜利')
elif response == 'WHITE WIN':
    appendLog(f'{author} 移动棋子从 {x} 到 {y}，白棋胜利')