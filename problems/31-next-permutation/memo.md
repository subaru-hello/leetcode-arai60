# 31. Next Permutation
https://leetcode.com/problems/next-permutation/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-24, 2min, ok)
### 考えたこと
- 完全に自力では出せず、`[1,2,3]`→`[1,3,2]`、`[1,3,2]`→`[2,1,3]`、`[3,2,1]`→`[1,2,3]`という具体例を1つずつ手を動かして比較しながら、「pivotを右端から探す→pivotより大きい最小値と交換→pivotより右を反転」というアルゴリズムを導いた。
- 参考: olsen-blue/Arai60のPRを1つ読んで、自分たちで導いた手順とほぼ同じ実装だったことを確認した。
- 「pivotより右側は常に降順」という不変条件が、交換相手探し・反転の両方の正しさを支えている、という点がポイント。
- `nums[pivot], nums[swap_point] = nums[swap_point], nums[pivot]`（一時変数なしのswap）はMove Zeroesと同じパターンとして復習になった。
- `pivot`という命名は「何の軸か伝わらない」という指摘があり、Step2で見直し予定(`ascend_index`/`break_index`案)。
- `find_pivot`が`len(nums)-2`から、`find_swap_point`が`len(nums)-1`から始まる理由(前者は`i`と`i+1`の2つを見るため、後者は`i`単体しか見ないため)も整理した。

## Step 2
### 整形して変えた点
- `pivot`の命名見直しを検討したが(`ascend_index`/`break_index`案)、結局`pivot`のまま確定させた。
- 参考PRにあった「2重ループ1つで書く別解」も検討したが、pivot探索と交換相手探索という別々の役割が1つの入れ子構造に混ざって読みにくくなる(かつ`>=`の否定条件も直感的でない)ため不採用。Step3で再現する際に「4段階の物語(pivot探索→-1チェック→交換相手探索→交換→反転)」がそのままコード構造に対応する3関数版を採用。
- 別解はmemoに記録のみ:
```python
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for pivot_index in range(len(nums) - 2, -1, -1):
            for swap_index in range(len(nums) - 1, pivot_index, -1):
                if nums[pivot_index] >= nums[swap_index]:
                    continue
                nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
                nums[pivot_index + 1:] = reversed(nums[pivot_index + 1:])
                return
        nums.reverse()
```

## Step 3（3回連続の記録）
- 1回目: 2026-08-25, 5min, ok
- 2回目: 2026-08-25, 5min, ok
- 3回目: 2026-08-25, 5min, ok

3回連続クリア、mastered。途中「pivotとswap_pointを交換する理由」「反転する理由」を思い出せなくなり、具体例`[1,3,2]`のトレースに立ち返って再確認した。

## 参考
- https://github.com/olsen-blue/Arai60/pull/59
- https://github.com/fuga-98/arai60/pull/55
- https://github.com/mamo3gr/arai60/pull/53
- https://github.com/t9a-dev/LeetCode_arai60/pull/58
- https://github.com/Manato110/LeetCode-arai60/pull/59
