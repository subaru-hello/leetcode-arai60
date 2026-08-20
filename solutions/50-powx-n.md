# 50. Pow(x, n)
https://leetcode.com/problems/powx-n/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-08-01, 6min, ok)

### 考えたこと
- x^n を n 回掛け算するのではなく、n を半分にしながら二乗する「二分累乗法 (exponentiation by squaring)」で O(log n) にする。CLRS 31.6節の MODULAR-EXPONENTIATION と同じ考え方。
- n が偶数: x^n = x^(n//2) * x^(n//2)（指数法則 x^a * x^b = x^(a+b) を a=b=n//2 で適用）
- n が奇数: x^n = x * x^(n-1)（同じ法則を a=1, b=n-1 で適用）
- n が負: x^n = 1 / x^(-n) に帰着させ、既に解けている非負ケースの再帰を再利用する（Pólya の「解けている問題に帰着させる」）
- 最初は `n / 2`（float）や `1/n`（逆数と符号反転の混同）でつまずいた。`n // 2` で整数除算、`-n` で符号反転、`1 / self.myPow(x, -n)` で逆数を取る、の3つを区別できていなかった。

### 実装
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return x * self.myPow(x, n - 1)
```

## Step 2 (2026-08-02)

### 自分なりに整形
- `n % 2 == 0` を `is_even` という真偽値変数に切り出した。参考PR (hayashi-ay/leetcode#41) で nodchip から「`n % 2` の 0/1 と偶数/奇数の対応が直感的か疑問」と指摘されていたのと同じ論点。
- 一方 `n < 0` も同様に `is_negative` に切り出してみたが、こちらは効果が薄いと判断して差し戻した。`n < 0` はそのままで十分読める。**指摘されていた具体的な問題（0/1 と偶奇の対応）を持つ箇所だけ直す**方が、機械的に全部を変数化するより意図が伝わる。

### 他人のコードを読んでの気づき
- hayashi-ay/leetcode#41 の実際のレビューコメントを読んだ（詳細は下記 hayashi-ay 参照欄）。要点は「変数名は一発で決まらない、レビューの往復で収束する」こと。`digits`/`res` → `cumulated`/`powered` と直したら意味が逆になっていた、というエピソードが印象的だった。
- 再帰 vs ループの選択は「個人差がある」という nodchip のコメントに納得。今回は再帰のままで進める（Step 1 から書き慣れているため）。

### 再整形後の実装
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        is_even = n % 2 == 0
        if is_even:
            half_powered = self.myPow(x, n // 2)
            return half_powered * half_powered
        else:
            return x * self.myPow(x, n - 1)
```

## 参考

### olsen-blue/Arai60 #45
https://github.com/olsen-blue/Arai60/pull/45

再帰＋ビット演算のパターンも解説。累乗を2進数分解して考える視点（x^13 = x^8 * x^4 * x^1 のような分解）が step2 の while ループ解法（下記 rimokem PR）と地続き。

### fuga-98/arai60 #45
https://github.com/fuga-98/arai60/pull/45

step1 は素直に for ループ実装 → x=0.00001, n=2147483647 で TLE。log を取って `pow(2, log2(x) * n)` で戻す案を試すが精度・符号の扱いが煩雑になり断念、という失敗ログが参考になる（浮動小数の log/pow 変換は誤差が乗りやすい）。

### mamo3gr/arai60 #43
https://github.com/mamo3gr/arai60/pull/43

- 計算量見積もりが詳細: 素朴な O(n) だと n=2^31 で ~214秒（TLE確定）、分解＋再帰の O(log n) なら log2(2^31)=31 ステップ、3マイクロ秒オーダー。再帰フレームのメモリも 150 bytes * 31 ≒ 4.6KB と見積もっている。
- n が負のとき、毎回 `1/x` するのではなく **先に x^|n| を計算してから最後に一度だけ逆数を取る**方が良いと指摘（浮動小数点の除算を繰り返さないことで誤差と計算コストを抑える）。今回自分が書いた `1 / self.myPow(x, -n)` はこの方針と一致している。
- リンク先の hayashi-ay/leetcode #41 で「left-to-right binary exponentiation」（nを2進数表記し上位ビットから2乗＋条件付き乗算）も紹介されている。Python 組み込み `pow()` はこの方式らしい。

### Yoshiki-Iwasa/Arai60 #38
https://github.com/Yoshiki-Iwasa/Arai60/pull/38

- 言語は Rust。`n.unsigned_abs()` で符号なしに変換してから再帰、最後に正負で `powered` か `1.0/powered` を返す構成 — 「符号を先に外して非負ケースに帰着させる」考え方は自分の実装と同じ。
- 再帰内は `pow(x*x, n/2)`（偶数）/ `pow(x*x, n/2) * x`（奇数）で、x 側を2乗しながら n を毎回半分にする書き方（自分は x はそのまま、half の結果を2乗する書き方 — 両者は同値だが x を先に2乗するほうが末尾再帰的でループ変換しやすい）。

### rimokem/arai60 #45
https://github.com/rimokem/arai60/pull/45

- step1: `x^(2n)=(x^2)^n`, `x^(2n+1)=x*(x^2)^n` という式変形で再帰。自分の「half*half」と同値だが、x側を先に2乗する形（Yoshiki-Iwasa と同じ発想）。
- step2: ビット演算での反復版を提示。n の2進数表現を最下位ビットから走査し、ビットが1なら `result *= base` を行い、毎回 `base *= base`、`remaining >>= 1` で進める。再帰を使わず O(log n) を実現する定番パターンとして押さえておきたい。
  ```python
  class Solution:
      def myPow(self, x: float, n: int) -> float:
          if n < 0:
              x = 1 / x
              n = -n

          result = 1.0
          base = x
          remaining = n
          while remaining > 0:
              if remaining & 1:
                  result *= base
              base *= base
              remaining >>= 1

          return result
  ```
