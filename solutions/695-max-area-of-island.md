# 695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-02, 55 min, ok)

### 1-A: 自力で考えたこと
- データ構造案: grid をそのまま使い、訪問済みは値を0に書き換えて管理（追加のvisited不要）
- アルゴリズム案: #200 Number of Islands と同じ DFS 型。カウントの代わりに面積を積算して return する形に変える。

### 1-B: 詰まった点
- 完全に自力では書けなかった。DFS の骨格（境界チェック→沈める→隣接4方向の再帰の合計をreturn）を思い出せず、1行ずつガイドを受けながら実装した。
- 「読んで理解した」と「実際にキーボードでタイプしてAC する」の間に大きな溝があると実感した回。

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

## 参考
- (このセッションの GitHub アクセスは自リポジトリに限定されており、他ユーザーの arai60 community PR は未取得。`/arai60 refs max-area-of-island` で Editorial / neetcode / 標準ライブラリを別途取得可能)
