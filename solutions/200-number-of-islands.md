# 200. Number of Islands
https://leetcode.com/problems/number-of-islands/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-21, 60min, △)
- スタックを使うだろうなとまずは思った。幅探索アルゴリズムと深さ探索アルゴリズムがある。
- 写経した。
- 入力パラメータを破壊しているので、もし破壊しないで書くとしたら、visited setを使うといいらしい。
> 'm modifying the input grid in place to save memory. If we need to preserve the input, I can use a separate visited set instead.
- 探索外の条件と、探索範囲を決める



```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.traverse_and_delete_one_island(grid, r, c, rows, cols)
                    count += 1
        return count

    def traverse_and_delete_one_island(self, grid, r, c, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        self.traverse_and_delete_one_island(grid, r+1, c, rows, cols)
        self.traverse_and_delete_one_island(grid, r-1, c, rows, cols)
        self.traverse_and_delete_one_island(grid, r, c+1, rows, cols)
        self.traverse_and_delete_one_island(grid, r, c-1, rows, cols)

```

### Step2
- せっかくなので、入力値を破壊しない方法も調べてみた

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island_counts = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.traverse_and_delete_island(grid, r, c, rows, cols, visited)
                    island_counts += 1
        return island_counts

    def traverse_and_delete_island(self, grid, row, col, rows, cols, visited):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 
        if (row, col) in visited:
            return
        if grid[row][col] != "1":
            return
        
        visited.add((row, col))
        self.traverse_and_delete_island(grid, row+1, col, rows, cols, visited)
        self.traverse_and_delete_island(grid, row-1, col, rows, cols, visited)
        self.traverse_and_delete_island(grid, row, col+1, rows, cols, visited)
        self.traverse_and_delete_island(grid, row, col-1, rows, cols, visited)
```

## 参考
- https://github.com/mamo3gr/arai60/pull/16
- https://github.com/olsen-blue/Arai60/pull/17
> https://github.com/Yoshiki-Iwasa/Arai60/pull/16
Rustで、UnionFind, bfs, dfsを使って書いていた。

> num_, sum_といったprefixは頻出する。スタイルガイドでは、原則省略形は避けるべきと書いてある。https://github.com/h-masder/Arai60/pull/18/changes#r3092788628

> - 自分で考える。書く前に時間計算量を見積もる(https://github.com/Yuto729/LeetCode_arai60/pull/16#discussion_r2602118324)。
> - エラーをはかずに3回解くようになるまで書いてみる。
> - 他の人のコードを見て、自分のコードと比較して修正する。

この方針はいいと思うのだが、写経中に眠くなって力尽きてしまう。。
「まだまだ、広い選択肢から比較検討してよさそうなものを選べるだけのスキル」を身につけるためには、まず考えうる解法を馴染ませて、状況に応じて使い分けるのがいいのだろうが、眠い。


- https://github.com/h-masder/Arai60/pull/18
- https://github.com/Shunii85/arai60/pull/17
