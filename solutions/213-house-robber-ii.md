# 213. House Robber II
https://leetcode.com/problems/house-robber-ii/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-25, 2min, ok)

### 考えたこと
-

### 実装
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]):
            one_before_max = 0
            two_before_max = 0
            for num in houses:
                current_max = max(one_before_max, two_before_max + num)
                two_before_max = one_before_max
                one_before_max = current_max
            return one_before_max

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
```

## references

### ref1: olsen-blue — #198 を再利用するパターン
https://github.com/olsen-blue/Arai60/pull/36

> (レビュー) `return max(rob1(nums[:-1]), rob1(nums[1:]))` のように House Robber I の関数をそのまま呼ぶのがシンプル。

```python
# House Robber I を内部関数として再利用
def rob(self, nums: List[int]) -> int:
    def rob_linear(houses):
        two_before, one_before = 0, 0
        for num in houses:
            current = max(one_before, two_before + num)
            two_before = one_before
            one_before = current
        return one_before

    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

> (レビュー) スライスはコピーを作る（O(n) 空間）。`begin`/`end` の index 制御にすれば O(1) のまま。
> (レビュー) 変数名は `nums_without_init`/`nums_without_tail` より `nums_excluding_first`/`nums_excluding_last` が明確。
> (レビュー) エッジケースは `len <= 1` だけで十分。`<= 3` の特別処理は不要。

### ref2: olsen-blue — メモ化再帰（`@cache` デコレータ）
https://github.com/olsen-blue/Arai60/pull/36

```python
from functools import cache

def rob(self, nums: List[int]) -> int:
    @cache
    def max_amount_from(start, end, index):
        if index > end:
            return 0
        return max(
            nums[index] + max_amount_from(start, end, index + 2),
            max_amount_from(start, end, index + 1)
        )

    n = len(nums)
    if n == 1:
        return nums[0]
    return max(
        max_amount_from(0, n - 2, 0),
        max_amount_from(1, n - 1, 1)
    )
```

> (レビュー) 再帰ではないパターン（ボトムアップ）も練習すると良い。
> (レビュー) `@cache` は高階関数でラップするデコレータ — 仕組みを理解しておくと良い。

## 参考
- https://github.com/olsen-blue/Arai60/pull/36 (olsen-blue — 213. House Robber II)
- https://github.com/fuga-98/arai60/pull/36 (fuga-98 — 213. House Robber II)
- https://github.com/mamo3gr/arai60/pull/34 (mamo3gr — 213. House Robber II)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/51 (Yoshiki-Iwasa — 213. House Robber II)
- https://github.com/rimokem/arai60/pull/36 (rimokem — 213. House Robber II)
