# 108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-13, 40min, △)

### 1-A: 自力で考えたこと
- データ構造案: Binary Tree
- アルゴリズム案: 今回もBFSで解けそうかもしれない

### 1-B: 詰まった点
ちょっと問題の軸がずれた途端にわからなくなる。

### 1-C: 自分が理解した解法
- 入力は「ソート済み配列」（treeではなくarray）。これを BST に変換する。
- BST のルール: 左ノード < 親ノード < 右ノード。ソート済み配列はすでにこの順序を満たしている。
- **height-balanced にするための鍵**: 配列の**中央値を root** にすれば、左右の要素数の差が最大1になり、自動的にバランスが取れる。
- あとは左半分・右半分に対して同じ操作を再帰的に繰り返すだけ。
- base case: 配列が空になったら None を返す。


### 1-D: 実装
```python
class Solution:
	def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
		if nums is None:
			return None
		mid = len(nums) // 2
		root = TreeNode(nums[mid])
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid + 1:])
		return root
```

## Step 2 (2026-07-14, 10min, ○)
binery searchのセクションと準備のセクションは分けた方が関数の責務を分離できて保守性が上がりそうと思った

```python
class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> TreeNode | None:
                def sort_to_bst(start, end):
                        if start > end:
                                return None
                        mid = (start + end) // 2
                        root = TreeNode(nums[mid])
                        root.left = sort_to_bst(start, mid - 1)
                        root.right = sort_to_bst(mid + 1, end)
                        return root
                return sort_to_bst(0, len(nums) - 1)
```

> スライスを作るとコピーが発生し、処理が重くなるため、 phase2 のようにインデックスで処理したほうがよいと思います。
https://github.com/SuperHotDogCat/coding-interview/pull/40/changes#r1770559848

> 一応、具体的な数字にしておくことをおすすめします。
Python の再帰の深さは限界いくらくらいで、n は今回いくつと考えているので、log n がいくつくらいになるのか、まで。
最後は、常に具体的な数字が問題になるので。(普段、わざわざ書くかどうかはともかく、練習ならば書いてもいいでしょう。)
https://github.com/SuperHotDogCat/coding-interview/pull/40/changes#r1782715427

> https://github.com/TORUS0818/leetcode/pull/26#discussion_r1693044574

## 参考
- https://github.com/olsen-blue/Arai60/pull/24
- https://github.com/fuga-98/arai60/pull/24
- https://github.com/mamo3gr/arai60/pull/23
- https://github.com/ichika0615/arai60/pull/17
- https://github.com/h-masder/Arai60/pull/27
