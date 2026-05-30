# 82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

## ルール
- **Step 1**: 答えを見てもOK、まず正解させる
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-05-30, 174min, △)
- 重複したら消す。前回は重複したら次のオブジェクトをpointするpointerを次にずらすだけだった。が、今回は、次にずらした後、現在のオブジェクトのpointerを外す必要がありそう。

```python

class Solution(object):
  def deleteDuplicates(self, head):
    sentinel = ListNode(0, head)
    prev = sentinel
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
          while curr.next and curr.val == curr.next.val:
            curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return sentinel.next

```

## Step2
- まずLinkedListでは、先頭ノード自体が削除される場合に備えて、呼び出し元に新しい先頭を返せるよう、番兵という概念を使う。
- ポインタは2個用意する
  - prev: 確定済リストの末尾
  - curr: これから判定するリスト
- ループでcurrの値を一つづつ見る
- currentとcurrentの次が同じなら一つの重複塊として捉える。重複が続く限りcurrentを次に進める。塊の最後に来たら、prev.nextをcurrent.nextに繋ぎかえる。そうすることで、重複塊をLinkedListから消すことができる。
- curr = curr.nextのような、走査対象を次に進める処理のイメージがだいぶ湧いてきた。


```python
class Solution(object)
  def deleteDuplicates(self, head):
    sentinel = ListNode(0, head)
    prev = sentinel
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
          while curr.next and curr.val == curr.next.val:
            curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return sentinel.next

```

## 参考
- https://github.com/olsen-blue/Arai60/pull/4
- https://github.com/momeemt/LeetCode/pull/4
- https://github.com/chanseok-lim/arai60/pull/13
- https://github.com/Yoshiki-Iwasa/Arai60/pull/2

> node, nextNode なんですが、node はもうすでに取っておくことが確定したものの末尾であり、nextNode は取っておくべきか否かをためつすがめつしている対象ですよね。つまり、フォーカスは nextNode のほうにあるはずです。
https://github.com/goto-untrapped/Arai60/pull/43#discussion_r1695372547

めちゃくちゃコメントがある。読むだけでも価値がある。
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0