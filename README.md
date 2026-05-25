# leetcode-arai60

SWE協会（一般社団法人ソフトウェアエンジニアリング協会）推奨フローに従い、新井康平氏選定の LeetCode 69問（通称 arai60）を Python で反復練習するリポジトリ。

- 公式問題リスト: https://1kohei1.com/leetcode/
- LeetCode リスト: https://leetcode.com/list/?selectedList=xt2qzsi5
- 練習会: SWE協会 Discord

## レビュー駆動フロー

1問1ブランチ・1PR・**`.md` ファイルにコードと思考を混ぜて書く**。PR は merge せず open のまま、各 attempt を commit で積んでレビューコメントを溜める。

1. 自力で解く（5〜10分詰まれば答えを見る）
2. LeetCode で AC → ブランチを切って `solutions/<#>-<slug>.md` に attempt を書く
3. PR を出して Discord `#leetcode_subaru2918` で一声かける
4. レビューコメントが付いたら次の attempt に反映して push
5. 3回連続10分以内クリアで master 判定 → PR は **close** か **open のまま放置**（merge しない）

ブランチ名: `feat/<#>-<slug>`（例: `feat/206-reverse-linked-list`）
ファイル名: `solutions/<#>-<slug>.md`（例: `solutions/206-reverse-linked-list.md`）

## 運用ルール

### 日次（毎日）

1. `/arai60` でその日のキューを表示（新規1問 + 復習1問）。
2. `/arai60 start <slug>` で計測開始 → 自力で解く。**5〜10分詰まったら答えを見る**（粘らない）。
3. LeetCode で AC → `/arai60 done <slug> <所要分> <ok|ng>`。1回目クリア時は自動で `/arai60 refs` が走り、他者コードが `solutions/<#>-<slug>.md` の references セクションに追記される。
4. references を読んで洗練された解法を理解する。
5. 次回復習日まで放置 → spaced repetition で自動的にキューに戻る。

### 週次（金曜）

`/arai60 review` で集計確認。詰まりカテゴリを翌週の重点に。

## マスター判定（SWE協会基準）

**10分以内にエラーなく実装** を **3回連続** クリア → `mastered`。

| status | 次回復習日 |
|---|---|
| `untouched` | 未着手 |
| `learning` (1回目クリア) | 翌日 |
| `reviewing` (2回連続) | 3日後 |
| `reviewing` (あと1回でmaster) | 7日後 |
| `mastered` | 30日後（劣化チェック） |
| 10分超過 or NG | カウントリセット、翌日に戻す |

## 全69問リスト

進捗管理は [`tracker.md`](./tracker.md) を見てください。以下は問題への直リンクのみ。

### LinkedList（5問）
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [143. Reorder List](https://leetcode.com/problems/reorder-list/)

### Stack（4問）
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

### Heap / PriorityQueue（6問）
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [355. Design Twitter](https://leetcode.com/problems/design-twitter/)

### HashMap（6問）
- [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

### Graph / BFS / DFS（6問）
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

### Tree / BT / BST（11問）
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [235. Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### Sort（3問）
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### Dynamic Programming（9問）
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [198. House Robber](https://leetcode.com/problems/house-robber/)
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [139. Word Break](https://leetcode.com/problems/word-break/)
- [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

### Binary Search（3問）
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

### Recursion（4問）
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [46. Permutations](https://leetcode.com/problems/permutations/)
- [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

### Sliding Window（4問）
- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

### Two Pointers（5問）
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [15. 3Sum](https://leetcode.com/problems/3sum/)
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

### Greedy + Backtracking（3問）
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [55. Jump Game](https://leetcode.com/problems/jump-game/)
- [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)

## ディレクトリ

```
leetcode-arai60/
├── README.md                       # このファイル
├── tracker.md                      # 全問題の進捗テーブル（single source of truth）
├── queue.md                        # 今日のキュー（コマンドが生成、.gitignore対象）
├── log/YYYY-MM-DD.md               # 日次ログ（.gitignore対象）
└── solutions/<#>-<slug>.md         # 実装 + 思考 + references + notes
```

## solutions/<#>-<slug>.md のテンプレ

```markdown
# <#>. <問題名>

<LeetCode URL>

カテゴリ: <category>

---

## attempt 1 (YYYY-MM-DD, NN min, ok|ng)

最初に考えたこと:
- ...

\`\`\`python
def solve():
    ...
\`\`\`

詰まった点・気づき:
- ...

---

## attempt 2 (YYYY-MM-DD, NN min, ok|ng)

ref1 を読んで気づいた:
- ...

\`\`\`python
def solve():
    ...
\`\`\`

---

## references

- ref1: LeetCode Editorial — <approach>
  \`\`\`python
  ...
  \`\`\`
- ref2: neetcode — <approach>
- ref3: Python標準ライブラリ活用 (<library>)

## notes

- 学んだこと・パターン
```

## PR の出し方

```bash
git checkout -b feat/206-reverse-linked-list
# solutions/206-reverse-linked-list.md に attempt 1 を書く
git add solutions/206-reverse-linked-list.md
git commit -m "206 reverse-linked-list: attempt 1"
git push -u origin feat/206-reverse-linked-list
gh pr create --fill
```

PR 本文は **LeetCode URL 1行のみで OK**（hayashi-ay 流）。

## コマンド一覧

| コマンド | 用途 |
|---|---|
| `/arai60` / `/arai60 today` | 今日のキュー表示・生成 |
| `/arai60 start <slug>` | 計測開始、`solutions/<#>-<slug>.md` テンプレ作成 |
| `/arai60 done <slug> <分> <ok\|ng>` | attempt 記録、status 更新、references 自動取得 |
| `/arai60 refs <slug>` | 他者コード取得（手動再実行用） |
| `/arai60 review` | 週次集計 |
