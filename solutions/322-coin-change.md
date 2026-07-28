# 322. Coin Change
https://leetcode.com/problems/coin-change/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-28, 3min, ok)

### 考えたこと
- dp[i] = 「金額 i を作るのに必要な最小コイン枚数」
- dp[i] = min(dp[i], dp[i-coin] + 1) を全コインで試す。Word Break と違い、参照先がコインの額面によってバラバラなので配列全体が必要（House Robber のような2変数圧縮はできない）
- +1 は「今使ったコイン1枚」をカウントするため
- 初期値は float('inf')（まだ作る方法が見つかっていない、の意味）、dp[0]=0
- current_best / candidate に分解すると読みやすい

### 実装
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    current_best = dp[i]
                    candidate = dp[i - coin] + 1
                    dp[i] = min(current_best, candidate)

        if dp[amount] != float('inf'):
            return dp[amount]

        return -1
```

## references

### ref1: olsen-blue — 変数名の明確化 + BFS別解の議論
https://github.com/olsen-blue/Arai60/pull/40

```python
class Solution:
    def coinChange(self, coins: List[int], target_amount: int) -> int:
        min_num_coins = [math.inf] * (target_amount + 1)
        min_num_coins[0] = 0
        # coins[r-1] > c なら continue で早期スキップ
```

> (nittoco) `num_rows`/`num_cols` のような抽象変数より `len(coins)+1`/`amount+1` を直接使う方が意味が明確。
> (nittoco) `continue` の後に `else` は不要（continue した時点でその後の処理はスキップされるため）。

**BFS 別解も言及あり**: `amount` から `0` に向かって、各ステップでコインを引いていく「最短距離」問題として BFS で解く方法。DP と計算量は同じだが「最小回数」を求める問題は最短経路探索とも読み替えられる、という発想の転換。

> (hroc135) 初期値やカウントの数え方は「0枚から始める」方が直感的にわかりやすい場合がある。

## 参考
- https://github.com/olsen-blue/Arai60/pull/40 (olsen-blue — 322. Coin Change)
- https://github.com/fuga-98/arai60/pull/40 (fuga-98 — 322. Coin Change)
- https://github.com/mamo3gr/arai60/pull/38 (mamo3gr — 322. Coin Change)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/54 (Yoshiki-Iwasa — 322. Coin Change)
- https://github.com/rimokem/arai60/pull/40 (rimokem — 322. Coin Change)
