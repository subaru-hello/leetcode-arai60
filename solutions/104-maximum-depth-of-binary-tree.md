# 104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-10, 解説つき・長め, ok)

### 1-A: 自力で考えたこと
- データ構造案: stack
- アルゴリズム案: DFS

### 1-B: 詰まった点
- 深さを更新していく方法を思い付かず断念

### 1-C: 自分が理解した解法
- 積む側、降ろす側がある
- rightかleftがある場合、こノードがあるということなので、depthを１増やして次のnodeをstackに積む
- stackが空になるまで降ろして最大深度を更新し続ける

### 1-D: 実装
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
```

## Step2

再起で解く方法が一般的みたい。今回のnodeの数上限を見たら、スタックオーバーフローを起こす可能性がないからか？
ただ、解答例の中では遅いほうだな。4msだった
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
```

BFSバージョンもある
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        max_depth = 0
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth
```

**概念: top-down か bottom-up か**
- Step1 の「depth を引数で上から配る」書き方は **top-down**（根から葉へ深さを配り、葉で return）。
- 再帰版 `max(左, 右) + 1` は **bottom-up**（葉から深さを畳み上げる）。引数の受け渡しが消えてスッキリ見えるのはこのため。「洗練されて見える」の正体は書式ではなく、この計算方向の違い。
- この語彙（top-down / bottom-up）は木DP系で効いてくる。
- 出典: nicah4o/arai60#20 (liquo-rice スレッド)

**反復DFSで `max()` が必要な理由（ただの代入ではダメ）**
- pop 順のせいで「深い葉を先に、浅い葉を後に」取り出すことがある。後の浅い深さで上書きすると壊れる。
- 反例: `[3,1,5,null,null,null,7]` → 深い枝(5→7)を先、浅い葉(1)を後に pop するケースで、代入だと浅い側の深さで上書きされてしまう。だから `max_depth = max(max_depth, depth)`。
- 出典: goto-untrapped/Arai60#45 (Ryotaro25 スレッド)

**スタイル（レビューで繰り返し出た指摘）**
- `if node.left:` より **`if node.left is not None:`** を明示。「ノードの存在チェック」か「値の真偽」かを読み手に迷わせない。(komdoroid#17)
- 再帰は **ヘルパー関数も不要・条件分岐も1つで済む**。`return max(maxDepth(left), maxDepth(right)) + 1`。(nicah4o#20)
- `1 + max(...)` より **`max(...) + 1`** が多数派（複雑な項を先に、+1 を後に）。趣味の範囲だが読み手に優しい。(jjysogfy#10 nodchip)
- スタックに `(node, depth)` を積むなら、要素名は中身を表す（`nodeAndDepth`）と誤読が減る。分解して `node, depth = stack.pop()` するなら可読。(goto-untrapped#45)


## Step 3 (2026-07-10, ~10min, ok) — レビュー反映（is not None）
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right is not None:
                stack.append((node.right, depth + 1))
            if node.left is not None:
                stack.append([node.left, depth + 1])
        return max_depth
```

## 参考
- https://github.com/komdoroid/arai60/pull/17 (komdoroid — 104. Maximum Depth of Binary Tree)
- https://github.com/nicah4o/arai60/pull/20 (nicah4o — 104. maximum depth of binary tree)
- https://github.com/jjysogfy/arai60-202603/pull/10 (jjysogfy — 104. maximum depth of binary tree)
- https://github.com/h-masder/Arai60/pull/22 (h-masder — 104. Maximum Depth of Binary Tree)
- https://github.com/goto-untrapped/Arai60/pull/45 (goto-untrapped — 104. Maximum Depth of Binary Tree)
