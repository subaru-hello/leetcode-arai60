# 252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-20, 20min, ok)
### 考えたこと
- Premium問題でLeetCode上のAC確認ができないため、2つの与えられた例で手動検証してok判定とした。
- 「開始時刻でソートして、直前の終了時刻と比較する」という発想は自力で出せたが、`start < last_meeting_end`にする際に「1つ前の会議のendを覚えておく変数」が必要、という点で最初つまずいた(`for start,end in sorted_intervals`の中の`start`/`end`が同じ会議のものだと気づくのに時間がかかった)。
- 参考: olsen-blue/Arai60のPRを1つ読んだ。累積和(+1/-1を置いて最大重複数を見る)というもう1つのアプローチも知れて面白かった。
- 境界(直前の終了時刻と今の開始時刻が同じ)は「重なってない」扱い、という点も先に確認してから実装した。

## Step 2
### 整形して変えた点
- 累積和方式と比較検討したが、この問題の制約(`n<=10^4`, 時刻の範囲`10^6`)では累積和は空間`O(10^6)`で今のソート方式`O(n log n)`より不利、かつ時刻が整数前提という弱点もあるため、ソート方式を維持。
- `last_meeting_end` → `last_meeting_ended_at`、`start` → `begin` にリネームして可読性を上げた。

## Step 3（3回連続の記録）
- 1回目: 2026-08-20, 1min, ok
- 2回目: 2026-08-20, 1min, ok
- 3回目: 2026-08-20, 1min, ok

3回連続クリア、mastered。

## 参考
- https://github.com/olsen-blue/Arai60/pull/56
- https://github.com/mamo3gr/arai60/pull/59
- https://github.com/Yoshiki-Iwasa/Arai60/pull/60
- https://github.com/t9a-dev/LeetCode_arai60/pull/55
- https://github.com/Manato110/LeetCode-arai60/pull/56

## 補足
LeetCode Premium限定問題のため、LeetCode上でのAC確認はできず。手動テストケース検証で進行。
