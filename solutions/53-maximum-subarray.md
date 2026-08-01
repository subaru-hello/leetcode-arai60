# 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-23, 10min, ok)

### 考えたこと
- 今回もDPを使ってとけそう。ひとつ前の値までの累積値を採用するか、現在の値から再スタートするか、みたいな感じだろうか。


### 実装
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        
        return best

```

## Step2
累積和を使ったアプローチもある。

```python
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    prefix_sum = 0
    max_sum = -math.inf
    min_sum = 0

    for num in nums:
      prefix_sum += num
      max_sum = max(max_sum, prefix_sum - min_sum)
      min_sum = min(min_sum, prefix_sum)
    return max_sum

```


## Step 2 (2026-07-23)

### 考えたこと
- 累積和 + 最小値管理（標高イメージ）
- `prefix_sum - min_sum` = 谷底からの上昇幅 = その位置で終わる最大 subarray の和
- 各位置で最大上昇幅を更新、最後に返す

### 実装
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_sum = -math.inf
        min_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        return max_sum
```

## references

### ref1: olsen-blue — 累積和の最小値管理（標高イメージ）とKadane/ナップザックDP の2解法
https://github.com/olsen-blue/Arai60/pull/32

```python
# Step1: 累積和の最小値管理（標高イメージ）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_sum = -math.inf
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return max_sum

# Step2: ナップザックDPのイメージ（Kadane）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        INITIAL_VALUE = -math.inf
        max_sum_at_index = [INITIAL_VALUE] * len(nums)
        max_sum_at_index[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum_at_index[i] = max(nums[i], max_sum_at_index[i-1] + nums[i])
        return max(max_sum_at_index)
```

> (oda) 「過去最安からの上げ幅」だけ変数にしておくと、マイナスになったときは最安値が更新されたという意味なので、`prefix_sum - min_prefix_sum` の一変数だけで話がつくんですね。
> (hroc135) `INITIAL_VALUE` と言われてもなんの VALUE かわからないので、単に `[-math.inf] * len(nums)` でいいと思いました。

### ref2: fuga-98 — DP配列で前値が負ならリセット、累積和でも書き直し
https://github.com/fuga-98/arai60/pull/32

```python
# Step1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total_with_i = [0] * len(nums)
        max_total_with_i[0] = nums[0]
        for i in range(1, len(nums)):
            if max_total_with_i[i - 1] < 0:
                max_total_with_i[i] = nums[i]
                continue
            max_total_with_i[i] = max_total_with_i[i - 1] + nums[i]
        return max(max_total_with_i)

# Step3: 累積和＋最小値管理
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_prefix_sum = -math.inf
        min_prefix_sum = 0
        for num in nums:
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return max_prefix_sum
```

> (olsen-blue) `i` はシンプルなループ変数として使うに留めたい。`max_total_with_i[i]` はあまり目に優しくない。`max_total_at[i]` などはどうか。

### ref3: mamo3gr — step1でKadane、step2で分割統治法（O(n log n)）
https://github.com/mamo3gr/arai60/pull/30

```python
# step1: Kadane's algorithm（O(n)）
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cumulative_sum = 0
        max_cumulative_sum = -math.inf
        min_cumulative_sum = math.inf
        for num in nums:
            cumulative_sum += num
            max_cumulative_sum = max(
                max_cumulative_sum,
                cumulative_sum,
                cumulative_sum - min_cumulative_sum,
            )
            min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)
        return max_cumulative_sum

# step2: 分割統治法（O(n log n)）
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def find_max_sum_in_range(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            left_max = find_max_sum_in_range(left, mid)
            right_max = find_max_sum_in_range(mid + 1, right)
            mid_max = find_max_sum_crossing_mid(left, right, mid)
            return max(left_max, right_max, mid_max)

        def find_max_sum_crossing_mid(left: int, right: int, mid: int) -> int:
            leftward_sum = 0
            left_max = nums[mid]
            for i in range(mid, left - 1, -1):
                leftward_sum += nums[i]
                left_max = max(left_max, leftward_sum)
            rightward_sum = 0
            right_max = nums[mid + 1]
            for i in range(mid + 1, right + 1):
                rightward_sum += nums[i]
                right_max = max(right_max, rightward_sum)
            return left_max + right_max

        return find_max_sum_in_range(0, len(nums) - 1)
```

> (naoto-iwase) 分割統治法の `find_max_sum_crossing_mid` は線形走査で、再帰の深さが O(log n) なので全体は O(n log n)。さらに O(n) に削ることも一応可能。
> (oda) 「どの解法が最適かは状況次第」。電車が止まったときタクシーや徒歩を選べるか、という話と同じ。

### ref4: Yoshiki-Iwasa — Rust で Kadane（current_max_sum と max_subarray_sum の2変数）
https://github.com/Yoshiki-Iwasa/Arai60/pull/48

```rust
// step3
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let Some(first) = nums.first() else {
            return 0;
        };
        let mut current_max_sum = *first;
        let mut max_subarray_sum = *first;

        (1..nums.len()).for_each(|i| {
            current_max_sum = std::cmp::max(current_max_sum + nums[i], nums[i]);
            max_subarray_sum = max_subarray_sum.max(current_max_sum);
        });

        max_subarray_sum
    }
}
```

> (fhiyo) `max_sum` という変数名はおかしい。i から j までの nums の合計なので `subarray_sum` が適切。

### ref5: rimokem — Kadane (step1) と分割統治法 (step2/3) を両方実装
https://github.com/rimokem/arai60/pull/32

```python
# step1: Kadane
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        best_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            best_sum = max(best_sum, current_sum)
        return best_sum

# step3: 分割統治法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)
            left_sum = float("-inf")
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            right_sum = float("-inf")
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            cross_max = left_sum + right_sum
            return max(left_max, right_max, cross_max)
        return helper(0, len(nums) - 1)
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/32 (olsen-blue — 53. Maximum Subarray)
- https://github.com/fuga-98/arai60/pull/32 (fuga-98 — 53. Maximum Subarray)
- https://github.com/mamo3gr/arai60/pull/30 (mamo3gr — 53. Maximum Subarray)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/48 (Yoshiki-Iwasa — 53. Maximum Subarray)
- https://github.com/rimokem/arai60/pull/32 (rimokem — 53. Maximum Subarray)
