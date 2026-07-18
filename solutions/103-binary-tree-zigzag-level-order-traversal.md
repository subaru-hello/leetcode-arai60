# 103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-16, 10min, ok)

### 1-A: 自力で考えたこと
- データ構造案: queue
- アルゴリズム案: DFS

### 1-B: 詰まった点
- セマフォのようなものを用意して、左右を表現するとことまでは思いついた。

### 1-C: 自分が理解した解法
- 階層毎にノードを走査していく。前回の問題との違いは、左起点で掘り下げるか否かという変数を用いてzigzagに走査する点

### 1-D: 実装
```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        left_to_right = True
        group_by_level = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            group_by_level.append(level)
            left_to_right = not left_to_right
        return group_by_level

```

## Step 2 (2026-07-18)

他者コードを読んだ上での整形版。変数名を `group_by_level` → `result` に統一し、簡潔にした。
neetcode の `level[::zigzagDirection]` (スライスステップ) は面白いが、`q.pop(0)` が O(n) なのでそこは deque のまま維持。

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        left_to_right = True
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result
```

## references

### ref1: LeetCode Editorial — BFS with direction flag
Time O(N) Space O(N)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/editorial/

※ LeetCode Editorial はログインが必要なページのため、コードの直接取得不可。概要: BFS でレベルごとにノードを収集し、レベルの奇偶で `deque.appendleft` か `deque.append` を切り替えてジグザグを実現するアプローチ。

### ref2: neetcode — BFS with slice step
https://github.com/neetcode-gh/leetcode/blob/main/python/0103-binary-tree-zigzag-level-order-traversal.py

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        result, zigzagDirection = [], 1
        q = [root]
        while q:
            level, queueLength = [], len(q)
            for i in range(queueLength):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level[::zigzagDirection])
            zigzagDirection *= -1
        return result
```

### ref3: Python標準ライブラリ活用 (collections.deque)
https://docs.python.org/3/library/collections.html#collections.deque

```python
# deque の appendleft を使い、逆順コピーを作らずにジグザグを実現する例
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        left_to_right = True
        result = []
        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(level))
            left_to_right = not left_to_right
        return result
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/27 (olsen-blue — 103. Binary Tree Zigzag Level Order Traversal)
- https://github.com/fuga-98/arai60/pull/27 (fuga-98 — 103. Binary Tree Zigzag Level Order Traversal)
- https://github.com/mamo3gr/arai60/pull/27 (mamo3gr — 103. Binary Tree Zigzag Level Order Traversal)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/31 (Yoshiki-Iwasa — 103. Binary Tree Zigzag Level Order Traversal)
- https://github.com/rimokem/arai60/pull/27 (rimokem — 103. Binary Tree Zigzag Level Order Traversal)
