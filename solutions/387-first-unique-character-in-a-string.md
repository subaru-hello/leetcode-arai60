# 387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-12, 60min, △)

- 繰り返しているかどうかは、最初から最後までを舐めないと分からない。ただ、愚直にユニークで一番目の数字を調べるのだと時間効率が悪い気がした。

- stringをkeyにして、valueにindex, 頻度のtupleを入れたい。tupleはimmutableだから、valueがある場合、valueのindexの方を保持して頻度を1増やせないかと思った

> コンテナデータ型
>
```
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
```

> https://docs.python.org/ja/3/library/collections.html#collections.Counter

### 実装
```python
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
      counter = Counter(s)
      for i, char in enumerate(s):
        if counter[char] == 1:
            return i
      return -1

```

## Step2
- counterを使った例を写経してしまった。が、counterを使わない方法も見てみたい
- Counterは、dictのサブクラス、要素をdictのkey, 要素の回数をdictのvalueにしてくれる


```python
class Solution:
  def firstUniqChar(self, s: string) -> int:
    char_to_count = {}
    for char in s:
        char_to_count[char]  = char_to_count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if char_to_count[char] == 1:
            return i
    return -1
```


## 参考
- https://github.com/mamo3gr/arai60/pull/15
> Python 3.7から、辞書の要素が挿入順に取り出せるのでありがたい（インデックスでのソートが不要）。
そうなんだ
> 順序が必要な場合は collections.OrderedDictを使う必要があった

- https://github.com/komdoroid/arai60/pull/5#discussion_r2569568326

> https://discord.com/channels/1084280443945353267/1233603535862628432/1238208008182562927

川上から文字が流れてくる話は、どんぶらこの桃が文字になっている情景を思い浮かばせられた。シフト制の話は、他のアルゴリズムの解説（塔を登って数字を探す？）にもあったような気がする。

>  https://discord.com/channels/1084280443945353267/1200089668901937312/1201210890142351401
再帰の考え方は、上司と部下の例を使っている。

- https://github.com/mamo3gr/arai60/pull/15/changes#r2651929897

- https://github.com/olsen-blue/Arai60/pull/15

LinkedHashMapを使うといいらしい。LinkedHashMapは、「挿入順を保持するHashMap」だから、python3.7以降であれば通常のdictで問題なさそう。
> https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = {}
        for char in s:
            char_to_count[char] = char_to_count.get(char, 0) + 1
        
        # counterは挿入順なので、最初に count==1 のものが最初のunique char
        for char, count in char_to_count.items():
            if count == 1:
                return s.index(char) # .indexで再捜査が走るからenumarateの時より効率が悪い。s.index()を使う方は「最悪、文字数ぶん走査が増える」ので合計O(n²)になる可能性がある。
        return -1
```

- https://github.com/chanseok-lim/arai60/pull/8
- https://github.com/Yoshiki-Iwasa/Arai60/pull/14
- https://github.com/h-masder/Arai60/pull/16
