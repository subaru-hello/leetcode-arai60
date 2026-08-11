# 209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-08-11, 20min, △)

### 考えたこと
- Sliding Window。全部正の整数なので、window合計を1変数(running_sum)で持ち回れる（累積和配列は不要）
- right(index)を進めて合計に加算 → target以上になったら、left側から削れるだけ削りながら最小長さを更新
- 長さは right - left + 1（閉区間）。半開区間版（end=i+1）も検討したが、+1が別の場所に移動するだけで複雑さは変わらないため、標準的な閉区間版を採用
- left/rightのロジック（どちらを引く・どちらを進めるか）を何度か間違えたため、正直に△扱いで記録

### 実装
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float("inf")
        cummulated_sum = 0
        for right, num in enumerate(nums):
            cummulated_sum += num
            while cummulated_sum >= target:
                min_length = min(min_length, right - left + 1)
                cummulated_sum -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else 0
```

## references

### ref1: olsen-blue — 累積和 + 二分探索という別解の議論
https://github.com/olsen-blue/Arai60/pull/50

> (レビュー) `min_length` の初期値は `len(nums)` でもいい（最大でも配列全体の長さを超えることはないため、`inf`の代わりに使える）。
> (レビュー) 累積和配列を作れば単調増加になる（全部正の整数なので）。単調増加な配列なら二分探索で「targetを超える最小のindex」を探せるので、O(n log n)の別解が成立する。

Sliding Window（O(n)）の方が効率は良いが、「累積和が単調増加なら二分探索が使える」という発想は #300（LIS の bisect版）で使った考え方と同じ系統。

## 参考
- https://github.com/olsen-blue/Arai60/pull/50 (olsen-blue — 209. Minimum Size Subarray Sum)
- https://github.com/fuga-98/arai60/pull/48 (fuga-98 — 209. Minimum Size Subarray Sum)
- https://github.com/mamo3gr/arai60/pull/46 (mamo3gr — 209. Minimum Size Subarray Sum)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/43 (Yoshiki-Iwasa — 209. Minimum Size Subarray Sum)
- https://github.com/rimokem/arai60/pull/49 (rimokem — 209. Minimum Size Subarray Sum)
