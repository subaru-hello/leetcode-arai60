# 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-07, 60min, △)

### 1-A: 自力で考えたこと
- データ構造案: dictを作ることを思いついた
- アルゴリズム案: two sumが使えそうだと思った

- 受け取ったlist内の各string塊をalphabet順でソートして、keyにソート済みstring, valueをlistにしたdictを作れないかどうかが思い浮かんだ。
- そして、valuesをグルーピングして二次元配列として返せないか



### 1-B: 詰まった点
- keyにソート済みstring, valueにlistを入れる方法がわからなかった。そもそも、このアプローチでgroup anagramsを実現できるのかも不明。

### 1-C: 自分が理解した解法
- defaultdictを使ってデータ構造を構築するみたい
- tuple型とsortメソッドを使っていた

- list.sort()とsorted()が存在する。
list.sort(): 破壊的変更。元のlistをsortする
sorted(): 非破壊的変更。新しいリストを返す。
今回はoriginalの文字列を保持する必要があったことと、そもそも文字列がimmutableだったことを加味して、sorted()の方を採用した。

- 下記の例を参考にすればkeyをalphabet順にsortできそうだと思った。(original, sorted_str)とするtupleを
```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
```
https://docs.python.org/ja/3/howto/sorting.html

### 1-D: 実装
```python
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())
```

## Step2
- defaultdict()やlist()といった関数を使わずに実装できないか？と思った。特定の外部関数に依存した関数を実装してしまうと、解決策が狭まるのではないかと思ったから。


## 参考
- https://github.com/mamo3gr/arai60/pull/12
- https://github.com/olsen-blue/Arai60/pull/12
- https://github.com/chanseok-lim/arai60/pull/2
- https://github.com/Yoshiki-Iwasa/Arai60/pull/11
- https://github.com/h-masder/Arai60/pull/13
