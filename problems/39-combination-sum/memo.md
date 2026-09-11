# 39. Combination Sum
https://leetcode.com/problems/combination-sum/

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-14, 5min, ok)
### 考えたこと
- Subsetsの延長線として「target - candidateを繰り返して0になったら答え」という発想は最初から持てた。
- Subsetsで使った `candidates[i+1:]` をそのまま使うと今見てる値自体が除外されてしまい、「同じ値を何回でも使える」という今回のルールに反することに気づいた。
- 代わりに `candidates[i:]`（自分自身は残すが前には戻らない）にすることで、reuse可能かつ重複順列を防げた。
- `remaining < 0` になったら打ち切り（枝刈り）が必要、という点も自分で気づけた。
- backtrackの引数がSubsetsの2つ(path, candidates)から3つ(path, remaining, candidates)に増える理由も理解できた（targetまでの残りを追跡する必要があるため）。

## Step 2
### 整形して変えた点
- 関数名 `backtrack` → `find_combinations`（アルゴリズム名ではなく問題固有の意味に）。
- `remainings`(int) → `remaining_target`（何の残りかを明示、単数形に）。
- 内側の `candidates`（外側の引数とシャドーイングしてた）→ `remaining_candidates` にリネーム。
- ガード節の順番を `remaining_target < 0` → `remaining_target == 0` に統一（無効ケースを先に弾く）。
- リネーム中に一度バグ発生: for ループの中の再帰呼び出しで `remaining_candidates[i]` にすべきところを外側の `candidates[i]` のまま使ってしまい、重複した組み合わせ（例: `[2,2,3]`と`[3,2,2]`)が出る不具合があった。トレースして気づき修正。
- `result` はクロージャで直接書き換える方式のまま維持（backtrackingでは標準的なパターンと確認）。

## Step 3（3回連続の記録）
- 1回目: 2026-08-15, 2min, ok
- 2回目: 2026-08-16, 3min, ok
- 3回目: 2026-08-16, 3min, ok

3回連続クリア、mastered。

## 参考
- https://github.com/olsen-blue/Arai60/pull/53
- https://github.com/fuga-98/arai60/pull/51
- https://github.com/mamo3gr/arai60/pull/49
- https://github.com/Yoshiki-Iwasa/Arai60/pull/57
- https://github.com/h-masder/Arai60/pull/55
