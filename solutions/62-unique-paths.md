# 62. Unique Paths
https://leetcode.com/problems/unique-paths/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-23, 10min, ok)

### 考えたこと
-

### 実装
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        return grid[m - 1][n - 1]
```

## Step 2 (2026-07-23)

### 考えたこと
- 1D DP で空間 O(n) に削減
- 各行の更新は前の行と現在行の左だけ使うので2次元配列不要
- `dp[col] += dp[col-1]` = 上からの値（前の行の dp[col]）+ 左からの値（dp[col-1]）

### 実装
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]
        return dp[-1]
```

## references

### ref1: olsen-blue — 2D DP（変数名の議論 + ループの書き方）
https://github.com/olsen-blue/Arai60/pull/33

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_of_paths = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                num_of_paths[r][c] = num_of_paths[r-1][c] + num_of_paths[r][c-1]
        return num_of_paths[m-1][n-1]
```

> (philip82148) `m` と `n` は何を表すか不明なので `num_rows` / `num_cols` が推奨。
> (hroc135) `range(1, n)` にすれば `if c == 0` の分岐が不要になる。

### ref2: olsen-blue — メモ化再帰
https://github.com/olsen-blue/Arai60/pull/33

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def helper(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            result = helper(r+1, c) + helper(r, c+1)
            cache[(r, c)] = result
            return result
        return helper(0, 0)
```

### ref3: mamo3gr — 2D配列の初期化の罠
https://github.com/mamo3gr/arai60/pull/31

> (oda) `[[0] * n] * m` は「同じリストオブジェクトを m 個参照する」だけになる。`[row[:] for row in ...]` か内包表記で作る必要がある。これでも動くことがあるのが「とても嫌な動き方」。

### ref4: Yoshiki-Iwasa — 数学解法（組み合わせ論）
https://github.com/Yoshiki-Iwasa/Arai60/pull/47

全移動回数は `m+n-2` 回、そのうち下移動が `m-1` 回 → C(m+n-2, m-1) で求まる。

```python
from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
```

> (rimokem) 数学解法はエレガントだが、integer overflow に注意（Python は問題なし）。

## 参考
- https://github.com/olsen-blue/Arai60/pull/33 (olsen-blue — 62. Unique Paths)
- https://github.com/fuga-98/arai60/pull/33 (fuga-98 — 62. Unique Paths)
- https://github.com/mamo3gr/arai60/pull/31 (mamo3gr — 62. Unique Paths)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/47 (Yoshiki-Iwasa — 62. Unique Paths)
- https://github.com/rimokem/arai60/pull/33 (rimokem — 62. Unique Paths)
