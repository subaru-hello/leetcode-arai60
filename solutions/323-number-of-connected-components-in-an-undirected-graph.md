# 323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-06, 10 min, ok)

### 1-A: 自力で考えたこと
- データ構造案: graph
- アルゴリズム案: 連続した塊が何個あるのかを探す系なので、DFSかBFSかUnionFindを使用したら解けそう

(a,b), (b, c)＝連結している
(a,b), (c, d)=連結していない

ヒント見る前
nodeの数が最大2000個、edgeの数が最大5000個で、edgeのリピートがない
union findの書き方が分からなかったのは収穫。あとで調べる。
0番目のnodeをスタート地点として、index+1...nでnodeを見ていく。
(a,b)はそのままstackに入れて、(a,b)のbと次のvertexである(b,c)のbが同じ値になっているのかを見ていく。

ヒント見た後
島の探索の時は、与えられたgridが整列していたから上下左右で深さ探索できた。
今回は与えられるListが整形されていないので、一度整形し直す必要がある。
 edges = [[0,1],[1,2],[3,4]]   →   graph[0] = [1]
                                      graph[1] = [0, 2]
                                      graph[2] = [1]
                                      graph[3] = [4]
                                      graph[4] = [3]



### 1-B: 詰まった点
与えられたedgeをそのまま走査して連結成分を探そうとして詰まった。

### 1-C: 自分が理解した解法
塗り初めの回数を数えていく。

### 1-D: 実装
dfsバージョン
```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        def visit_connected_component(node) -> None:
            visited[node] = True
            for nxt_node in graph[node]:
                if not visited[nxt_node]:
                    visit_connected_component(nxt_node)
        
        connected_components = 0
        for node in range(n):
            if not visited[node]:
                connected_components += 1
                visit_connected_component(node)
        return connected_components
```

bfsバージョン

```python
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        connected_components = 0

        for start_node in range(n):
            if visited[start_node]:
                continue

            visited[start_node] = True
            connected_components += 1

            queue = deque([start_node])
            while queue:
                node = queue.popleft()
                for nxt_node in graph[node]:
                    if not visited[nxt_node]:
                        visited[nxt_node] = True
                        queue.append(nxt_node)
        
        return connected_components



```

union findバージョン

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find_root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for a, b in edges:
            root_a, root_b = find_root(a), find_root(b)
            if root_a != root_b:
                parent[root_a] = root_b
        
        roots = set()
        for i in range(n):
            roots.add(find_root(i))
        return len(roots)

```

## Step2

dfsを、再帰じゃなくてstack+loopにすると、コードの読み方がbfsと似るため、stackとqueueの差分理解につながっていいと感じた
```python
def visit(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        for nxt in adj[node]:
            stack.append(nxt)
```

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        def visit(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node in seen: continue
                seen.add(node)
                for nxt_node in graph[node]:
                    stack.append(nxt_node)

        connected_components = 0
        for node in range(n):
            if node in seen: continue
            connected_components += 1
            visit(node)
        return connected_components
```

```python
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        def visit_connected_nodes(node):
            seen.add(node)
            for nxt_node in adj[node]:
                if nxt_node not in seen:
                    visit_connected_nodes(nxt_node)
        
        num_of_connected_nodes = 0
        for node in range(n):
            if node in seen:
                continue
            num_of_connected_nodes += 1
            visit_connected_nodes(node)
        return num_of_connected_nodes

```

3rd
訪問済みにするタイミングがわからなくなってしまう。訪問ずみ＝チェック済みと考えると汎用性が高くなると気づいた。
stackアルゴリズムは、取り出す側でチェック済みにするから、listのメモリサイズが膨張する恐れがある。皿を乗せる人と皿を取る人がいる。多分、取る人はイライラする場合がある。「もう洗い終わった印をつけてるのに何度も乗せないでくれる？」的な。なぜなら、皿を乗せる人は印をみてない。

一方、queueアルゴリズムは、列に並ばせる側がチェックするから、listのメモリサイズは節約できる。フェス入り口の待ち行列を想定。客は待ち行列に並ぶために列の入り口でチェックをもらう必要がある。並んでいる人は皆チェックが完了している。

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def visit_adj_components(start_node):
            stack = [start_node]
            while stack:
                node = stack.pop()
                visited.add(node)
                for nxt_node in adj[node]:
                    if nxt_node not in visited:
                        stack.append(nxt_node)

        
        nums_of_connected_components = 0
        for node in range(n):
            if node not in visited:
                nums_of_connected_components += 1
                visit_adj_components(node)
        return nums_of_connected_components
```

4th
stack=チェックするのは皿を取る側、queue=チェックするのは列に並ばせる側、というわけではなく、チェックするタイミングは選べることに気づいた。

コンテナ(stack/queue)と、チェックの側(取り出す時/入れる時)は独立。
膨張の有無を決めるのは「コンテナの種類」ではなく「チェックの側」。

### ① stack × 取り出す側チェック（O(E)）
皿を乗せる人は印を見ない → 同じ皿が重複して積まれる → 取る人が pop時に弾く。
```python
def visit(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nxt in adj[node]:
            stack.append(nxt)
```

### ② stack × 入れる側チェック O(V)）
フェス方式を皿に適用。乗せる人が印を見るので重複が積まれない。
```python
def visit(start):
    visited.add(start)
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in adj[node]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
```

### ③ queue × 入れる側チェック（O(V)）
②の `pop()` を `popleft()` にしただけ。列に並ぶ人は全員チェック済み。
```python
from collections import deque
def visit(start):
    visited.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

### ④ queue × 取り出す側チェック（O(E)）
①の `pop()` を `popleft()` にしただけ。BFSなのに列が膨れるので普通は選ばない。
```python
from collections import deque
def visit(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for nxt in adj[node]:
            queue.append(nxt)
```

## 参考
- https://github.com/hayashi-ay/leetcode/pull/37
- https://github.com/goto-untrapped/Arai60/pull/35
- https://github.com/Ryotaro25/leetcode_first60/pull/20
- https://github.com/kazukiii/leetcode/pull/20