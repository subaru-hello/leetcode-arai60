# 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-01, ≤10 min, ok) — 復習

### 1-A: 自力で考えたこと
- データ構造案: 追加のノードは持たない（O(1) 空間を狙う）
- アルゴリズム案: Floyd の Tortoise and Hare。slow は1歩、fast は2歩。

### 1-B: 詰まった点
- なし（既出問題の復習。10分以内に再現）

### 1-C: 自分が理解した解法
- サイクルがあれば fast は slow に毎周回1歩ずつ近づくので必ず衝突する。
- サイクルが無ければ fast が末尾（None）に到達してループが終わる。
- ノード一致は `is`（同一オブジェクト判定）で見る。

### 1-D: 実装
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
```

### レビューメモ（Step 2 で反映候補）
- 先頭の `if head is None: return False` は冗長。`head is None` なら `fast is None` で while 条件を即抜けるので、ガード無しでも同じ挙動。
- `slow = fast = head` で初期化を1行にできる。
- 面接では「このガードは while 条件でカバーされるので消せます」と説明できるのが本質。

## 参考
- (arai60 community PRs — 後述の注記参照)
