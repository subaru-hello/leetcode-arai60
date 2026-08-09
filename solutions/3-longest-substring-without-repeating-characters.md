# 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-08-09, 4min, ok)

### 考えたこと
- Sliding Window: left/right の2ポインタで「重複のない連続区間」を管理
- seen[char] = 最後に登場した位置(インデックス)を記録
- 重複が見つかったら、left を「重複した文字の次の位置」まで一気に進める（1歩ずつではない）
- seen[c] >= left のチェックが必要（過去の記録が今のwindowの外なら無視していい）
- longest は毎回 max(longest, right - left + 1) で更新（常に伸ばすのではなく、windowの長さと比較）

### 実装
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        longest = 0

        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            longest = max(longest, right - left + 1)
        return longest
```

## references

### ref1: olsen-blue — max()でleft更新をシンプルに
https://github.com/olsen-blue/Arai60/pull/49

```python
left = 0
for right in range(len(s)):
    if s[right] in seen_char_to_index:
        left = max(left, seen_char_to_index[s[right]] + 1)
    seen_char_to_index[s[right]] = right
```

`if seen[c] >= left` の条件分岐の代わりに `max(left, ...)` を使うと、「過去の記録が今のwindowより前なら無視される」を自然に表現できる（`left`は減ることがないため）。

> (oda) Sliding Window と尺取り法は同じもの。`dict.get(s[right], -1)` を使えば `in` チェックを回避できる。
> (olsen-blue) ウィンドウ内部を常にvalid状態に保つ設計がクリーン。

### ref2: mamo3gr — 変数名の議論（char_to_last_index）
https://github.com/mamo3gr/arai60/pull/45

> (nodchip) `char_to_index` より `char_to_last_index` の方が「最後に登場した位置」という意図が明確。
> (garunitule) `max_length` だけ保持する形の方がメモリ効率的（dp配列全体を持たなくていい、今回の実装と同じ発想）。

## 参考
- https://github.com/olsen-blue/Arai60/pull/49 (olsen-blue — 3. Longest Substring Without Repeating Characters)
- https://github.com/fuga-98/arai60/pull/47 (fuga-98 — 3. Longest Substring Without Repeating Characters)
- https://github.com/mamo3gr/arai60/pull/45 (mamo3gr — 3. Longest Substring Without Repeating Characters)
- https://github.com/Yoshiki-Iwasa/Arai60/pull/42 (Yoshiki-Iwasa — 3. Longest Substring Without Repeating Characters)
- https://github.com/rimokem/arai60/pull/48 (rimokem — 3. Longest Substring Without Repeating Characters)
