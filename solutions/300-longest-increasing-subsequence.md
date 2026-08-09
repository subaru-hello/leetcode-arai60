# 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-22, 10min, ok)

### 考えたこと
下記2点を判断して、非連続で昇順に並ぶ数字を作ることができる最大長を見つける問題だと捉えた
- 現在見ている値が今まで見てきた値より大きいのか
- 大きければ、最大長を伸ばして記録する

### 実装
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

```

## Step2
Step1の実装は、最悪時間がn**nになっていたから、問題文の推奨であるn log nのパターンを実装してみた。

```
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            position = bisect.bisect_left(tails, num)
            if position >= len(tails):
                tails.append(num)
            else:
                tails[position] = num
        return len(tails)
```

## references

### ref1: olsen-blue — DP + 変数名 `length_at_index` / `max_lengths`、bisect解法も実装
https://github.com/olsen-blue/Arai60/pull/31

```python
# Step2 での整形後（変数名を max_lengths に改善）
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)
        return max(max_lengths)
```

```python
# bisect 解法（Step2）
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []  # Longest Increasing Subsequence
        for num in nums:
            insert_index = bisect_left(lis, num)
            if insert_index <= len(lis) - 1:  # 差し替えの場合
                lis[insert_index] = num
            else:                              # 末尾追加の場合
                lis.append(num)
        return len(lis)
```

> (レビュー: oda) これ自体は `lis` ではなくて、長さがインデックスの increasing sequence を作る場合の末尾の最小値ですよね。変数名で表現しきれない気がするのでコメントで対処ですかねえ。
>
> (olsen-blue) `# lis[i] : 長さがi+1の増加部分列における末尾の数字の最小値` とコメントで補足する方向で。

### ref2: fuga-98 — Step1 WA から DP・bisect へ、bisectのコメントが秀逸
https://github.com/fuga-98/arai60/pull/31

```python
# Step2 DP（olsen-blue PR を参考に整理）
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        max_lengths = [1] * len_nums
        for i in range(len_nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)
        return max(max_lengths)
```

```python
# Step2 bisect 解法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []  # 長さがインデックスの increasing sequence を作る場合の末尾の最小値
        for num in nums:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)
```

> bisect 解法の直感的な理解（olsen-blue のコメントより引用）:
> 数字を差し替えても長さ変わらないし、筋の良さげなルートをキープしておいて、未来においてより長いLISが作れる可能性を最大化する。
> 例: `[1, 98, 99, 100, 2, 4]` の後に `[5, 6]` が続いた場合、`2→4→5→6` のルートが活きる。

### ref3: mamo3gr — 後ろから走査する DP + `tails_by_lis_length` のインデックス設計
https://github.com/mamo3gr/arai60/pull/29

```python
# step1: 後ろから走査する DP（dict で管理）
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        sequence_length = {n - 1: 1}
        max_length = sequence_length[n - 1]

        for i in reversed(range(0, n - 1)):
            sequence_length_i = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    sequence_length_i = max(sequence_length_i, sequence_length[j] + 1)
            sequence_length[i] = sequence_length_i
            max_length = max(max_length, sequence_length_i)

        return max_length
```

```python
# step3: bisect 解法（番兵 -inf でインデックスを長さに揃える）
import bisect
import math

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # minimum tail number of increasing sequence whose length is i
        sentinel = -math.inf
        min_tail_by_length = [sentinel]

        for num in nums:
            index = bisect.bisect_left(min_tail_by_length, num)
            if index >= len(min_tail_by_length):
                min_tail_by_length.append(num)
            else:
                min_tail_by_length[index] = min(min_tail_by_length[index], num)

        return len(min_tail_by_length) - 1
```

> 番兵 `-math.inf` を先頭に置くことで `tails_by_lis_length[i]` が長さ `i` の IS 末尾の最小値に対応し、インデックスと長さが一致する設計。

### ref4: Yoshiki-Iwasa — Rust 実装、`partition_point` で bisect 相当を実現
https://github.com/Yoshiki-Iwasa/Arai60/pull/46

```rust
// step2: partition_point (lower_bound 相当) を使った O(N log N)
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut lis = vec![];

        nums.into_iter().for_each(|n| {
            let insert_pos = lis.partition_point(|num_in_lis| *num_in_lis < n);
            match insert_pos >= lis.len() {
                true => lis.push(n),
                false => lis[insert_pos] = n,
            }
        });
        lis.len() as i32
    }
}
```

> (レビュー: sasanquaneuf) `lis` はlongest increasing subsequenceとは必ずしも一致しない。例えば `nums = [10, 11, 12, 1, 2]` を与えると `lis` は `[1, 2, 12]` になるが `[1, 2, 12]` という部分列は実際には取れない。`lis[n]` の意味は「長さ n+1 の IS の末尾として取りうる最小値」。
>
> (oda) `end_minimums_of_is` などが候補。命名が難しい変数の典型例。

### ref5: rimokem — `subsequence_lengths` / `tails` の命名、step1 と step2 の対比が明快
https://github.com/rimokem/arai60/pull/31

```python
# step1: DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        subsequence_lengths = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    subsequence_lengths[i] = max(
                        subsequence_lengths[i], subsequence_lengths[j] + 1
                    )

        return max(subsequence_lengths)
```

```python
# step2: bisect 解法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)
```

> step1 では「i番目の要素を末尾とする最大部分列の長さ」を末尾でインデックスし、step2 では「長さ k+1 の部分列を作れるときの末尾要素の最小値」を長さでインデックスする。前者を選ぶと配列が単調増加になるため二分探索が適用できる、という対比が明快。

## 参考
- https://github.com/olsen-blue/Arai60/pull/31 (olsen-blue — 300. Longest Increasing Subsequence)
- https://github.com/fuga-98/arai60/pull/31 (fuga-98 — 300. Longest Increasing Subsequence)
- https://github.com/mamo3gr/arai60/pull/29 (mamo3gr — 300. Longest Increasing Subsequence)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/46 (Yoshiki-Iwasa — 300. Longest Increasing Subsequence)
- https://github.com/rimokem/arai60/pull/31 (rimokem — 300. Longest Increasing Subsequence)
