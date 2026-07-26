# 122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-26, 3min, ok)

### 考えたこと
- #121 の hold/not_hold パターンをベースに、取引回数無制限の違いを反映
- hold（保有中の損益）の更新式が `-price` → `not_hold - price` に変わる
- 「今日売って得た利益（not_hold）を元手に、同じ日にまた買い直せる」を表現するため、not_hold を先に更新してから hold の計算に使う

### 実装
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        not_hold = 0

        for price in prices[1:]:
            not_hold = max(not_hold, hold + price)
            hold = max(hold, not_hold - price)
        return not_hold
```

## references

### ref1: olsen-blue — 貪欲法（上がる区間の差分を全部足す）
https://github.com/olsen-blue/Arai60/pull/38

```python
max_profit = 0
yesterday_price = prices[0]

for i in range(1, len(prices)):
    today_price = prices[i]
    if yesterday_price < today_price:
        max_profit += today_price - yesterday_price
    yesterday_price = today_price

return max_profit
```

「複数の小さい上昇の合計 = 大きい上昇1回分」という数学的事実を使い、上がる日の差分だけ足す。ただし取引回数制限がある版（#123, #188）ではこの貪欲法は使えず、状態DPが必要になる。

> (レビュー) `if` 文 vs `max(today_price - yesterday_price, 0)` は好みの問題、両方OK。

### ref2: olsen-blue — 2次元配列版の状態DP
https://github.com/olsen-blue/Arai60/pull/38

```python
HOLD_STOCK = 1
NOT_HOLD_STOCK = 0
profits = [[0] * 2 for _ in range(len(prices))]
# profits[i][HOLD_STOCK] / profits[i][NOT_HOLD_STOCK] で状態を管理
return profits[-1][NOT_HOLD_STOCK]
```

> (レビュー) 2次元配列より「2本の変数」の方が読みやすい可能性がある（今回のあなたの実装がまさにこちら）。
> (レビュー) 株保有状態（HOLD_STOCK）は最終的な最大利益にならないため、返り値は NOT_HOLD_STOCK のみで十分。

## 参考
- https://github.com/olsen-blue/Arai60/pull/38 (olsen-blue — 122. Best Time to Buy and Sell Stock II)
- https://github.com/fuga-98/arai60/pull/38 (fuga-98 — 122. Best Time to Buy and Sell Stock II)
- https://github.com/mamo3gr/arai60/pull/36 (mamo3gr — 122. Best Time to Buy and Sell Stock II)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/53 (Yoshiki-Iwasa — 122. Best Time to Buy and Sell Stock II)
- https://github.com/rimokem/arai60/pull/38 (rimokem — 122. Best Time to Buy and Sell Stock II)
