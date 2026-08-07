# 779. K-th Symbol in Grammar
https://leetcode.com/problems/k-th-symbol-in-grammar/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-08-07, 5min, ok)

### 考えたこと
- n行目のk番目は、n-1行目の (k+1)//2 番目（親）から生まれる
- 0→"01", 1→"10" の展開ルールより、奇数番目は親と同じ値、偶数番目は親の反転値
- 親の値を再帰で取得してから、奇数/偶数で分岐して返す

### 実装
```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent_value = self.kthGrammar(n - 1, (k + 1) // 2)

        if k % 2 == 0:
            return 1 - parent_value
        else:
            return parent_value
```

## Step 2 (2026-08-07)

### 考えたこと
- Step 1 の再帰版をベースに確定。ビットカウントのワンライナー解（`bin(k-1).count("1") % 2`、refs参照）も検討したが、面接で「なぜそうなるか」を言語化しやすい再帰版を採用
- if/else を三項演算子に圧縮する案も検討したが、奇数/偶数の分岐が読み取りにくくなるため見送り

### 実装
```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        parent_value = self.kthGrammar(n - 1, (k + 1) // 2)

        if k % 2 == 0:
            return 1 - parent_value
        else:
            return parent_value
```

## 参考
- https://github.com/olsen-blue/Arai60/pull/47
- https://github.com/fuga-98/arai60/pull/46
- https://github.com/mamo3gr/arai60/pull/44
- https://github.com/Yoshiki-Iwasa/Arai60/pull/39
- https://github.com/rimokem/arai60/pull/46
