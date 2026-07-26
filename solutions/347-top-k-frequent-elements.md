# 347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

## ルール
- **Step 1**: 答えを見てもOK、まず正解させる
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## attempt 1 / Step 1 (2026-06-03, 109min, △)
- どんな順番でもいいから、与えられた配列の中でk個の頻繁に出現する要素？をListで返却する
- o(n log n)で、ユニークな値を返す
- frequentはpriority queueの出番だと思う
- https://docs.python.org/3.11/library/collections.html#collections.Counter.most_common
- ライブラリを使うと、「数値と出現数のハッシュ」と「上位k回出現した数値」を少ないchunkで計算できる

```python
from collections import Counter

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequent = Counter(nums)
    return [n for n, _ in frequent.most_common(k)]
```

## Step2
- 毎回、Step2が苦手。Step1の段階で、写経してるから、Step1の内容を自分なりにアレンジができない
- が、今回はライブラリを自前で実装することで内部を理解することに徹してみる
- Counterはhashtableらしい。numsをループしてhash tableを作れそう
- hashtableは「優先度」をどうやって作る？hashtableって値の大きさでソートできるのか？インデックスアクセスをするから、アドレスは持っていそうだけど、頻度ってどうやって表現できるんだ？
優先度をどうやって作るか→bucket sortで、出現頻度毎にカテゴリ（バケツ）を作る [3]=[1]
- hashtableはdict(辞書型)を指すのか。dict()を使うか{}で表現できる
- バケツのindexは出現頻度だから、top kを出すためにrangeは降順で計算した

```python
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for i in range(len(buckets) -1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]

```


## 参考
- https://github.com/mamo3gr/arai60/pull/9
- https://github.com/olsen-blue/Arai60/pull/9
- https://github.com/Yoshiki-Iwasa/Arai60/pull/8
- https://github.com/h-masder/Arai60/pull/10
- https://github.com/Shunii85/arai60/pull/9


frequent.most_commonのソースコード
- 内部でheapq(https://docs.python.org/ja/3/library/heapq.html)を使っている
```python
def most_common(self, n=None):
    if n is None:
        return sorted(self.items(), key=itemgetter(1), reverse=True)
    else:
        return heapq.nlargest(n, self.items(), key=itemgetter(1))
```

```python
# ❌ KeyError on first sight of n
freq[n] = freq[n] + 1

# ✅ Fix: provide a default of 0
freq[n] = freq.get(n, 0) + 1
```

```
range(start, stop, step)
```
(c.f: https://docs.python.org/ja/3/library/stdtypes.html#typesseq-range)

```
result = [1, 2, 3, 4, 5]

result[:2]  # → [1, 2]   最初のk個だけ取り出す
result[:3]  # → [1, 2, 3]
```