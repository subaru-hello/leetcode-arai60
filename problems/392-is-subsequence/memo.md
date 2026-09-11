# 392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-23, 2min, ok)
### 考えたこと
- 「sを1文字ずつ、tは前回の続きから探す」という2ポインタの発想は自力で出せた。
- `while`条件で`<=`と`<`、`and`と`or`を間違えて、境界のトレースで気づいて修正した(`i==len(s)`の時点で`s[i]`は存在しない添字、両方とも終わってない間だけ継続する必要がある、という2点)。
- 実用例: VSCode/Sublimeのファジー検索(`"gtf"`が`"getText Function"`にマッチする仕組み)、DNA配列のパターン検索、LCS(diffツールの基礎)につながる、という話を聞いて面白かった。
- LeetCode公式のフォローアップ(大量のsをtに対して判定する場合の最適化)も知った。

## Step 2
### 整形して変えた点
- `while i<len(s) and j<len(t)`の2ポインタ手動管理から、`for char in t`でtを自動的になぞる形に変更。`j`という変数が丸ごと不要になった。
- 残った`i`を`s_index`にリネーム(「sのどこまで見たか」を明示)。
- 関数分割はロジックが短い(6行程度)ので見送り。

## Step 3（3回連続の記録）
- 1回目: 2026-08-24, 1min, ok
- 2回目: 2026-08-24, 1min, ok
- 3回目: 2026-08-24, 1min, ok

3回連続クリア、mastered。

## 参考
- https://github.com/olsen-blue/Arai60/pull/58
- https://github.com/fuga-98/arai60/pull/54
- https://github.com/mamo3gr/arai60/pull/52
- https://github.com/Manato110/LeetCode-arai60/pull/58
- https://github.com/t9a-dev/LeetCode_arai60/pull/57
