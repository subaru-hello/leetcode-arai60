# 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-28, 10min, ok)

### 考えたこと
- 二分探索の再帰版。target と nums[mid] を比較して探索範囲を半分に絞る
- target < nums[mid] のとき helper(start, mid-1)（mid は除外、無限再帰を避けるため mid+1 ではなく mid-1）
- start > end になったら探索終了。target が存在しない場合、start が「挿入すべき位置」になる

### 実装
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start > end:
                return start
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return helper(start, mid - 1)
            else:
                return helper(mid + 1, end)

        return helper(0, len(nums) - 1)
```

## references

### ref1: olsen-blue — 再帰版から while ループへの書き換え議論
https://github.com/olsen-blue/Arai60/pull/41

```python
if left == right:
    return left
middle = (left + right) // 2
if nums[middle] >= target:
    return find_insert_index(left, middle)
else:
    return find_insert_index(middle + 1, right)
```

> (oda) 再帰を `while True` ループに変更し、`left, right = left, middle` + `continue` で置き換えられる。
> (olsen-blue, 自省) 「関数を使うという手段へのこだわりが強くなりすぎていた」。再帰関数はトップダウンDPと同様「欲しいものを叫べる」利点があるが、実装が重くなる欠点もある。

### ref2: rimokem — while ループ版（半開区間、left < right）
https://github.com/rimokem/arai60/pull/41

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    if nums[right] < target:
        return len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

`left == right` に収束するまでループする書き方（あなたの再帰版とは終了条件の考え方が異なる: `start > end` ではなく `left == right`）。

> (nodchip) コーナーケース処理（`nums[-1] < target` の早期リターン）は関数の先頭に置くべき。理由: 「短期記憶容量の無駄遣いになってしまう」（後で気にする必要がないよう先に片付ける）。
> (oda, Shunii85) 閉区間 vs 半開区間、二分探索の境界の取り方についての議論あり。

## 参考
- https://github.com/olsen-blue/Arai60/pull/41 (olsen-blue — 35. Search Insert Position)
- https://github.com/fuga-98/arai60/pull/41 (fuga-98 — 35. Search Insert Position)
- https://github.com/mamo3gr/arai60/pull/39 (mamo3gr — 35. Search Insert Position)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/34 (Yoshiki-Iwasa — 35. Search Insert Position)
- https://github.com/rimokem/arai60/pull/41 (rimokem — 35. Search Insert Position)
