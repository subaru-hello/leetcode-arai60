# 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-25, 4min, ok)

### 考えたこと
- min_price = これまでの最安値、max_profit = これまでの最大利益
- 各 price で min_price を更新し、price - min_price を利益として計算
- #53 Maximum Subarray の累積和アプローチと同じ構造（谷底からの上昇幅の最大化）

### 実装
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = -math.inf

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
```

## Step 2 (2026-07-26)

### 考えたこと
- `hold`/`not_hold` の状態DPで解く（#122 に繋がる汎用パターン）
- `profit_holding` = 株を保有している状態での損益（買値をマイナスとして持つ）
- `max_profit_sold` = 売却した場合の最大利益（最終的な答え）
- 各日、「昨日までの hold で今日売ったら」を先に計算 → その後「今日買い直した方が得か」を更新（順序を守らないと過去の情報が消える）

### 実装
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_holding = -prices[0]
        max_profit_sold = 0

        for price in prices[1:]:
            max_profit_sold = max(max_profit_sold, profit_holding + price)
            profit_holding = max(profit_holding, -price)
        return max_profit_sold
```

## references

### ref1: olsen-blue — 配列版から始めて空間 O(1) に議論で気づくパターン
https://github.com/olsen-blue/Arai60/pull/37

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = [-math.inf] * len(prices)
        # ... 配列で各時点の最大利益を持つバージョン
```

> (liquo-rice) 空間計算量は定数に落とせる。リストではなく変数で持てば十分。
> (oda) `zip` や `itertools.accumulate` の活用も検討できる。
> (huyfififi) Maximum Subarray（#53）との類似性を指摘。「過去の最小値を管理すれば良さそう」。DP と呼べるか（依存関係のない貪欲計算では？）の議論も発生。

## 参考
- https://github.com/olsen-blue/Arai60/pull/37 (olsen-blue — 121. Best Time to Buy and Sell Stock)
- https://github.com/fuga-98/arai60/pull/37 (fuga-98 — 121. Best Time to Buy and Sell Stock)
- https://github.com/mamo3gr/arai60/pull/35 (mamo3gr — 121. Best Time to Buy and Sell Stock)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/52 (Yoshiki-Iwasa — 121. Best Time to Buy and Sell Stock)
- https://github.com/rimokem/arai60/pull/37 (rimokem — 121. Best Time to Buy and Sell Stock)
