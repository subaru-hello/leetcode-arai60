# 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-29, 5min, ok)

### 考えたこと
- #35 の while ループの型を応用
- nums[mid] と nums[right] を比較。nums[right] > nums[mid] なら最小値は mid かそれより左 → right = mid、そうでなければ最小値は mid より右 → left = mid + 1

### 実装
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

## references

### ref1: olsen-blue — 境界探索パターンの一般化と重複要素の注意点
https://github.com/olsen-blue/Arai60/pull/42

> (oda) 境界探索型の二分探索パターンとして `right=len(nums)`、`<=` 比較、`middle` への割り当てを推奨。left/right の意味定義（何を含み、何を含まないか）を明確にすることが重要。
> (Ryotaro25) 重複要素を含む配列（例: `[1,1,1,0,1]`）ではこのアルゴリズムは機能しない。今回の問題は「重複なし」が前提だが、重複ありの発展問題（#154）では別の工夫が必要。
> (saagchicken) `sorted()` や `min()` でも技術的には正解になるが、O(log n) の意図を汲むなら二分探索が本筋。

## 参考
- https://github.com/olsen-blue/Arai60/pull/42 (olsen-blue — 153. Find Minimum in Rotated Sorted Array)
- https://github.com/fuga-98/arai60/pull/42 (fuga-98 — 153. Find Minimum in Rotated Sorted Array)
- https://github.com/mamo3gr/arai60/pull/40 (mamo3gr — 153. Find Minimum in Rotated Sorted Array)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/35 (Yoshiki-Iwasa — 153. Find Minimum in Rotated Sorted Array)
- https://github.com/rimokem/arai60/pull/42 (rimokem — 153. Find Minimum in Rotated Sorted Array)
