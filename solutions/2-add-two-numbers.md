# 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

## ルール
- **Step 1**: 答えを見てもOK、まず正解させる
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## attempt 1 / Step 1 (2026-05-30, 84min, △)
- 繰り上げありだから、

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
      dummy = ListNode()
      tail = dummy
      carry = 0

      while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry

        carry = total // 10
        tail.next = ListNode(total % 10)
        tail = tail.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next
      return dummy.next
```

## Step2
- 自分なりに整形、となると途端に難しくなる
- まず準備をして、while野中で処理を進めて、最後に先頭を返す
- 前回、valueをvに省略しすぎて何を表しているのかがわからなくなった
- 繰り上げ処理と、位に配置する合計値の算出のイメージが湧いてきた


```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sentinel = ListNode()
        tail = sentinel
        carry = 0

        while l1 or l2 or carry:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            total = value_1 + value_2 + carry

            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return sentinel.next
```

- 無理に三項演算子にせず、ヘルパー関数を用意した方が、コードの読み手の目の移動を減らせる

- 変数名にvalueとつけるのは違和感があったが、他にいい変数名を思いつかなかった。

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def get_value(node):
          if node is None:
            return 0
          return node.val

        sentinel = ListNode()
        tail = sentinel
        carry = 0

        while l1 or l2 or carry:
            value_1 = get_value(l1)
            value_2 = get_value(l2)
            total = value_1 + value_2 + carry

            carry = total // 10
            tail.next = ListNode(total % 10)
            
            tail = tail.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        return sentinel.next

```

## 参考
- https://github.com/mamo3gr/arai60/pull/5
- https://github.com/olsen-blue/Arai60/pull/5
- https://github.com/momeemt/LeetCode/pull/5
- https://github.com/chanseok-lim/arai60/pull/14
- https://github.com/Yoshiki-Iwasa/Arai60/pull/4
