# 206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

カテゴリ: LinkedList

---

## attempt 1 (2026-05-26, 47min, △)

_ここに思考プロセスとコードを書く_
まず、linked listを定義する方法もわからない。
最小個数0~最大個数5000の範囲で値を受け取り、順番を入れ替える。
思いついたのは、先頭と最後尾をswapしていく方法。n/2 O(n)のオーダーで解けそう
あれ、linked listってランダムアクセスじゃないかもしれない。swapできないかも。
受け取ったheadの向きをtailにしていくといけるかも

```python
def reverseList(self, head):
  next = head.next  
  current = head
  head.next = current
  return reverseList(current, head)
```

---

## references

_(1回目クリア後に自動収集される)_

## notes

## attempt 2
head, curr, prevという概念があると知った。

```python
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev 
```

## attempt 3