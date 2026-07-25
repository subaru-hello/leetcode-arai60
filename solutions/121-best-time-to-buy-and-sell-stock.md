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
