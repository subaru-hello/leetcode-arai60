# 349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-09, 179min, △)

### 1-A: 自力で考えたこと
- データ構造案:
- アルゴリズム案:

nums1の各数字をn1_dictに保持
nums2を走査して、n1_dictと突合
n1_dictに存在していた場合、setに入れる
setを返す

### 1-B: 詰まった点
- なかった。初めてかも

### 1-C: 自分が理解した解法
- うまく抽象化できないな。
- 2つのlistを比較して、共通する値をlistで返却する問題。

### 1-D: 実装
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_dict = {}
        for num in nums1:
            n1_dict[num] = 1

        result = set()

        for num in nums2:
            if num in n1_dict:
                result.add(num)
        return list(result)
```

## Step2
他の方のPRを見ると、積集合を使って解いている方がいた。実装がシンプルになっていい。
```python

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       return list(set(nums1) & set(nums2))
```

> 片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか、特に大きいほうが sort 済みのときにはどうしますか。
> https://github.com/katataku/leetcode/pull/12/changes#r1893968021

- 二分探索を使った書き方もあるらしい。２つに分ける位置で分割して、targetの値よりもleft, rightが大きい・小さいかを判定して、探索対象を狭めていっている。

> https://github.com/olsen-blue/Arai60/pull/13/changes#r1912060328

- 二分探索を日報を使って解説している。二分探索は、範囲を絞っていって期待する値を見つけるアルゴリズムだと解釈した。
- 「範囲」の「中にある」「値」を探索していく。範囲といっても、横並びになっているメモリの間だから、左側と右側つまり開始端と終了端がある。
> https://discord.com/channels/1084280443945353267/1192736784354918470/1199018938005213234

この問題、二分探索の理解にもってこいの問題なのかもしれない。[こんな深く分析できていなかった](https://github.com/olsen-blue/Arai60/blob/41171886bb6299943cdcdf8e92e08bdc2833580f/349.%20Intersection%20of%20Two%20Arrays.md#step5%E5%89%8D%E6%97%A5%E3%81%BE%E3%81%A7%E3%81%AE%E4%BF%9D%E8%A8%BC%E5%86%85%E5%AE%B9%E6%9C%AC%E6%97%A5%E3%81%AE%E8%AA%BF%E6%9F%BB%E5%86%85%E5%AE%B9%E7%B5%82%E4%BA%86%E6%9D%A1%E4%BB%B6middle%E3%81%AE%E5%88%B6%E7%B4%84%E5%88%9D%E6%9C%9F%E5%80%A4%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E6%96%87%E5%AD%97%E3%81%AB%E8%B5%B7%E3%81%93%E3%81%99)


```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        search_space = sorted(nums1)
        result = set()
        
        for n in nums2:
            i = self.binary_search_left(search_space, n)
            if i < len(search_space) and search_space[i] == n:
                result.add(n)
        
        return list(result)

    def binary_search_left(self, nums, target) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        
        return left

```


## 参考
- https://github.com/mamo3gr/arai60/pull/13
- https://github.com/olsen-blue/Arai60/pull/13
- https://github.com/chanseok-lim/arai60/pull/5
- https://github.com/Yoshiki-Iwasa/Arai60/pull/12
- https://github.com/h-masder/Arai60/pull/14
