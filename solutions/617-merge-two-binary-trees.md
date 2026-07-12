# 617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-12, ?? min, ??)

### 1-A: 自力で考えたこと
- データ構造案: Binary Tree
- アルゴリズム案: BFS

### 1-B: 詰まった点
- node1とnode2のvalを足し合わせた後、TreeNodeをどう繋ぎ合わせればいいのかわからなかった

### 1-C: 自分が理解した解法
- 片方のrootに統合していく解法。確保するスタックメモリを増やさないで済むが、元のrootの値を破壊してしまう。
- 再起的に、左、右のnodeを足し合わせて次に進んでいく

### 1-D: 実装
```python
class Solution:
	def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
		if root1 is None:
			return root2
		if root2 is None:
			return root1

		root1.val += root2.val
		root1.right = self.mergeTrees(root1.right, root2.right)
		root1.left = self.mergeTrees(root1.left, root2.left)
		return root1
```

## Step2
他の人の実装は、非破壊的な実装が多かった。
こっちの方がシンプルで好き

```python
class Solution:
        def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
                if root1 is None:
                    return root2
                if root2 is None:
                    return root1
                
                return TreeNode(
                    root1.val + root2.val,
                    self.mergeTrees(root1.left, root2.left),
                    self.mergeTrees(root1.right, root2.right)
                )
```

## 参考
- https://qiita.com/ryo2132/items/4bedeec846d0427f1ac7
- https://github.com/olsen-blue/Arai60/pull/23 (olsen-blue — 617. Merge Two Binary Trees)
- https://github.com/fuga-98/arai60/pull/23 (fuga-98 — 617. Merge Two Binary Trees)
- https://github.com/mamo3gr/arai60/pull/22 (mamo3gr — 617. Merge Two Binary Trees)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/66 (Yoshiki-Iwasa — 617. Merge Two Binary Trees)
- https://github.com/rimokem/arai60/pull/23 (rimokem — 617. Merge Two Binary Trees)
