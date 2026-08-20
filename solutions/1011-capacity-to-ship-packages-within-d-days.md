# 1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-31, 3min, ok)

### 考えたこと
- 「最小の capacity」を求める → 答えを二分探索するパターン（capacity が大きいほど運びやすい、という単調性がある）
- can_ship(capacity) = 「その capacity で days 日以内に運べるか」を判定する関数を分離（ベルトコンベアのように荷物を順番に積んでいくシミュレーション）
- 探索範囲: at_least = max(weights)（これ未満は物理的に不可能）、at_most = sum(weights)（確実に1日で運べる上限）
- can_ship(mid) が True のとき、mid はまだ答えの候補（もっと小さい値があるかも）なので at_most = mid（mid を含めたまま残す）。False のときは mid は答えになり得ないと確定するので at_least = mid + 1（除外）

### 実装
```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += weight
            return days_needed <= days

        at_least = max(weights)
        at_most = sum(weights)
        while at_least < at_most:
            mid = (at_least + at_most) // 2
            if can_ship(mid):
                at_most = mid
            else:
                at_least = mid + 1
        return at_least
```

## references

### ref1: olsen-blue — bisect_left(key=...) を使った境界探索
https://github.com/olsen-blue/Arai60/pull/44

```python
def is_loadable_capacity(capacity: int) -> bool:
    days_required = 1
    prefix_load = 0
    for weight in weights:
        prefix_load += weight
        if prefix_load > capacity:
            prefix_load = weight
            days_required += 1
    return days_required <= days

return bisect_left(range(sum(weights) + 1), True, lo=max(weights), key=is_loadable_capacity)
```

`range(sum(weights)+1)` を「仮想配列」に見立て、`bisect_left` の `key` 引数（Python 3.10+）に判定関数を渡すことで、「F,F,...,F,T,T,...,T の境界」を標準ライブラリの二分探索に丸投げできる。手動で `while` ループを書く必要がなくなる。

> (nodchip) この問題は「FF...FFTT...TTの境界を求める問題」と本質を一言で表現。
> (oda) `bisect_left(range(...), True, lo=..., key=...)` と書くのが最も自然、という提案。
> (hroc135) 型ヒントは引数だけでなく返り値にもつけて統一すべき。`lo`/`hi` より `low`/`high` の方が分かりやすい。

## 参考
- https://github.com/olsen-blue/Arai60/pull/44 (olsen-blue — 1011. Capacity To Ship Packages Within D Days)
- https://github.com/fuga-98/arai60/pull/44 (fuga-98 — 1011. Capacity To Ship Packages Within D Days)
- https://github.com/mamo3gr/arai60/pull/42 (mamo3gr — 1011. Capacity To Ship Packages Within D Days)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/37 (Yoshiki-Iwasa — 1011. Capacity To Ship Packages Within D Days)
- https://github.com/rimokem/arai60/pull/44 (rimokem — 1011. Capacity To Ship Packages Within D Days)
