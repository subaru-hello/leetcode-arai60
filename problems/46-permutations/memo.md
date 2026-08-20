# 46. Permutations
https://leetcode.com/problems/permutations/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-14, 2min, ok)
### 考えたこと
- バックトラッキング: current(組み立て中の順列) と remaining_nums(まだ使っていない数字) の2つを状態として持つ
- remaining_numsが空になったら、currentが完成した順列 → resultに追加
- forループで「次にどの数字を選ぶか」を全通り試す。選んだらcurrentに追加、remaining_numsから除いて再帰
- remaining_nums[:i] + remaining_nums[i+1:] で i番目を除いたリストを作る（半開区間の考え方、:iはi含まない、i+1:はiを含まない）
- 5分で行き詰まり、参考(バックトラッキングの標準形)を1つ見た。閉じて全部消してから再実装した

## Step 2
### 整形して変えた点
- current/remaining_nums → path/remaining にリネーム。「current(今の状態)」より「path(決定木を辿ってきた経路)」の方がバックトラッキングの発想を表す標準的な命名
- backtrack()呼び出しの引数をそのまま渡す形はシンプルなので維持（next_current等の中間変数は導入せず）

## Step 3（3回連続の記録）
- 1回目: 2026-08-14, 10分以内, ok
- 2回目: 2026-08-14, 10分以内, ok
- 3回目: 2026-08-14, 10分以内, ok
- 3回連続クリア、mastered

## 参考
- https://github.com/olsen-blue/Arai60/pull/51 (olsen-blue — 46. Permutations)
- https://github.com/fuga-98/arai60/pull/49 (fuga-98 — 46. Permutations)
- https://github.com/mamo3gr/arai60/pull/47 (mamo3gr — 46. Permutations)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/55 (Yoshiki-Iwasa — 46. Permutations)
- https://github.com/rimokem/arai60/pull/50 (rimokem — 46. Permutations)
