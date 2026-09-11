# 78. Subsets
https://leetcode.com/problems/subsets/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-14, 10分以内, ok)
### 考えたこと
- Permutationsとの違いに気づけず最初詰まった。Permutationsは「全部選び終わった葉」だけがresultに入るが、Subsetsは「再帰の途中の状態も含めて全部」がresultに入る、という点がポイント。
- そこに気づいてからは `result.append(path)` を毎回の呼び出しの先頭でやる、という構造にすぐ辿り着けた。
- for ループを `nums` 全体ではなく `remainings` にして `remainings[i+1:]` を次に渡すことで、`[1,2]` と `[2,1]` のような重複を防いだ（要素を選ぶ順番を前方向だけに固定する）。

## Step 2
### 整形して変えた点
- `remainings` → `candidates` にリネーム（「pathにまだ入ってない候補」という意味を明確に）。
- ロジックは変更なし。

## Step 3（3回連続の記録）
- 1回目: 2026-08-14, 10分以内, ok
- 2回目: 2026-08-14, 10分以内, ok
- 3回目: 2026-08-14, 10分以内, ok

3回連続クリア、mastered。反復（doubling）・ビット演算版は別途余裕があれば追記予定。

## 参考
- https://github.com/olsen-blue/Arai60/pull/52
- https://github.com/fuga-98/arai60/pull/50
- https://github.com/mamo3gr/arai60/pull/48
- https://github.com/Yoshiki-Iwasa/Arai60/pull/56
- https://github.com/rimokem/arai60/pull/51
