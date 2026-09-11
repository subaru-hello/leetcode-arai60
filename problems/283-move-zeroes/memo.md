# 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-18, 2min, ok)
### 考えたこと
- 最初、再帰(helper関数)で解こうとしたが、この問題はループ1回で完結すると気づいて方針転換。
- 「0を数えて末尾に足す」という発想自体は最初からあったが、実装でいくつかつまずいた:
  - `num == "0"`(文字列)と`int`の型不一致。
  - `nums[idx] == ""`で`==`(比較)と`=`(代入)を間違えていた。
  - `nums.concat()`のような存在しないメソッドを使おうとした。
  - `for _ in zero_count:` — `int`はiterableではないので`range(zero_count)`が必要と学んだ。
  - `return non_zero`だけでは呼び出し元の`nums`は書き換わらない、`nums[:] = non_zero`(スライス代入で中身を丸ごと入れ替える)が必要、という点を理解した。
- 最終的に「0以外を集めたリストを作る→0をzero_count個足す→`nums[:]`で書き戻す」という形でAC。

## Step 2
### 整形して変えた点
- Step1は「0以外を集めた新しいリストを作る」のでO(n)の追加メモリを使っていて「ハック的」に感じた。
- 二分ポインタ(`i`, `insert_pos`)によるin-place swap方式に変更してO(1)space化。
- `insert_pos`は「次に0じゃない値を置くべき場所」で、0に出会うたびに`i`との差が開いていく（0がどんどん後ろに追いやられるイメージ）、という点をトレースで理解した。
- swap相手の`insert_pos`は`i`の隣とは限らない(0を何個スキップしたかで離れる)、という点も具体例で確認した。

## Step 3（3回連続の記録）
- 1回目: 2026-08-20, 1min, ok
- 2回目: 2026-08-20, 1min, ok
- 3回目: 2026-08-20, 1min, ok

3回連続クリア、mastered。

## 参考
- https://github.com/olsen-blue/Arai60/pull/55
- https://github.com/fuga-98/arai60/pull/53
- https://github.com/mamo3gr/arai60/pull/51
- https://github.com/kunimomo/arai60/pull/6
- https://github.com/Yoshiki-Iwasa/Arai60/pull/59
