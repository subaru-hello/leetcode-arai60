# 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

## ルール
- **Step 1**: 答えを見てもOK、まず正解させる
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## attempt 1 / Step 1 (2026-05-31, 110min, △)
- 準備として、開始する方のカッコを定数で持っておく。渡ってきたstringにどのカッコがあるのかを走査して、対応する閉じかっこが存在するかを判定していく。
- ひとまずこの方の[解法](https://github.com/katataku/leetcode/pull/6/changes/65829f8db9de8773ac999b71ae66c7b99cb2ffe2)を見て解いた

```python

class Solution(object):
    def isValid(self, s: string) -> bool:
        opening_parentheses = []
        for c in s:
            if c in '({[':
                opening_parentheses.append(c)
                continue
            if len(opening_parentheses) == 0:
                return False
            
            if c == ')' and opening_parentheses[-1] != '(':
                return False

            if c == '}' and opening_parentheses[-1] != '{':
                return False

            if c == ']' and opening_parentheses[-1] != '[':
                return False
            
            opening_parentheses.pop()
        return not opening_parentheses

```

## Step2
- 3つ目以降の３つのif文は、いずれもcの値が何かと開きかっこの値が何かを評価しているので共通化できそう
- )の時は(が来ることを期待するのであれば、dict形式で持っておくのがいいらしい
- 長さが0であるかどうかも、implicit falseを利用してで判定できるらしい (https://github.com/katataku/leetcode/pull/6/changes/65829f8db9de8773ac999b71ae66c7b99cb2ffe2#r1846116208)
- stackであることを変数名にしてみる。データ構造を変数名にするのはアリなのか？
- pop()で値の取り出しと除去の両方をできるらしい。(https://docs.python.org/ja/3/tutorial/datastructures.html)
> 指定された位置の要素をリストから取り除き、それを返します。



```python
    def isValid(self, s):
        parentheses_pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
          if c not in parentheses_pairs:
            stack.append(c)
            continue

          if not stack:
            return False

          if stack.pop() != parentheses_pairs[c]:
            return False
        return not stack
```

- sに6種のカッコしかこないから、c not in pairsとすることができているが、他の文字が来る場合はandを使ってkeyを厳密にチェックすることが必要
- pairsの値がへは開きカッコしか格納していないので、stackには開きカッコしか入らない


## 参考
- https://github.com/mamo3gr/arai60/pull/6
- https://github.com/olsen-blue/Arai60/pull/6
- https://github.com/chanseok-lim/arai60/pull/15
- https://github.com/Shunii85/arai60/pull/6
- https://github.com/rimokem/arai60/pull/6
