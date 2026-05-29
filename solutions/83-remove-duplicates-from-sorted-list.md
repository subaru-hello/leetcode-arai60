# 83. Remove Duplicates from Sorted List

## 問題
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

カテゴリ: LinkedList（arai60 順3/60）

## 学習方法

### Step 1
答えを見てもいいのでとにかく正解になったらOK（[標準的な進め方](https://docs.google.com/document/d/1bjbOSs-Ac0G_cjVzJ2Qd8URoU_0BNirZ8utS3CUAeLE/edit?tab=t.0#heading=h.6ana9osx0wrd)と同様）

- sorted linked listの重複を排除する。重複を排除してソート済みlinked listを返すなら、渡されたlinked listをset関数に入力して、set関数から再度linked listを作り直せばいいと最初は思った。しかし、再度linked listを作る方法がわからず断念。
- 他の方の解法を見て、現在見ているnodeが持つ値と隣のnodeの値を比較して同じだった場合に１つポインターを進めていけばいいとわかった。


```python

class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        while node is not None:
            if node.next is not None and node.val == node.next.val:
              node.next = node.next.next
            else:
                node = node.next
        return head

```

### Step 2
1. コードを自分なりに整形する
- is not Noneを外せそうなことに気がついた。できるだけif文の中にnot入れたくない気持ちを持った。少し読みづらくなるため。
n
```python
class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
```

2. 他の人のコードとコメントを読み、それを踏まえて再整形する。正解することを確認する（ここでレビュー依頼をする＝本 Pull Request）
- 前後のnodeという概念を取り入れると、条件分岐をシンプルにできそう。write/readパターンというらしい
- currがcurr.nextの値と一致しなくなるまで、currを次に進める。一致しない場合、prevのnextをcurrが一致しなかった場所まで進める。



```python
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        previousNode = head
        currentNode = head
        while currentNode:
            if currentNode.val != previousNode.val:
                previousNode.next = currentNode
                previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = None 
        return head 


```


### Step 3
レビューを踏まえて整形する。その後、10分以内にエラーを出さずに書く

---

## attempt 1 / Step 1 (2026-05-29, 79min, △)

参考にした他者 PR / 資料:
- https://github.com/mamo3gr/arai60/pull/3
- https://github.com/olsen-blue/Arai60/pull/3
- https://github.com/momeemt/LeetCode/pull/3
- https://github.com/chanseok-lim/arai60/pull/12
- https://github.com/Yoshiki-Iwasa/Arai60/pull/1
- https://github.com/enari-k/LeetCode/pull/67


_ここに思考プロセスとコードを書く_

```python

```

---

## references

_(1回目クリア後に自動収集される)_

## notes
