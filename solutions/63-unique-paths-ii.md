# 63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-24, 10min, ok)

### 考えたこと
前回と違い、gridが用意されている。
マスにアクセスできる条件は上からor左から、の２通り
上段のマスを事前に計算しておけば、ますにアクセスできる経路は左から計算すればいい
現在見ているマスに障害物が置いてあれば、そこへのアクセス経路を使用する予定はなくなるので0


### 実装
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])

        num_paths = [0] * num_cols
        num_paths[0] = 1

        for r in range(num_rows):
            for c in range(num_cols):
                if obstacleGrid[r][c] == 1:
                    num_paths[c] = 0
                elif c > 0:
                    num_paths[c] += num_paths[c - 1]
        return num_paths[-1]

```

## references

### ref1: olsen-blue — 2D DP（端の初期化を明示的に行うパターン）
https://github.com/olsen-blue/Arai60/pull/34

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        num_of_paths = [[0] * num_cols for _ in range(num_rows)]

        for c in range(num_cols):
            if obstacleGrid[0][c] == OBSTACLE:
                break
            num_of_paths[0][c] = 1
        for r in range(num_rows):
            if obstacleGrid[r][0] == OBSTACLE:
                break
            num_of_paths[r][0] = 1

        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if obstacleGrid[r][c] == OBSTACLE:
                    num_of_paths[r][c] = 0
                else:
                    num_of_paths[r][c] = num_of_paths[r-1][c] + num_of_paths[r][c-1]
        return num_of_paths[num_rows-1][num_cols-1]
```

> (philip82148) `OBSTACLE` はグローバル定数か `Solution` のクラス変数にする方が自然。
> (philip82148) `num_of_paths[r][c] = 0` は初期化済みなので不要。
> (hroc135) `r`, `c` で十分。Googleスタイルガイド「スコープサイズと使用頻度に比例」。

### ref2: rimokem — メモ化再帰 + 関数名の議論
https://github.com/rimokem/arai60/pull/34

```python
# メモ化再帰版のイメージ
def count_paths_to(row, col):
    if obstacleGrid[row][col] == 1:
        return 0
    if row == 0 and col == 0:
        return 1
    result = 0
    if row > 0:
        result += count_paths_to(row - 1, col)
    if col > 0:
        result += count_paths_to(row, col - 1)
    return result
```

> (h-masder) 関数名は `count_paths_to(num_rows-1, num_cols-1)` のように意図を表す名前がよい。
> (h-masder) メモリ制約が厳しくなければ grid 形式の方が可読性が上がる。

## 参考
- https://github.com/olsen-blue/Arai60/pull/34 (olsen-blue — 63. Unique Paths II)
- https://github.com/fuga-98/arai60/pull/34 (fuga-98 — 63. Unique Paths II)
- https://github.com/mamo3gr/arai60/pull/32 (mamo3gr — 63. Unique Paths II)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/49 (Yoshiki-Iwasa — 63. Unique Paths II)
- https://github.com/rimokem/arai60/pull/34 (rimokem — 63. Unique Paths II)
