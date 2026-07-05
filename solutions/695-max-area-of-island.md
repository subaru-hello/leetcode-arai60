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

`dfs` って名前、面接では問題ないと思ってたけど実は微妙らしい。呼び出し元が知りたいのは「これがどうやって動くか」より「何が返ってくるか」なので、`dfs()` だと戻り値が想像つかない。`area_from(row, col)` みたいに直したい。

stack版とqueue版で結果が変わるのか気になったけど、面積を数えるだけなら訪れる順番はどうでもいいから答えは同じになる。順番が意味を持つのは最短距離・最小手数を聞かれる問題（#127 Word Ladderとか）のとき。今回はどっちでもいいから、`deque`がいらない分`stack`（list）の方が身軽。

`sr, sc, nr, nc, dr, dc` が最初さっぱり分からなかった。`sr/sc`=start row/col（出発点）、`r/c`=今処理中の座標、`nr/nc`=next row/col（隣接候補）、`dr/dc`=delta row/col（移動量）。グリッド探索だとほぼお決まりの略し方らしい。慣れるまではフルスペル（`started_row`, `next_row`, `row_delta`等）で書いていい。

自分でstack書いた版の方が再帰版よりごちゃごちゃしてるのはなぜか気になった。再帰は「次どこに行くか」をPythonの呼び出しスタックに丸投げできる。自分でstackを管理すると、その丸投げしてた部分を全部自分の手で書く必要が出てくるので、行数もネストも増える。書き方が下手なわけじゃなくて反復DFSに構造的についてくるコスト。反復版を使う理由は基本的に「再帰の深さ制限を避けたいとき」くらいで、その心配がないなら再帰版の方が素直。ネストを減らしたいなら「範囲チェック+追加」を `unvisited_land_neighbors(row, col)` みたいな関数に切り出す手もある。

## 参考

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

## Step 2 (2026-07-03, ≤10 min, ok)

Step1の内容を思い出しながら何も見ずに書き直したら2つバグを埋め込んでいた。

1つ目: `dfs` はクラスのメソッドじゃなくて `maxAreaOfIsland` の中に定義した関数（クロージャ）なのに `def dfs(self, row, col):` と書いてしまい、`dfs(r, c)` の呼び出しで引数が足りずエラーになった。ネストした関数には`self`はいらない、というのが体に入ってなかった。

2つ目: 境界チェックで `col <= cols` と書いていた。`col`は常に`cols`以下になるので、この条件は実質いつでも真になり、`dfs`が呼ばれた瞬間に毎回0を返して終わっていた。`>=`で書くべきところを`<=`にしていた単純な不等号ミス。

この2つを直して10分以内でAC。参考(ref-A)を見て、境界チェックの`grid[nr][nc] == 1`のところは今回はそのまま`== 1`で残した方が自分には読みやすいと感じたので変えなかった。

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return (1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, dfs(r, c))
        return best
```
