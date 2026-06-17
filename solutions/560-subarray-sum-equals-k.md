# 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-17, 60min, △)

### 1-A: 自力で考えたこと
- データ構造案: 
- アルゴリズム案: two sumの考え方でいけるのではないかと思った

### 1-B: 詰まった点
- 連続する値をどうdictに保持するか
- わからなくて写経をしたが、３回写経してよくわからなかったから立ち止まった。
- 部分配列の和は累積和の差で表せる理由が直感的によくわからなかった。こういうときってみんなどうするのだろう

### 1-C: 自分が理解した解法
- prefix sumが使えるらしい。現在見ているメモリに、一つ前の値と現在見ている値を足した結果を格納していく。足した結果がkになったら、どうする？そこがわからなかった。
- 累積和は、それまでに出てきた数字を足し合わせた結果のことかな。なんでprefix_count[prefix_sum - k]が存在すると累積和がkになるsubarrayがあることがわかるのだろうか

式：
nums[i..j] の和 = prefix_sum[j+1] - prefix_sum[i]

```
nums = [1, 2, 3]
prefix_sum: 0, 1, 3, 6

nums[1..2] = [2, 3] の和 = prefix_sum[3] - prefix_sum[1] = 6 - 1 = 5
```

なんとなくわかってきたぞ？

```
0番目から3番目までの合計 = 10
0番目から0番目までの合計 = 2
1番目から3番目までの合計 = 10 - 2 = 8
```



### 1-D: 実装
```python
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            result += prefix_count[prefix_sum - k] 
            prefix_count[prefix_sum] += 1
        return result
```

### Step2
やっぱりprefix_countの直感が沸かないから、写経は続く

```python
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int, {0: 1})
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            complement = prefix_count[prefix_sum - k]
            result += complement
            prefix_count[prefix_sum] += 1
        return result
```
> > [-2,1,-3,4,-1,2,1,-5,4]を例に取れば、100回ちょっとも足し算すれば、全通り出せるわけで、とりあえずそれをやってから考えたらどうでしょう。

## 参考
- https://github.com/mamo3gr/arai60/pull/17
- https://github.com/olsen-blue/Arai60/pull/16
- https://github.com/chanseok-lim/arai60/pull/9
- https://github.com/Yoshiki-Iwasa/Arai60/pull/15
- https://github.com/h-masder/Arai60/pull/17
