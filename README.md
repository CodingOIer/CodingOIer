
## CodingOIer 的社区国际象棋锦标赛

[**English Version**](#codingoiers-community-chess-championship)

当前状态：正在对局

下一步需白棋走棋。

参与方法：

- 点击下面的任意一个棋子，跳转到对应页面后再点击想要移动到的位置。

- 如果结束，可以点击 [重置](https://github.com/CodingOIer/CodingOIer/issues/new?title=%21init&body=%E9%80%9A%E5%B8%B8%EF%BC%8C%E4%BD%A0%E5%8F%AA%E9%9C%80%E8%A6%81%E7%82%B9%E5%87%BB%E5%8F%B3%E4%B8%8B%E6%96%B9%E7%9A%84%20Create%20%E6%8C%89%E9%92%AE%E5%8D%B3%E5%8F%AF%E5%8F%91%E9%80%81%E8%AF%B7%E6%B1%82%EF%BC%8C%E7%AD%89%E5%BE%85%E5%8D%81%E5%87%A0%E7%A7%92%E6%9B%B4%E6%94%B9%E5%B0%B1%E4%BC%9A%E6%98%BE%E7%A4%BA%E5%9C%A8%E6%A3%8B%E7%9B%98%E4%B8%8A%EF%BC%8C%E5%A6%82%E6%9E%9C%E9%A1%BA%E6%89%8B%EF%BC%8C%E8%AF%B7%E4%BD%A0%E9%A1%BA%E4%BE%BF%E7%82%B9%E5%87%BB%E5%90%8E%E9%9D%A2%E4%BC%9A%E5%87%BA%E7%8E%B0%E7%9A%84%20Close%20Issue%20%E6%9D%A5%E5%85%B3%E9%97%AD%E6%AD%A4%E8%AE%AE%E9%A2%98%0A%0A%5B%E8%BF%94%E5%9B%9E%E6%A3%8B%E7%9B%98%E9%A1%B5%E9%9D%A2%5D%28https%3A//github.com/CodingOIer%23codingoier-%25E7%259A%2584%25E7%25A4%25BE%25E5%258C%25BA%25E5%259B%25BD%25E9%2599%2585%25E8%25B1%25A1%25E6%25A3%258B%25E9%2594%25A6%25E6%25A0%2587%25E8%25B5%259B%29%0A%0AUsually%2C%20you%20only%20need%20to%20click%20the%20Create%20button%20in%20the%20lower%20right%20corner%20to%20send%20the%20request.%20Wait%20for%20more%20than%20ten%20seconds%20for%20the%20changes%20to%20appear%20on%20the%20board.%20If%20it%20goes%20smoothly%2C%20please%20click%20the%20Close%20Issue%20button%20that%20will%20appear%20later%20to%20close%20this%20issue.%0A%0A%5BReturn%20to%20the%20board%20page%5D%28https%3A//github.com/CodingOIer%23codingoiers-community-chess-championship%29)。

或者手动提交 Issue：

> 在本 [repo](https://github.com/CodingOIer/CodingOIer) 的 [Issue](https://github.com/CodingOIer/CodingOIer/issues) 界面提交一个新的 Issue，标题如下：
>
> - `!move|<需要移动的棋子位置>|<想要移动到的位置>` 来移动棋子，如 `!move|A2|A4`。
>
> - `!init` 来重置棋盘，当且仅当棋局结束可以使用。

下棋逻辑实现比较简陋，部分特殊移动方式可能无法使用，**需要吃掉对方的王才算胜利**。

到达对方底线的兵将被自动升变为后，暂不支持自行决定。

可以查看 git log / [`documents/log.md`](https://github.com/CodingOIer/CodingOIer/blob/game/documents/log.md) 获取结果，或直接查看下面的棋盘。

如果遇到问题，请发送邮件到 `i@wanghongtian.com` 或提交 Issue，但是由于 Issue 可能堆积，有可能无法看到。

同样的，欢迎 PR。

|       |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | [![](./chess-images/bR.svg)](./chess-links/a8.md)  | [![](./chess-images/nn.svg)](./chess-links/b8.md)  | [![](./chess-images/bB.svg)](./chess-links/c8.md)  | [![](./chess-images/bQ.svg)](./chess-links/d8.md)  | [![](./chess-images/bK.svg)](./chess-links/e8.md)  | [![](./chess-images/bB.svg)](./chess-links/f8.md)  | [![](./chess-images/bN.svg)](./chess-links/g8.md)  | [![](./chess-images/bR.svg)](./chess-links/h8.md)  |
| **7** | [![](./chess-images/bP.svg)](./chess-links/a7.md)  | [![](./chess-images/bP.svg)](./chess-links/b7.md)  | [![](./chess-images/bP.svg)](./chess-links/c7.md)  | [![](./chess-images/bP.svg)](./chess-links/d7.md)  | [![](./chess-images/bP.svg)](./chess-links/e7.md)  | [![](./chess-images/bP.svg)](./chess-links/f7.md)  | [![](./chess-images/bP.svg)](./chess-links/g7.md)  | [![](./chess-images/bP.svg)](./chess-links/h7.md)  |
| **6** | [![](./chess-images/nn.svg)](./chess-links/a6.md)  | [![](./chess-images/nn.svg)](./chess-links/b6.md)  | [![](./chess-images/bN.svg)](./chess-links/c6.md)  | [![](./chess-images/nn.svg)](./chess-links/d6.md)  | [![](./chess-images/nn.svg)](./chess-links/e6.md)  | [![](./chess-images/nn.svg)](./chess-links/f6.md)  | [![](./chess-images/nn.svg)](./chess-links/g6.md)  | [![](./chess-images/nn.svg)](./chess-links/h6.md)  |
| **5** | [![](./chess-images/nn.svg)](./chess-links/a5.md)  | [![](./chess-images/nn.svg)](./chess-links/b5.md)  | [![](./chess-images/nn.svg)](./chess-links/c5.md)  | [![](./chess-images/nn.svg)](./chess-links/d5.md)  | [![](./chess-images/nn.svg)](./chess-links/e5.md)  | [![](./chess-images/nn.svg)](./chess-links/f5.md)  | [![](./chess-images/nn.svg)](./chess-links/g5.md)  | [![](./chess-images/nn.svg)](./chess-links/h5.md)  |
| **4** | [![](./chess-images/nn.svg)](./chess-links/a4.md)  | [![](./chess-images/nn.svg)](./chess-links/b4.md)  | [![](./chess-images/nn.svg)](./chess-links/c4.md)  | [![](./chess-images/nn.svg)](./chess-links/d4.md)  | [![](./chess-images/nn.svg)](./chess-links/e4.md)  | [![](./chess-images/wP.svg)](./chess-links/f4.md)  | [![](./chess-images/nn.svg)](./chess-links/g4.md)  | [![](./chess-images/nn.svg)](./chess-links/h4.md)  |
| **3** | [![](./chess-images/nn.svg)](./chess-links/a3.md)  | [![](./chess-images/nn.svg)](./chess-links/b3.md)  | [![](./chess-images/nn.svg)](./chess-links/c3.md)  | [![](./chess-images/nn.svg)](./chess-links/d3.md)  | [![](./chess-images/nn.svg)](./chess-links/e3.md)  | [![](./chess-images/nn.svg)](./chess-links/f3.md)  | [![](./chess-images/nn.svg)](./chess-links/g3.md)  | [![](./chess-images/nn.svg)](./chess-links/h3.md)  |
| **2** | [![](./chess-images/wP.svg)](./chess-links/a2.md)  | [![](./chess-images/wP.svg)](./chess-links/b2.md)  | [![](./chess-images/wP.svg)](./chess-links/c2.md)  | [![](./chess-images/wP.svg)](./chess-links/d2.md)  | [![](./chess-images/wP.svg)](./chess-links/e2.md)  | [![](./chess-images/nn.svg)](./chess-links/f2.md)  | [![](./chess-images/wP.svg)](./chess-links/g2.md)  | [![](./chess-images/wP.svg)](./chess-links/h2.md)  |
| **1** | [![](./chess-images/wR.svg)](./chess-links/a1.md)  | [![](./chess-images/wN.svg)](./chess-links/b1.md)  | [![](./chess-images/wB.svg)](./chess-links/c1.md)  | [![](./chess-images/wQ.svg)](./chess-links/d1.md)  | [![](./chess-images/wK.svg)](./chess-links/e1.md)  | [![](./chess-images/wB.svg)](./chess-links/f1.md)  | [![](./chess-images/wN.svg)](./chess-links/g1.md)  | [![](./chess-images/wR.svg)](./chess-links/h1.md)  |

## CodingOIer's Community Chess Championship

[**中文版本**](#codingoier-的社区国际象棋锦标赛)

Current status: PLAYING

The next step requires WHITE chess moves.

How to participate:

- Click on any of the chess pieces below to jump to the corresponding page and then click on the position you want to move to.

- If end, you can click [Reset](https://github.com/CodingOIer/CodingOIer/issues/new?title=%21init&body=%E9%80%9A%E5%B8%B8%EF%BC%8C%E4%BD%A0%E5%8F%AA%E9%9C%80%E8%A6%81%E7%82%B9%E5%87%BB%E5%8F%B3%E4%B8%8B%E6%96%B9%E7%9A%84%20Create%20%E6%8C%89%E9%92%AE%E5%8D%B3%E5%8F%AF%E5%8F%91%E9%80%81%E8%AF%B7%E6%B1%82%EF%BC%8C%E7%AD%89%E5%BE%85%E5%8D%81%E5%87%A0%E7%A7%92%E6%9B%B4%E6%94%B9%E5%B0%B1%E4%BC%9A%E6%98%BE%E7%A4%BA%E5%9C%A8%E6%A3%8B%E7%9B%98%E4%B8%8A%EF%BC%8C%E5%A6%82%E6%9E%9C%E9%A1%BA%E6%89%8B%EF%BC%8C%E8%AF%B7%E4%BD%A0%E9%A1%BA%E4%BE%BF%E7%82%B9%E5%87%BB%E5%90%8E%E9%9D%A2%E4%BC%9A%E5%87%BA%E7%8E%B0%E7%9A%84%20Close%20Issue%20%E6%9D%A5%E5%85%B3%E9%97%AD%E6%AD%A4%E8%AE%AE%E9%A2%98%0A%0A%5B%E8%BF%94%E5%9B%9E%E6%A3%8B%E7%9B%98%E9%A1%B5%E9%9D%A2%5D%28https%3A//github.com/CodingOIer%23codingoier-%25E7%259A%2584%25E7%25A4%25BE%25E5%258C%25BA%25E5%259B%25BD%25E9%2599%2585%25E8%25B1%25A1%25E6%25A3%258B%25E9%2594%25A6%25E6%25A0%2587%25E8%25B5%259B%29%0A%0AUsually%2C%20you%20only%20need%20to%20click%20the%20Create%20button%20in%20the%20lower%20right%20corner%20to%20send%20the%20request.%20Wait%20for%20more%20than%20ten%20seconds%20for%20the%20changes%20to%20appear%20on%20the%20board.%20If%20it%20goes%20smoothly%2C%20please%20click%20the%20Close%20Issue%20button%20that%20will%20appear%20later%20to%20close%20this%20issue.%0A%0A%5BReturn%20to%20the%20board%20page%5D%28https%3A//github.com/CodingOIer%23codingoiers-community-chess-championship%29).

Or submit an issue manually:

> Submit a new issue in the [Issue](https://github.com/CodingOIer/CodingOIer) interface of this [repo](https://github.com/CodingOIer/CodingOIer) in the title format:
>
> - `!move|<position of chess piece to be moved>|<position to be moved>` to move chess pieces, such as `!move|A2|A4`.
>
> - `!init` to reset the chessboard, which can be used only when the game is over.

The logic of chess is relatively simple, and some special moves may not be available. **You need to capture the opponent's king to win**.

Pawns that reach the opponent's bottom line will be automatically promoted to the back, and you can't decide for yourself at this time.

You can check git log / [`documents/log.md`](https://github.com/CodingOIer/CodingOIer/blob/game/documents/log.md) to get the results, or just look at the board below.

If you encounter any problems, please send an email to `i@wanghongtian.com` or submit an issue, but since issues may be piled up, they may not be visible.

Likewise, PRs are welcome.

|       |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | [![](./chess-images/bR.svg)](./chess-links/a8.md)  | [![](./chess-images/nn.svg)](./chess-links/b8.md)  | [![](./chess-images/bB.svg)](./chess-links/c8.md)  | [![](./chess-images/bQ.svg)](./chess-links/d8.md)  | [![](./chess-images/bK.svg)](./chess-links/e8.md)  | [![](./chess-images/bB.svg)](./chess-links/f8.md)  | [![](./chess-images/bN.svg)](./chess-links/g8.md)  | [![](./chess-images/bR.svg)](./chess-links/h8.md)  |
| **7** | [![](./chess-images/bP.svg)](./chess-links/a7.md)  | [![](./chess-images/bP.svg)](./chess-links/b7.md)  | [![](./chess-images/bP.svg)](./chess-links/c7.md)  | [![](./chess-images/bP.svg)](./chess-links/d7.md)  | [![](./chess-images/bP.svg)](./chess-links/e7.md)  | [![](./chess-images/bP.svg)](./chess-links/f7.md)  | [![](./chess-images/bP.svg)](./chess-links/g7.md)  | [![](./chess-images/bP.svg)](./chess-links/h7.md)  |
| **6** | [![](./chess-images/nn.svg)](./chess-links/a6.md)  | [![](./chess-images/nn.svg)](./chess-links/b6.md)  | [![](./chess-images/bN.svg)](./chess-links/c6.md)  | [![](./chess-images/nn.svg)](./chess-links/d6.md)  | [![](./chess-images/nn.svg)](./chess-links/e6.md)  | [![](./chess-images/nn.svg)](./chess-links/f6.md)  | [![](./chess-images/nn.svg)](./chess-links/g6.md)  | [![](./chess-images/nn.svg)](./chess-links/h6.md)  |
| **5** | [![](./chess-images/nn.svg)](./chess-links/a5.md)  | [![](./chess-images/nn.svg)](./chess-links/b5.md)  | [![](./chess-images/nn.svg)](./chess-links/c5.md)  | [![](./chess-images/nn.svg)](./chess-links/d5.md)  | [![](./chess-images/nn.svg)](./chess-links/e5.md)  | [![](./chess-images/nn.svg)](./chess-links/f5.md)  | [![](./chess-images/nn.svg)](./chess-links/g5.md)  | [![](./chess-images/nn.svg)](./chess-links/h5.md)  |
| **4** | [![](./chess-images/nn.svg)](./chess-links/a4.md)  | [![](./chess-images/nn.svg)](./chess-links/b4.md)  | [![](./chess-images/nn.svg)](./chess-links/c4.md)  | [![](./chess-images/nn.svg)](./chess-links/d4.md)  | [![](./chess-images/nn.svg)](./chess-links/e4.md)  | [![](./chess-images/wP.svg)](./chess-links/f4.md)  | [![](./chess-images/nn.svg)](./chess-links/g4.md)  | [![](./chess-images/nn.svg)](./chess-links/h4.md)  |
| **3** | [![](./chess-images/nn.svg)](./chess-links/a3.md)  | [![](./chess-images/nn.svg)](./chess-links/b3.md)  | [![](./chess-images/nn.svg)](./chess-links/c3.md)  | [![](./chess-images/nn.svg)](./chess-links/d3.md)  | [![](./chess-images/nn.svg)](./chess-links/e3.md)  | [![](./chess-images/nn.svg)](./chess-links/f3.md)  | [![](./chess-images/nn.svg)](./chess-links/g3.md)  | [![](./chess-images/nn.svg)](./chess-links/h3.md)  |
| **2** | [![](./chess-images/wP.svg)](./chess-links/a2.md)  | [![](./chess-images/wP.svg)](./chess-links/b2.md)  | [![](./chess-images/wP.svg)](./chess-links/c2.md)  | [![](./chess-images/wP.svg)](./chess-links/d2.md)  | [![](./chess-images/wP.svg)](./chess-links/e2.md)  | [![](./chess-images/nn.svg)](./chess-links/f2.md)  | [![](./chess-images/wP.svg)](./chess-links/g2.md)  | [![](./chess-images/wP.svg)](./chess-links/h2.md)  |
| **1** | [![](./chess-images/wR.svg)](./chess-links/a1.md)  | [![](./chess-images/wN.svg)](./chess-links/b1.md)  | [![](./chess-images/wB.svg)](./chess-links/c1.md)  | [![](./chess-images/wQ.svg)](./chess-links/d1.md)  | [![](./chess-images/wK.svg)](./chess-links/e1.md)  | [![](./chess-images/wB.svg)](./chess-links/f1.md)  | [![](./chess-images/wN.svg)](./chess-links/g1.md)  | [![](./chess-images/wR.svg)](./chess-links/h1.md)  |
