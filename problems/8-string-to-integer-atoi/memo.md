# 8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-30, 3min, ok)
### 考えたこと
- 完全に自力では方針が立たず、5つの具体例(`"42"`, `"   -42"`, `"4193 with words"`, `"words and 987"`, `"-91283472332"`)を1つずつ確認しながら5つのルール(空白読み飛ばし/符号/数字読み取り/数字なしは0/32bit範囲クランプ)を言語化した。
- 参考: olsen-blue/Arai60のPRを1つ読んだ。ループ中で毎回範囲チェックする実装だったが、Pythonは多倍長整数なので最後に1回だけチェックすれば十分と気づき簡略化。
- `sign = 0`で初期化してしまい、符号なしの数字(`"42"`)が`num *= sign`で常に`0`になるバグを踏んだ→`sign = 1`がデフォルトと気づいた。
- `MIN_INT = 2 ** 31`(符号が抜けて正の数になっていた)というバグで、負の数の結果が全部誤ってクランプされる不具合も踏んだ→`MIN_INT = -2 ** 31`に修正。
- `if`/`elif`の使い分け: 符号チェックを2つの独立した`if`にすると、1つ目が成立して`index`が進んだ後、2つ目の`if`が同じ`index`を再評価しに行き、`s="-"`のような入力で範囲外アクセス(IndexError)になることを実際にPythonで実行して確認した。`elif`にすることで、1つ目が成立したら2つ目を評価しないようにして解決。

## Step 2
### 整形して変えた点
- 関数分割(Extract Function)を検討したが、今回の5ルールは`index`という1つの状態を順番に更新していく流れなので、切り出すと「更新した`index`をタプルで毎回受け渡す」形になり、逆に読みにくくなる懸念があった。
- Rob Pike("Clear is better than clever")とMartin Fowler(Extract Functionは読みやすくなる時だけ使う、無理な分割は"Long Parameter List"の臭いに近づく)の原則に照らして、関数分割は見送り、空行+コメントで4ブロック(空白/符号/数字/クランプ)に区切る形にした。
- 別解として正規表現版も検討した:
```python
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^[ ]*([+-]?\d+)', s)
        if not match:
            return 0
        num = int(match.group(1))
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        return max(MIN_INT, min(MAX_INT, num))
```
`[ ]*`(空白0回以上)/`[+-]?`(符号0か1回)/`\d+`(数字1回以上)が手動実装の3ルールに対応する。正規表現の学習コストが高いと感じたため今回は見送り、概念のみ記録。

## Step 3（3回連続の記録）
- 1回目: YYYY-MM-DD, ?? min, ??
- 2回目: YYYY-MM-DD, ?? min, ??
- 3回目: YYYY-MM-DD, ?? min, ??

## 参考
- https://github.com/olsen-blue/Arai60/pull/60
- https://github.com/fuga-98/arai60/pull/56
- https://github.com/mamo3gr/arai60/pull/54
- https://github.com/Yoshiki-Iwasa/Arai60/pull/64
- https://github.com/t9a-dev/LeetCode_arai60/pull/59
