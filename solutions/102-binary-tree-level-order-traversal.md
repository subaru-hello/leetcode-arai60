# 102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-15, 15 min, △)

### 1-A: 自力で考えたこと
- データ構造案: queue
- アルゴリズム案: BFS

### 1-B: 詰まった点
- 階層毎に値を配列で保持する必要があることはなんとなくわかった。ただ、実装する方法がわからなかった

### 1-C: 自分が理解した解法
- 同じ階層であることを、roopの中で左と右ノードを辿るという行為で表現できることがわかった。
- 階層毎のブロックを、２層で作成している。１層目、queue roopの外側に定義。２層目、queue roopの内側のさらにfor roopの中で定義することで、同階層を表現する

### 1-D: 実装
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        values_by_level = []

        while queue:
            frontier = len(queue)
            level = []
            for _ in range(frontier):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values_by_level.append(level)
        return values_by_level

```

## Step 2 (2026-07-16, 10 min, ○)

### 2-A: 他の解法から学んだこと
- ref2 の `(node, level)` タプルをキューに持たせるアプローチを採用
- ノードが自分のレベルを持ち歩くため、処理中に「今どの階層にいるか」が明示的になる
- `if level >= len(values): values.append([])` で結果配列を動的に伸ばす

### 2-B: 実装

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([(root, 0)])
        values = []
        while queue:
            node, level = queue.popleft()
            if level >= len(values):
                values.append([])
            values[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return values
```

## references

### DFS再帰（level を引数で渡す）
https://github.com/mamo3gr/arai60/pull/25

```python
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        values = []

        def traverse(node: TreeNode, level: int) -> None:
            if level >= len(values):
                values.append([])
            values[level].append(node.val)

            if node.left is not None:
                traverse(node.left, level + 1)
            if node.right is not None:
                traverse(node.right, level + 1)

        traverse(root, 0)
        return values
```

> (naoto-iwase) `if level >= len(values)` より `while level >= len(values)` の方が、「配列長が足りなければ足りるまで伸ばす」というシンプルで独立したロジックとして完結していて読み手に優しい。
> (mamo3gr) 同意。levelごとでループが回る方式なら append 条件判定自体が不要で、さらに読み手に優しい。

### BFS（キューに (node, level) を持たせる）
https://github.com/mamo3gr/arai60/pull/25

```python
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_and_level = collections.deque([(root, 0)])
        values = []
        while node_and_level:
            node, level = node_and_level.popleft()
            if level >= len(values):
                values.append([])
            values[level].append(node.val)

            if node.left is not None:
                node_and_level.append((node.left, level + 1))
            if node.right is not None:
                node_and_level.append((node.right, level + 1))

        return values
```

### BFS（while True + next_nodes リストスワップ）
https://github.com/fuga-98/arai60/pull/26

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = [root]
        level_order = []
        while True:
            next_nodes = []
            level_values = []
            for node in nodes:
                level_values.append(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            level_order.append(level_values)
            if not next_nodes:
                return level_order
            nodes = next_nodes
```

> (oda) `while True` より `while stack:` にして `return result` をループ外に出す方が好み（終了条件が目に入りやすい）。
> (olsen-blue) `while True` は終わる箇所が分かりにくいので好まない。

自分も同意見。whileの中を見て、終了条件を探す必要があるのが手間。
> (nodchip) キューとして使っていないのに `stack` という変数名は混乱を招く。`nodes` が適切。

## 参考
- https://github.com/olsen-blue/Arai60/pull/27
- https://github.com/fuga-98/arai60/pull/26
- https://github.com/mamo3gr/arai60/pull/27
- https://github.com/h-masder/Arai60/pull/30
- https://github.com/Yoshiki-Iwasa/Arai60/pull/31
