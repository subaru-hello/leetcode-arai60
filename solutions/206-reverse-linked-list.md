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
意識したこと
- 組み込み関数と名前衝突が起きる可能性も考慮に入れて変数・関数定義をする。
- １行１代入文にする。
１行１代入文にすると、少し負荷が軽減された感覚がある。なんか、脳に一時的に置いておく情報を少なくできた感じ。
今回における変数宣言には、参照先を一旦退避する目的と、値を書き換える目的があるかも。


```python
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```