# 695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-02, 55 min, ok)

### 1-A: 自力で考えたこと
- 以前 #200 Number of Islands で DFS を使って「隣り合った島の数」を数えた記憶があり、「今回も同じでは？」と思った。
- 実際その直感は正しく、型は #200 と同じ DFS。差分は「カウントを+1する」代わりに「面積を積算して return する」だけだった。

### 1-B: 詰まった点
- 連続して隣り合った1（陸）を走査する方法が思いつかなかった。「同じ型では」と当たりはついたが、それを実際に「境界チェック→沈める→隣接4方向を再帰でたどる」というコードの形に落とし込む部分で手が止まった。
- 「読んで理解した」と「実際にキーボードでタイプしてAC する」の間に大きな溝があると実感した回。1行ずつガイドを受けながら実装した。

### 1-C: 自分が理解した解法
- `dfs(row, col)` は「そのセルを起点にした島の面積」を返す関数。
- 範囲外 or 海(0) なら 0 を返す（早期return）。
- 自分のマスを 0 に沈めてから、上下左右の `dfs` の結果 + 自分の1 を足して返す。
- 全マスを走査し、陸(1)を見つけるたびに `dfs` を呼び、面積の最大値を更新する。

### 1-D: 実装
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return (1
                      + dfs(row + 1, col)
                      + dfs(row - 1, col)
                      + dfs(row, col + 1)
                      + dfs(row, col - 1))

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, dfs(r, c))
        return best
```

計算量: 時間 O(rows × cols)、空間 O(rows × cols)（最悪ケースの再帰スタック）。

## 疑問・気づき（随時追記）

### Q. `dfs` という関数名は面接で問題ないか？
- 最初「問題ない」と回答したが誤り。典型コメント集に明記あり: `dfs()` は内部実装の分類名であり、呼び出し元は戻り値（何が返ってくるか）を知りたいのであって手法を知りたいわけではない。`area_from(row, col)` のように戻り値が想像できる名前が望ましい。

### Q. 反復DFS（stack版）とBFS（queue版）で結果は変わるか？
- 面積（マス数）を数えるだけなら**訪れる順番は結果に影響しない**ので、DFS/BFSどちらでも同じ答えになる。
- 順番が重要になるのは「最短距離・最小手数」を問う問題（#127 Word Ladder等）。その場合はBFS必須。
- 今回は順番が自由なので、実装がシンプルな方（Pythonでは`deque`不要な`list`+`stack`＝DFS）を選ぶのが合理的。

### Q. `sr, sc, nr, nc, dr, dc` のような略語は分かりにくい
- `sr/sc`=start row/col、`r/c`=処理中の座標、`nr/nc`=next row/col（隣接候補）、`dr/dc`=delta row/col（移動量）。
- グリッド探索問題ではほぼ世界共通の慣用表記（スコープが数行に限定され役割が変わらないため、典型コメント集の「一文字変数の許容条件」に合致）。ただし学習中はフルスペル（`started_row`, `next_row`, `row_delta`等）で書いて意味を1対1対応させるのも正当な手段。

### Q. なぜ反復版（stack）は再帰版よりネストが深く、`row`/`col`が頻出するのか？
- 再帰版は「次のマスに移る」を `dfs(row+1, col)` という関数呼び出し1行に圧縮できる。「今どこにいるか」の記憶をPythonの呼び出しスタックに任せているため。
- 反復版はその記憶を自前の`stack`（リスト）で明示的に管理する必要があり、座標の計算・保存・取り出しをすべて自分で書くためネストと変数の登場回数が増える。これは書き方が悪いのではなく反復DFSに構造的につきまとうコスト。
- 反復版を使う実務的な理由は「再帰の深さ制限（Python setrecursionlimit）を回避したいとき」のみ。その懸念がなければ再帰版の方が素直で読みやすい。
- ネストを減らす手として、「範囲チェック+追加」の繰り返しを `unvisited_land_neighbors(row, col)` のようなジェネレータ関数に切り出す方法がある（典型コメント集の#695への指摘: 「関数化・ラムダ化するといい」と一致）。

## 参考

**注**: このセッションの GitHub アクセスは自リポジトリ（subaru-hello/leetcode-arai60, n10u_org）に限定されており、arai60 コミュニティの Discord/PR には到達できなかった。代わりに一般公開の LeetCode 解法リポジトリを Web 検索で取得した。`/arai60 refs max-area-of-island` で Editorial / neetcode / 標準ライブラリを別途取得可能。

### ref-A: stack版DFS（qiyuangong/leetcode）
https://github.com/qiyuangong/leetcode/blob/master/python/695_Max_Area_of_Island.py

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(self.dfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i, j):
        stack = [(i, j)]
        area = 0
        while stack:
            r, c = stack.pop(-1)
            area += 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and grid[nr][nc]):
                    stack.append((nr, nc))
                    grid[nr][nc] = 0
        return area
```
**気づき**: 自分の実装と型はほぼ同じ。差分は「探索開始マスを沈める処理を外側のループでやってしまう」点（`dfs`を呼ぶ前に`grid[i][j] = 0`している）。また `grid[nr][nc]` を `== 1` と書かず、真偽値としてそのまま使っている（Pythonでは`1`は真、`0`は偽）。

### ref-B: queue版BFS（chenjienan/python-leetcode）
https://github.com/chenjienan/python-leetcode/blob/master/695.max-area-of-island.py

```python
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, self.bfs(grid, r, c))
        return res

    def bfs(self, grid, x, y):
        local_max = 1
        grid[x][y] = 0
        queue = deque([(x, y)])
        while queue:
            cur_x, cur_y = queue.popleft()
            for d_x, d_y in DIRECTIONS:
                nxt_x, nxt_y = cur_x + d_x, cur_y + d_y
                if (0 <= nxt_x < len(grid) and 0 <= nxt_y < len(grid[0])
                        and grid[nxt_x][nxt_y] == 1):
                    grid[nxt_x][nxt_y] = 0
                    queue.append((nxt_x, nxt_y))
                    local_max += 1
        return local_max
```
**気づき**: `DIRECTIONS` をクラス外の**モジュール定数**にしている（自分は関数内のローカル変数にしていた）。方向リストが複数のメソッドから使われる場合はこちらの方が自然。`local_max = 1`で開始マス自身を先に数えてから隣接を数える書き方（自分は`area = 0`で開始してループ内で+1する書き方）— どちらも正しいが「初期値をどう置くか」の選択が違う。
