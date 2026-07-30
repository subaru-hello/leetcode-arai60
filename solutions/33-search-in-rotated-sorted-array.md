# 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-30, 5min, ok)

### 考えたこと
- 単純に target と nums[mid] を比較するだけでは、回転配列は全体が単調ではないので判断できない（反例: nums=[4,5,6,7,0,1,2], target=0 で誤った方向に絞り込んでしまう）
- まず nums[left] <= nums[mid] で「どちらの半分が確実にソート済みか」を判定
- ソート済みの半分については target が範囲内かを確実にチェックできる（nums[left] <= target < nums[mid]）。範囲外なら消去法でもう片方に絞る
- while left <= right の閉区間版。nums[mid] == target で早期リターン、ループを抜けたら -1

### 実装
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

## Step 2 (2026-07-30)

### 考えたこと
- while ループ版 → 再帰版（inner function）に書き換え
- start > end を base case（探索範囲が尽きた = 見つからない）
- ロジックは Step 1 と同じ。start/end を更新してから helper(start, end) を再帰呼び出しする形（#153 と同じパターン）

### 実装
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            return helper(start, end)
        return helper(0, len(nums) - 1)
```

## references

### ref1: olsen-blue — 再帰版・inner function の是非をめぐる議論
https://github.com/olsen-blue/Arai60/pull/43

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_target_index(left: int, right: int) -> int:
            if not (left <= right):
                # 見つからない場合
                ...
```

> (saagchicken) 「終了条件を明示できないのが気になる」。if のネストを関数にまとめると二分探索部分が読みやすくなる。
> (TORUS0818) while ループで書けるなら inner function にしなくても良いのでは、という指摘（あなたの while 版はまさにこちらのアプローチ）。
> (hroc135) `if not (left <= right)` は Python では `if not left <= right` の方が自然（Pythonic）。
> (oda) `&`/`|`（ビット演算）と `and`/`or`（論理演算）の使い分けに注意。

## 参考
- https://github.com/olsen-blue/Arai60/pull/43 (olsen-blue — 33. Search in Rotated Sorted Array)
- https://github.com/fuga-98/arai60/pull/43 (fuga-98 — 33. Search in Rotated Sorted Array)
- https://github.com/mamo3gr/arai60/pull/41 (mamo3gr — 33. Search in Rotated Sorted Array)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/36 (Yoshiki-Iwasa — 33. Search in Rotated Sorted Array)
- https://github.com/rimokem/arai60/pull/43 (rimokem — 33. Search in Rotated Sorted Array)
