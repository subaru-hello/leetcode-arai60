# 6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。
- mastered 判定前に、目的・制約・解法を選んだ理由・計算量・別解とのトレードオフ・境界値を自分の言葉で説明する。

## この問題で得たい実務的な学び
- 状態（現在の行と方向）を持つ反復処理を実装し、読みやすさと空間効率のトレードオフを説明できるようにする。

## Step 1 (2026-08-31, AC)
### 考えたこと
- 現在の行と移動方向を持ち、文字を行ごとのリストへ振り分ける。

## Step 2
### 整形して変えた点
- `words_by_rows`、`curr_row` など、役割が伝わる名前にした。
- 文字の振り分けと、最後の結合を分けた。
- 時間計算量は O(n)、空間計算量は O(n)。周期計算版なら補助空間を減らせるが、計算式が複雑になるため、今回は読みやすい行リスト版を選んだ。

## Step 3（3回連続の記録）
- 1回目: 2026-09-20, 10分以内, AC
- 2回目: 2026-09-20, 5分, AC
- 3回目: 2026-09-20, 5分, AC

## 参考
- https://github.com/olsen-blue/Arai60/pull/61
- https://github.com/fuga-98/arai60/pull/57
- https://github.com/mamo3gr/arai60/pull/55
- https://github.com/Yoshiki-Iwasa/Arai60/pull/65
- https://github.com/t9a-dev/LeetCode_arai60/pull/60
