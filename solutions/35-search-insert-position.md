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

## Step 2 (2026-07-29)

### 考えたこと
- 再帰版 → while ループ版に書き換え（refs で「再帰は実装が重くなる」との指摘があったため）
- コーナーケース（target が全要素より大きい）を関数の先頭で先に処理
- nums[mid] < target なら target は右側にある → left = mid + 1、そうでなければ target は mid 以下 → right = mid
- left < right で収束するまでループ（半開区間）

### 実装
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
```

## Step 3 (2026-08-07, レビュー反映)

### 考えたこと
- Step 1 の「無限再帰を避けるため mid+1 ではなく mid-1」は、動かして壊れたから直しただけで理由になっていなかった。区間の取り方を先に決めれば式は導ける
- 区間は「初期値・空判定・更新式」の3点セットで決まる。混ぜると壊れる（閉区間の空判定のまま `end = mid` にすると縮まず無限再帰）

  | | 初期値 | 空判定 | 右を捨てる |
  |---|---|---|---|
  | 閉区間 `[s, e]` | `(0, n-1)` | `s > e` | `e = mid - 1` |
  | 半開区間 `[s, e)` | `(0, n)` | `s == e` | `e = mid` |
  | 開区間 `(s, e)` | `(-1, n)` | `e - s == 1` | `e = mid` |

- 3つとも「調べ終わった mid を未確定から外す」という同じ操作。`end` が最後の要素そのものか1つ先かの違いで式が1つずれるだけ
- 挿入位置 = 「target 未満の要素の個数」。`start` がそのカウンタになる。`start` より左は target 未満、`end` より右は target より大、その間は未確定
- 等値の早期リターンは `<` / `==` / `>` の3分岐にしたから必要になっただけ。`nums[mid] < target` の2分岐にすれば要らず、重複があっても lower_bound になる
- Step 2 の `nums[-1] < target` 早期リターンは、`right` を `len(nums)` から始めれば不要。挿入位置が `len(nums)` になる場合を区間で表現できていなかったのが原因
- 半開区間 `[start, end)` と「末尾に番兵 ∞ を足した閉区間 `[0, len(nums)]`」は同じもの。要素 n 個に対して境界は n+1 本、番兵込みの要素も n+1 個で 1 対 1 に対応する。`start < end` なら必ず `mid < end` なので ∞ は参照されない

### 実装
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
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
