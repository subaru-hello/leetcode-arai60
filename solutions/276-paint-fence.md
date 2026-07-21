# 276. Paint Fence
https://leetcode.com/problems/paint-fence/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-20, 10min, ok)

### 考えたこと
- 前と同じか、違うかを考えていく。

### 実装
```python
class Solution:
  def numWays(self, n: int, k: int) -> int:
    if n == 0: return 0
    if n == 1: return k

    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * k

    for i in range(3, n + 1):
      dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n]
```

## Step 2 (2026-07-22)

dp 配列 O(N) → `prev1`/`prev2` の2変数で O(1) 空間に整形。
ロジックは同じで、配列を持たず直前2つの値だけ保持する。

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n == 1: return k

        prev2 = k        # dp[1]
        prev1 = k * k    # dp[2]

        for _ in range(3, n + 1):
            prev2, prev1 = prev1, (k - 1) * (prev1 + prev2)

        return prev1
```

## references

### Python標準ライブラリ活用 (list)
https://docs.python.org/3/library/stdtypes.html#list

```python
# リスト内包表記で dp 配列を一括初期化するパターン。
# dp[0] = k, dp[1] = k*k, dp[i] = (k-1)*(dp[i-1]+dp[i-2])
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        dp = [0] * n
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n - 1]
```

```python

class Solution:
  def numWays(self, n: int, k: int) -> int:
    if n == 1:
      return k
    num_ways = [0] * n
    num_ways[1] = k
    num_ways[2] = k * k

    for i in range(3, n + 1):
      num_ways[i] = (k - 1) * (num_ways[i - 1] + num_ways[i - 2])

    return num_ways[-1]

```

## 参考
- https://github.com/olsen-blue/Arai60/pull/30 (olsen-blue — 276. Paint Fence)
- https://github.com/mamo3gr/arai60/pull/57 (mamo3gr — 276. Paint Fence)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/44 (Yoshiki-Iwasa — 276. Paint Fence)
- https://github.com/rimokem/arai60/pull/30 (rimokem — 276. Paint Fence)
