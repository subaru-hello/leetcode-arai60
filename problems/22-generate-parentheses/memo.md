# 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-16, 5min, ok)
### 考えたこと
- 最初「直前の文字」「置いた(の数の奇偶」で条件を作ろうとしたが、両方とも`"(())"`のトレースで崩れた。
- 最終的に「open_countとclose_countの2つのカウンター」を別々に持ち、`open_count < n`で`(`を置ける、`close_count < open_count`で`)`を置ける、という2つの独立したif（elifではない）で両方を試す形にたどり着いた。
- 自力でここまで持っていけず、fuga-98さんのPRのStep1解法(`used_open`/`opening_count`という名前だった)を1つ読んで、閉じてから自分の変数名(`open_count`/`close_count`)で書き直した。
- 最初 `traverse([], 0, 0)` と書いてしまい、`path`の型が`str`なのにlistを渡すミスがあった（`path + '('`でエラーになる）。型ヒントを見返して気づいた。

## Step 2
### 整形して変えた点
- Combination Sumで指摘された空間オーダーの話を踏まえ、`path`を`str`(`path + '('`で毎回コピー発生)から`list`(`append`/`pop`で書き換え)に変更。
- `path`を`nonlocal`で書き換える案を試したが、popによる「取り消し」がないと兄弟の枝を試すときに前の枝の文字が残ったまま壊れることに気づき、`append`→再帰→`pop`のbacktracking定番パターンに変更。
- base caseでは`''.join(path)`で文字列に戻してからresultに追加。
- `path`を`list`にした関係で `path = ''`（初期化ミス）→`path = []`に修正。

## Step 3（3回連続の記録）
- 1回目: 2026-08-16, 4分以内, ok
- 2回目: 2026-08-16, 4分以内, ok
- 3回目: 2026-08-16, 4分以内, ok

3回連続クリア、mastered。

## 参考
- https://github.com/olsen-blue/Arai60/pull/54
- https://github.com/fuga-98/arai60/pull/52
- https://github.com/mamo3gr/arai60/pull/50
- https://github.com/Yoshiki-Iwasa/Arai60/pull/58
- https://github.com/h-masder/Arai60/pull/56

## mastered後の別解探求

他4件のPRレビューで見つけた一番違う発想: `(A)B`分割法（olsen-blue, mamo3grが採用）。

`n`組の括弧は必ず`(`で始まり、対応する`)`との間の中身`A`と、それに続く`B`に分解できる。
`A`が`i`組、`B`が`n-1-i`組（外側の1組を引いた残りを分け合う）。

```python
def generate(k: int) -> List[str]:
    if k == 0:
        return ['']
    result = []
    for i in range(k):
        for A in generate(i):
            for B in generate(k - 1 - i):
                result.append('(' + A + ')' + B)
    return result
```

backtracking(1文字ずつ選ぶ)とは全く違う、分割統治のアプローチ。mamo3grさんは`@functools.cache`でこれをメモ化していた。
出力数はカタラン数 C_n ≈ 4^n/(n^1.5・√π) で抑えられる、という計算量の議論もあった。

コード化までは行わず、考え方の理解のみで一旦スキップ。
