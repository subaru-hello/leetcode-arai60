# 139. Word Break
https://leetcode.com/problems/word-break/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-07-27, 3min, ok)

### 考えたこと
- dp[i] = 「s[0:i] が辞書の単語で分割できるか」
- dp[j] and s[j:i] in word_set で、「j までは既にたどり着ける」×「j から i が1単語」の両方を確認
- dp[j] のチェックが無いと、後ろだけ辞書の単語と一致していても実際には繋がっていない分割を許してしまう
- wordDict は set に変換してから in チェック（線形探索を避ける）

### 実装
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
        return dp[-1]
```

## Step 2 (2026-07-27)

### 考えたこと
- refs の startswith 版を試す。スライスのコピーを作らず s.startswith(word, i) で直接チェック
- dp[i] = True のとき、そこから word が続いていれば dp[i + len(word)] = True（単語1個分前進した位置に印をつける）
- dp[i] が False の位置は探索をスキップして無駄を省く

### 実装
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)

        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in word_set:
                if s.startswith(word, i):
                    dp[i + len(word)] = True
        return dp[-1]
```

## references

### ref1: olsen-blue — トップダウンDP（メモ化再帰、startswith 版）
https://github.com/olsen-blue/Arai60/pull/39

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @cache
        def is_can_segmented(from_index) -> bool:
            if from_index == len(s):
                return True
            for word in wordDict:
                if s.startswith(word, from_index):
                    if is_can_segmented(from_index + len(word)):
                        return True
            return False
        return is_can_segmented(0)
```

`s[j:i] in word_set` の代わりに `s.startswith(word, from_index)` で「今の位置から各単語が始まっているか」を直接チェックするアプローチ。スライスのコピーを作らずに済む。

### ref2: olsen-blue — ボトムアップDP（startswith 版、あなたのコードに近い）
https://github.com/olsen-blue/Arai60/pull/39

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        is_can_segmented = [False] * (len(s) + 1)
        is_can_segmented[0] = True
        for from_index in range(len(s)):
            if not is_can_segmented[from_index]:
                continue
            for word in wordDict:
                if s.startswith(word, from_index):
                    is_can_segmented[from_index + len(word)] = True
        return is_can_segmented[len(s)]
```

前から順に「たどり着けた位置」から「単語1個分先」へ伝播させる書き方。`dp[j]` を先にチェックしてから内側のループに入る点は、あなたの実装（`if dp[j] and ...`）と本質的に同じ発想。

> (nodchip, philip82148) 変数名は `is_can_segmented` より `is_segmentable`/`can_be_segmented` が自然（`is_/can_/has_` 接頭辞の推奨）。
> (philip82148) `from_index` より `start`/`start_index` が分かりやすい。
> (nodchip) `if x == True:` のような冗長な比較は避け、条件式のみで書く。

## 参考
- https://github.com/olsen-blue/Arai60/pull/39 (olsen-blue — 139. Word Break)
- https://github.com/fuga-98/arai60/pull/39 (fuga-98 — 139. Word Break)
- https://github.com/mamo3gr/arai60/pull/37 (mamo3gr — 139. Word Break)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/67 (Yoshiki-Iwasa — 139. Word Break)
- https://github.com/rimokem/arai60/pull/39 (rimokem — 139. Word Break)
