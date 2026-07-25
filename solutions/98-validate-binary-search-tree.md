# 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-18, 10min, ok)

### 自分が理解した解法
- 最大２つの子ノード（left, right)を持ち、左ノードは親ノードより小さく、右ノードは親ノードより大きくなるようなツリー構造にしていく。
その条件に合わない場合をFalseにする。

### 実装
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min, max):
            if not node:
                return True
            
            if not (min < node.val < max):
                return False
            
            return validate(node.left, min, node.val) and validate(node.right, node.val, max)
        return validate(root, float('-inf'), float('inf'))

```

## Step 2 (2026-07-19)

他者コードを読んだ上での整形版。2点修正:
- `min`/`max` は Python 組み込みを隠すので `low`/`high` に変更
- デフォルト引数で初期境界値を持たせ、呼び出し側をすっきりさせる

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)
```

## references

引数側で初期値に下限と上限を持たせるパターン。
呼び出しがわで
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)
```



https://docs.python.org/3/library/functions.html#float
```python
# float('-inf') と float('inf') は Python 組み込みの float() で生成できる
# IEEE 754 の負の無限大・正の無限大を表し、すべての整数値より小さい/大きいことが保証される
# BST バリデーションの境界値として初期値に使うことで、
# ルートノードに対して「どんな値でも範囲内」という状態を表現できる

low = float('-inf')   # すべての整数 n に対して low < n が成立
high = float('inf')   # すべての整数 n に対して n < high が成立
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/28 (olsen-blue — 98. Validate Binary Search Tree)
- https://github.com/fuga-98/arai60/pull/28 (fuga-98 — 98. Validate Binary Search Tree)
- https://github.com/mamo3gr/arai60/pull/26 (mamo3gr — 98. Validate Binary Search Tree)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/32 (Yoshiki-Iwasa — 98. Validate Binary Search Tree)
- https://github.com/rimokem/arai60/pull/28 (rimokem — 98. Validate Binary Search Tree)
