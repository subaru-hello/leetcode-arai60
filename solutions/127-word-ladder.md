# 127. Word Ladder
https://leetcode.com/problems/word-ladder/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-09, 10 min, ok)

### 1-A: 自力で考えたこと
- データ構造案:
- アルゴリズム案:

### 1-B: 詰まった点
- wordの１文字を徐々に変えていく方法がわからず断念。答えを見て、みずに3回実施

### 1-C: 自分が理解した解法
- wordの長さをWL、アルファベットの総数をAL置き、最大WL*cAL回分走査する。さながらパチンコスロットのようにwordを１文字ずつアルファベットを交換していき、wordListに含まれているかを走査していく。
- 含まれていれば、次の文字へ移る


### 1-D: 実装
```python
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    nxt = word[:i] + char + word[i + 1:]
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
        return 0
```

## Step2
自分が実装したアルゴリズムは、文字数の長さが伸びれば伸びるほど計算量が増えてしまう点が懸念点だった。(各ケタ*アルファベットの数26文字)
word ladderは、最初の文字から最後の文字へ変遷していく過程で１文字づつ交換されていく。要は、１文字を伏せた形が同じなら隣と言える。
言い換えると、「あるパターン *ot を共有する単語どうしは、必ず1文字違い（=隣）」になる。こういう言い換え力って抽象化・汎化力向上につながると感じた。
Step1ではO(N·L·26) BFSだった。が、速度を詰めるなら隣接を *パターンで前処理してバケット化すれば実在する隣だけ辿れるから、26という定数を削れる。

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        buckets = defaultdict(list)
        for word in word_set | {beginWord}:
            for i in range(len(word)):
                buckets[(i, word[:i], word[i+1:])].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for nxt in buckets[(i, word[:i], word[i + 1:])]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, length + 1))
        return 0
```


## 参考
- https://github.com/komdoroid/arai60/pull/16 (komdoroid — 127. word ladder)
- https://github.com/tNita/arai60/pull/19 (tNita — 127. Word Ladder)
- https://github.com/nicah4o/arai60/pull/19 (nicah4o — 127. word ladder)
- https://github.com/jjysogfy/arai60-202603/pull/9 (jjysogfy — 127. word ladder)
- https://github.com/h-masder/Arai60/pull/21 (h-masder — 127. Word Ladder)
