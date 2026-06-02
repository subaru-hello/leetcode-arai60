# 703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

## ルール
- **Step 1**: 答えを見てもOK、まず正解させる
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## attempt 1 / Step 1 (2026-06-02, 60min, △)
- python3ってheapのライブラリは用意されていたっけ？と思った→あったhttps://docs.python.org/3/library/heapq.html
- sort済みのlistが渡される。ソート済みって重要だけど、面接では言及されなそう。LeetCodeの条件を読むことに慣れておくのは大事かも。コーディングオンライン面接の時に条件を明確にしていく時に使えそう
- priority queueの書き方がわからなかったので、見ないでかけるまでシャドーイングした

```python3
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

## Step2
- heapを知らないと解けない
- min heapがデフォルト。min heapには任意の数の値を入れることができる。
> The interesting property of a min-heap is that its smallest element is always the root, heap[0].
- min heapの先頭にはheap内の最小の値を取得できるという特性を利用して、heapに格納する値の個数上限を決めると良さそうということがわかった。上限が決まっていて、先頭に小さい値が来る、言い換えると、昇順に並んでいるのであれば、heapの容量をkにして、先頭を取得すれば、全体の上位k番目を取得できるということになる。と理解した。
- 他の方が書いたコードも読んだが、自分のコードが比較的コード量が少なく、条件分岐の数が少ないから認知負荷が低い。
- 高さを保つのが大事らしい  

```python3
import heapq
class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.heap = []

    for num in nums:
        self.add(num)
    
  def add(self, val) -> int:
    heapq.heappush(self.heap, val)
    if len(self.heap) > self.k:
        heapq.heappop(self.heap)

    kth_largest = self.heap[0]
    return kth_largest
```

## 参考
- https://github.com/mamo3gr/arai60/pull/8
- https://github.com/olsen-blue/Arai60/pull/8
- https://github.com/Yoshiki-Iwasa/Arai60/pull/7
- https://github.com/h-masder/Arai60/pull/9
- https://github.com/Shunii85/arai60/pull/8
