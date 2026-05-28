# 141. Linked List Cycle

## 問題
https://leetcode.com/problems/linked-list-cycle/

カテゴリ: LinkedList（arai60 順1/60）

## 学習方法

### Step 1
答えを見てもいいのでとにかく正解になったらOK（[標準的な進め方](https://docs.google.com/document/d/1bjbOSs-Ac0G_cjVzJ2Qd8URoU_0BNirZ8utS3CUAeLE/edit?tab=t.0#heading=h.6ana9osx0wrd)と同様）
- LinkedListを受け取って、LinkedListが循環しているかどうかを返す
- 0~10000の範囲の個数の値がlistに入るってことは、オーダーがO(n乗2)でも間に合いそう
- posはlist最後尾のNodeがpointする位置。-1か正常な値になる。
- posはパラメータで渡されない

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```

### Step 2
1. コードを自分なりに整形する
まだ自分なりに、ができないので３回シャドーイングした

2. 他の人のコードとコメントを読み、それを踏まえて再整形する。正解することを確認する（ここでレビュー依頼をする＝本 Pull Request）
- current一つをとっても、現場での使われ方との乖離や「現在処理中である変数」であることが自明なのにわざわざ変数名で表現する必要がない、といった観点がある
- 箱を用意する。listを一つづつ箱に格納していく。もし格納先が埋まっていたらサイクルがある。格納先が埋まっていない場合、格納して次に進める、というフローは想像しやすいと思った。
- なんでsetなのかは後で調べる

```python

class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) → bool:
        visited = new set()
        node = head
        while node:
          if node in visited:
            return True
          visited.add(node)
          node = node.next
        return False
```


### Step 3
レビューを踏まえて整形する。その後、10分以内にエラーを出さずに書く

---

## attempt 1 / Step 1 (2026-05-28, 47min, △)

参考にした他者 PR / 資料:
- https://github.com/mamo3gr/arai60/pull/1
- https://github.com/olsen-blue/Arai60/pull/1
- https://github.com/momeemt/LeetCode/pull/1
- https://github.com/fuga-98/arai60/pull/2
- https://github.com/chanseok-lim/arai60/pull/10

## memo
> CPU のクロック周波数は、最高で 5.8GHz のものが出ていますが、おおよそ数 GHz と覚えておけば大丈夫だと思います。
https://github.com/momeemt/LeetCode/pull/1#discussion_r1569731631

> ループで書いたほうが平均的なソフトウェアエンジニアにとって分かりやすいコードになるようです
https://github.com/momeemt/LeetCode/pull/1#discussion_r1568961359

> 純粋に面接のテクニックとしては、「Python の再帰の限界は?」と聞かれたときに、他の言語の話で逃げることはできます。本当に知りたいことは、スタックサイズの上限という概念があるか、だからです,,,
https://github.com/momeemt/LeetCode/pull/1#discussion_r1575068790

> 償却計算量（amortized cost）とは、一連の操作全体の計算量をその操作回数で割ったときの一回あたりのコストです
https://github.com/fuga-98/arai60/pull/2#discussion_r1957477394