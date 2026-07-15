# 112. Path Sum
https://leetcode.com/problems/path-sum/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-15, 10min, ○)

### 1-A: 自力で考えたこと
- データ構造案: Tree
- アルゴリズム案: DFS, recursive
1本の根ノードから葉ノードまでの道の総和がターケット値と同じになるかを検証


### 1-B: 詰まった点
- 部分和か、総和かどうか、問題文を読んでも読み解けなかった

### 1-C: 自分が理解した解法
- 左右にノードが存在しない場合を葉ノードとして扱い、葉ノードにおいてこれまでの総和がtargetsumと同じ値ならtrueを返す


### 1-D: 実装
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_valid_path(node: Optional[TreeNode], total: int):
            if not node:
                return False
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    return True
            return is_valid_path(node.left, total) or is_valid_path(node.right, total)
        return is_valid_path(root, 0)
```

## Step 2 (2026-07-15, ?, ○)
stackで書く方法
https://github.com/fuga-98/arai60/pull/25/changes
```python

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        total = root.val
        stack = [(root, total)]
        while stack:
            node, total = stack.pop()
            if not node.left and not node.right:
                if total == targetSum:
                    return True
            if node.left is not None:
                stack.append((node.left, total + node.left.val))
            if node.right is not None:
                stack.append((node.right, total + node.right.val))
        return False

```

## references

### ref1: LeetCode Editorial — Recursive DFS
Time O(N) Space O(N)
https://leetcode.com/problems/path-sum/editorial/

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
```

### ref2: neetcode — Recursive
https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/0112-path-sum.py

```python
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

### ref3: iterative stack approach
Time O(N) Space O(N)

```python
# スタックを使ったイテレーティブ解法
def hasPathSum(root, targetSum):
    if not root:
        return False
    stack = [(root, targetSum - root.val)]
    while stack:
        node, curr = stack.pop()
        if not node.left and not node.right and curr == 0:
            return True
        if node.left:
            stack.append((node.left, curr - node.left.val))
        if node.right:
            stack.append((node.right, curr - node.right.val))
    return False
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/25
- https://github.com/fuga-98/arai60/pull/25
- https://github.com/mamo3gr/arai60/pull/24
- https://github.com/h-masder/Arai60/pull/28
- https://github.com/Yoshiki-Iwasa/Arai60/pull/29
