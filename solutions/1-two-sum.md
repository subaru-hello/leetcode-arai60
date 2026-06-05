# 1. Two Sum
https://leetcode.com/problems/two-sum/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-05, 112min, △)

### 1-A: 自力で考えたこと
- データ構造案: hash map
- アルゴリズム案: 多分、two sumというアルゴリズムなのか？1番だから、基礎として扱われそう。今後、two sumの発展系が出てくるのではないだろうか。

### 1-B: 詰まった点
- target, index, num in numsを活用して解くのだろうと見立てて、hashを作るところまではなんとなく進めることができた。が、hashに入れた値をどう取り出せば、足し合わせたらtargetになる二つのpairを作れるのかが最初はわからなかった。

### 1-C: 自分が理解した解法
まず、keyをtarget - num1の計算結果・valueがindexになるhashを作成する。ここがO(n)
次に、target - num2 がkeyに存在するかを探していく。keyが見つかった場合、対応するvalueが走査中のindexと一致してはいけない。

なんか、コードでは書けるけど、解法を説明できない。いわゆる、今は、自分は解けるけど、次のシフトの人に引き継ぎができない状態なんだろう。

### 1-D: 実装
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}
        for n, i in nums:
            nums_to_i[target - n]: i

        result = []
        for n, j in nums:
            if target - n in  num_to_i and nums_to_i[target - n] != j:
                return [target - n, n]
        return result
```

↑直感で書いたら間違えた。
↓はAC。
- enumerateでindexとvalueを取り出す
- ループ間でコミュニケーションを取るには、補数を使用する。

```python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}
        for i, n in enumerate(nums):
            num_to_i[n] = i

        result = []
        for j, n in enumerate(nums):
            if target - n in num_to_i and num_to_i[target - n] != j:
                return [num_to_i[target - n], j]
        return result
```

## Step2
- for文自体をまとめれそう
- != jと評価している箇所が無駄そう
- 重要な要素が、target, num, index二つ

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums:
                return []
```

- seenというListを用意すると解けるらしい。なるほど

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []
```


## 参考
- https://github.com/mamo3gr/arai60/pull/11
- https://github.com/chanseok-lim/arai60/pull/1
- https://github.com/Yoshiki-Iwasa/Arai60/pull/10
- https://github.com/Shunii85/arai60/pull/11
- https://github.com/akmhmgc/arai60/pull/8

>     def find(self, node):
        while self.groups[node] != node:
            self.groups[node] = self.find(self.groups[node])
        return self.groups[node]

>これ、ぱっと見、動かないのですよ。node をたどっていくと、self.groups[node] が node にならないといけないんですが、そんなことは必ずではないでしょう。

ぱっと見で動くかどうかをデバッグできるようになってみたい