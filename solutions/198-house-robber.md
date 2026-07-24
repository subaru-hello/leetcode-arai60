# 198. House Robber
https://leetcode.com/problems/house-robber/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-24, 10min, ok)

### 考えたこと
泥棒が現在見ている家でできることは２つ。盗むか、盗まないか。
一つ前で盗むか、２つ前で盗んで今の家で盗むか、どちらの方が多くの金額になるのかを計算していく。

### 実装
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
      max_up_to_prev = 0
      max_up_to_prev2 = 0

      for num in nums:
        current_max = max(max_up_to_prev, max_up_to_prev2 + num)
        max_up_to_prev2 = max_up_to_prev
        max_up_to_prev = current_max

      return max_up_to_prev

```

## Step2
変数名をtwo_before_maxとone_before_maxにした。数字が先の方が読みやすいと思った。意味的には、up_toを入れた方が正しいとは思う。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        two_before_max = 0
        one_before_max = 0

        for num in nums:
            current_max = max(one_before_max, two_before_max + num)
            two_before_max = one_before_max
            one_before_max = current_max
        
        return one_before_max

```



## Step 2 (2026-07-24)

### 考えたこと
- 変数名を `two_before_max`/`one_before_max` に変更して意味を明確化
- `current_max` の一時変数で同時更新の意図を読みやすく

### 実装
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        two_before_max = 0
        one_before_max = 0

        for num in nums:
            current_max = max(one_before_max, two_before_max + num)
            two_before_max = one_before_max
            one_before_max = current_max

        return one_before_max
```

## references

### ref1: olsen-blue — ボトムアップ DP（変数名が意味を表すパターン）
https://github.com/olsen-blue/Arai60/pull/35

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums, default=0)
        two_before_max = nums[0]
        one_before_max = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_amount = max(nums[i] + two_before_max, one_before_max)
            two_before_max = one_before_max
            one_before_max = max_amount
        return max_amount
```

> (Ryotaro25) 全体的に綺麗。
> (hroc135) 感情やイメージを積極的にアウトプットすると定着しやすい。

### ref2: olsen-blue — 初期値 0 スタートの省エネ版（あなたのコードに近い）
https://github.com/olsen-blue/Arai60/pull/35

olsen-blue は `len(nums) < 3` のエッジケースを明示的に処理しているが、`rob2, rob1 = 0, 0` スタートにすれば不要。

```python
# 初期値 0 スタートなら len チェック不要
rob2, rob1 = 0, 0
for num in nums:
    current_max = max(rob1, rob2 + num)
    rob2 = rob1
    rob1 = current_max
return rob1
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/35 (olsen-blue — 198. House Robber)
- https://github.com/fuga-98/arai60/pull/35 (fuga-98 — 198. House Robber)
- https://github.com/mamo3gr/arai60/pull/33 (mamo3gr — 198. House Robber)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/50 (Yoshiki-Iwasa — 198. House Robber)
- https://github.com/rimokem/arai60/pull/35 (rimokem — 198. House Robber)
