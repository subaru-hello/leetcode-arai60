# 105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-19, 10min, ok)

### 考えたこと
-

### 実装
下記はO(N**2)
```python
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
	return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)

    root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

    return root
    

```

下記はhashmapを使用して、
空間：O(N)
時間：O(1)

```python
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreNode]:
    inorder_map = {val: index for index, val in enumerate(inorder)}
    pre_index = 0
    def helper(left, right):
      if left > right:
	return None
      
      root_val = preorder[pre_index]
      pre_index += 1
      root = TreeNode(root_val)

      mid = inorder_map[root_val]
      root.left = helper(left, mid -1)
      root.right = helper(mid + 1, right)
      return root
    
    return helper(0, len(inorder) - 1 )


```



## Step 2 (2026-07-20)

O(N²) のスライス版から O(N) の hashmap + nonlocal 版に整形。
- `inorder.index()` O(N) → `inorder_map` で O(1) に
- スライスコピー → `pre_idx` カウンタで参照のみ
- `self.pre_idx` → `nonlocal` でクラス状態を汚さない形に

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left  = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)
```

## references

### ref1: LeetCode Editorial — Recursion with HashMap
Time O(N) Space O(N)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/editorial/

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)
```

### ref2: neetcode — Recursion (slice)
https://github.com/neetcode-gh/leetcode/blob/main/python/0105-construct-binary-tree-from-preorder-and-inorder-traversal.py

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
```

### ref3: Python標準ライブラリ活用 (enumerate)
https://docs.python.org/3/library/functions.html#enumerate

```python
# enumerate + dict comprehension で inorder の値→インデックス対応表を O(N) で構築
inorder_map = {val: idx for idx, val in enumerate(inorder)}
# list.index() による O(N) 探索を O(1) に置き換えられる
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/29 (olsen-blue — 105. Construct Binary Tree from Preorder and Inorder Traversal)
- https://github.com/fuga-98/arai60/pull/29 (fuga-98 — 105. Construct Binary Tree from Preorder and Inorder Traversal)
- https://github.com/mamo3gr/arai60/pull/28 (mamo3gr — 105. Construct Binary Tree from Preorder and Inorder Traversal)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/33 (Yoshiki-Iwasa — 105. Construct Binary Tree from Preorder and Inorder Traversal)
- https://github.com/rimokem/arai60/pull/29 (rimokem — 105. Construct Binary Tree from Preorder and Inorder Traversal)
