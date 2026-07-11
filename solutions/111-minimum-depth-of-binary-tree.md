# 111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-11, ?? min, ??)

### 1-A: 自力で考えたこと
- データ構造案: binary tree
- アルゴリズム案: depth first search

### 1-B: 詰まった点
- min_depthの初期値を0にしていたが、初回にrootのdepthである1と比較するときに毎回0になってしまった

### 1-C: 自分が理解した解法
- maximum depthの時と同じような考え方を踏襲した

### 1-D: 実装
```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        min_depth = float('inf')
        while stack:
            node, depth = stack.pop()
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        return min_depth
```

## Step2
子がNoneのnodeを「最短で探す」という点で、BFSの方が適したアルゴリズムだと気づいた

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
        return 0
```

**概念: なぜ min depth は BFS が本命か（max depth との非対称）**
- BFS は浅い層から順に見るので、**最初に到達した葉の深さがそのまま答え**。見つけた瞬間 `return depth` で早期終了でき、木を全部なめる必要がない。
- 反復DFS(Step1)も正しいが、min を更新し切るために**必ず全ノードを訪問**する。「最短を探す」問題は BFS の早期終了と相性が良い、が定石。
- #104(max depth) では DFS でも BFS でも全探索が要り差が出なかった。min になった途端 BFS が有利になる — この非対称を押さえる。

**別解: 再帰版と「片側 None」の罠（#111 最大の落とし穴）**
```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```
- 素朴な `1 + min(minDepth(left), minDepth(right))` は**バグる**。例 `[1,2]`（右が None）で `minDepth(None)=0` を拾い `1` を返すが、正解は `2`（1→2 の葉まで）。
- 原因: **片方だけ子が無い節点は葉ではない**。その空側(深さ0)を min の候補に入れると最小を汚染する。だから「片側が None ならもう一方だけ潜る」ガードが要る。
- #104(max) との決定的違い: max は空側の 0 を拾っても最大に影響しないのでガード不要。min は 0 が最小を壊すのでガード必須。Step1 で `min_depth=float('inf')` 初期化に詰まったのも同根（min の単位元は inf、max は 0/-inf）。

**スタイル / レビュー観点**
- `is None` / `is not None` を一貫使用できている（#104 のレビュー指摘点をクリア済み）。
- BFS 版末尾の `return 0` は、非空の木なら必ず葉に当たるので**到達しない**。「木が非空なら while 内で必ず return する」と1行コメントを添えるか、`raise`/`assert` にする流儀もある。
- `(node, depth)` のタプルは、分解して `node, depth = queue.popleft()` しているので可読。積んだまま使うなら要素名を中身が分かる形にする、が #104 でも出た指摘。
- 出典比較用: goto-untrapped/Arai60#46（反復・再帰の両方に言及）, komdoroid/arai60#18。

## 参考
- https://github.com/komdoroid/arai60/pull/18 (komdoroid — 111. Minimum Depth of Binary Tree)
- https://github.com/nicah4o/arai60/pull/21 (nicah4o — 111. minimum depth of binary tree)
- https://github.com/jjysogfy/arai60-202603/pull/11 (jjysogfy — 111. minimum depth of binary tree)
- https://github.com/h-masder/Arai60/pull/23 (h-masder — 111. Minimum Depth of Binary Tree)
- https://github.com/goto-untrapped/Arai60/pull/46 (goto-untrapped — 111. Minimum Depth of Binary Tree)
