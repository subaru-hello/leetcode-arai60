# 142. Linked List Cycle II

## 問題
https://leetcode.com/problems/linked-list-cycle-ii/

カテゴリ: LinkedList（arai60 順2/60）

## 学習方法

### Step 1
答えを見てもいいのでとにかく正解になったらOK（[標準的な進め方](https://docs.google.com/document/d/1bjbOSs-Ac0G_cjVzJ2Qd8URoU_0BNirZ8utS3CUAeLE/edit?tab=t.0#heading=h.6ana9osx0wrd)と同様）

```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        node = head
        while node:
            if node == -1:
              return None
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None
```

### Step 2
1. コードを自分なりに整形する
- 入出力の型定義は呼び出し側の手間、コードジャンプをする手間を減らすために書いた方がいいのかな
- == -1を見て、何を意味するのか分からないかも。そもそも、-1のケースを書かなくても通った。が、「-1のケースで必ずNoneを返す」ことを明示していると、後でコードを読んだ人のためになるかもしれない。

```python

class Solution(object):
    def detectCycle(self, head):
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

```

2. 他の人のコードとコメントを読み、それを踏まえて再整形する。正解することを確認する（ここでレビュー依頼をする＝本 Pull Request）
- さっきのコードは結構簡潔に書くことが出来たと思う。他の人のPRを見ると、ウサギとかめを使っている人が結構いた。他の人のコードも読めるといいとのことなので、自分もウサギとカメを使ってみる。
- 衝突する場所をまず探す。衝突点をそのまま返してしまうと、スタート地点の可能性を排除できなくなってしまう。そのため、スタート地点を除外するためのwhile文を実装している

```python
class Solution(object):
  def detectCycle(self, head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            node = head
            while node != slow:
                node = node.next
                slow = slow.next
            return node
    return None
```


### Step 3
レビューを踏まえて整形する。その後、10分以内にエラーを出さずに書く

---

## attempt 1 / Step 1 (2026-05-28, 51min, △)

参考にした他者 PR / 資料:
- https://github.com/mamo3gr/arai60/pull/2
- https://github.com/olsen-blue/Arai60/pull/2
- https://github.com/momeemt/LeetCode/pull/2
- https://github.com/chanseok-lim/arai60/pull/11
- https://github.com/enari-k/LeetCode/pull/66

---

## references

> つまりは「コードの仕様を変えたいときに巨大なコードベースを掘って見つけ、該当箇所を変更する綺麗な案を作り、他のチームメイトにそれでうまくいくことを説明して、プロダクションに持っていくこと」なので、コードが書けるかどうかはあまり重要ではない。
> パズル的な他の解き方がある問題というのはとてもいいです。なぜかというと「パズル的な解き方を出題者が説明して、それを理解して実装してもらう」と、上の要素のうち「自然言語での説明を理解する」「変更案を作る」「コードの説明する」といった要素が自然に確認できるし、候補者がいい体験だったと思ってくれるからです。
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.jfs03xpyyrfl

_(1回目クリア後に自動収集される)_

## notes
