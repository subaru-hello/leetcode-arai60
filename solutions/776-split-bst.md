# 776. Split BST
https://leetcode.com/problems/split-bst/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-08-09, ng — 手厚いヒントで完成、次回は自力再挑戦)

### 考えたこと
- targetより小さいか、大きいかで、今見ているノードがどちらの木に属するか決まる
- BSTの性質上、root.val <= target なら root.left は全部target以下（確定）、root.rightだけ木1・木2が混在するので再帰的に仕分け直す
- root.val > target なら逆に root.right が確定、root.left を再帰的に仕分け直す
- 「分割した側と同じ側に、フィルタ済みの結果を繋ぎ直す」（右を分割したら右に戻す、左を分割したら左に戻す）
- 繋ぎ直す結果と、返り値のもう一方は必ず別のインデックス（[0]と[1]が分かれる）になる。同じ要素を2箇所で使うと木が壊れる
- premium問題でACできず、再帰の「潜って戻る」感覚も掴みきれなかったため、正直に ng 扱いとして記録。次回自力で再挑戦する

### 実装（手厚いヒントで到達した形、次回は見ずに書く）
```python
class Solution:
    def splitBST(self, root, target):
        if root is None:
            return [None, None]

        if root.val <= target:
            split_trees = self.splitBST(root.right, target)
            root.right = split_trees[0]
            return [root, split_trees[1]]
        else:
            split_trees = self.splitBST(root.left, target)
            root.left = split_trees[1]
            return [split_trees[0], root]
```

## Step 2 (2026-08-09)

### 考えたこと
- mamo3gr の実装が本質的に同じ構造だった（変数名を `child_left`/`child_right` にして、木1/木2どちらに属するかを名前で明示）
- `split_trees[0]`/`split_trees[1]` という配列アクセスより、タプルアンパックで変数名をつけた方が「今どちらの木を扱っているか」が読みやすい
- olsen-blue のレビューで「root という名前が動いてしまうので分かりづらい」との指摘があった。ヘルパー関数の引数名を `node` にすることで、外側の `root`（元の呼び出し）と再帰内部を区別

### 実装
```python
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def helper(node):
            if node is None:
                return None, None
            if node.val <= target:
                child_le, child_gt = helper(node.right)
                node.right = child_le
                return node, child_gt
            else:
                child_le, child_gt = helper(node.left)
                node.left = child_gt
                return child_le, node
        return list(helper(root))
```

## references

### ref1: mamo3gr — タプルアンパックで変数名を明示
https://github.com/mamo3gr/arai60/pull/58

```python
def splitBST(root: TreeNode, val: int) -> tuple[TreeNode | None, TreeNode | None]:
    def helper(node: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
        if node is None:
            return None, None
        if node.val <= val:
            child_left, child_right = helper(node.right)
            node.right = child_left
            return node, child_right
        else:
            child_left, child_right = helper(node.left)
            node.left = child_right
            return child_left, node
    return helper(root)
```

> (nodchip) 改行が崩れていて読みづらいという指摘があった（内容自体への指摘ではなくフォーマットの問題）。

### ref2: olsen-blue — 非再帰（イテレーティブ）な別解と、変数名議論
https://github.com/olsen-blue/Arai60/pull/48

`.right` を伸ばしながら木を繋いでいくイテレーティブ版も存在する（`smaller_node.right = root` のように、ポインタを付け替えながら進む）。

> (oda) 「root という名前が動いてしまう」ため、より説明的な変数名が必要。「.right が伸びていくイメージは説明が必要」で、図がないと理解しづらい解法だという指摘。
> (著者) 実装時に「頭がこんがらがってしまい、図が必要だった」と述懐。再帰版の方が図なしでも追いやすい。

## 参考
- https://github.com/olsen-blue/Arai60/pull/48 (olsen-blue — 776. Split BST)
- https://github.com/mamo3gr/arai60/pull/58 (mamo3gr — 776. Split BST)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/41 (Yoshiki-Iwasa — 776. Split BST)
- https://github.com/rimokem/arai60/pull/47 (rimokem — 776. Split BST)
