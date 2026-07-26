# 929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/

## ルール
- **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
- **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
- **Step 3**: レビュー反映 → 10分以内にエラーなく書く

## Step 1 (2026-06-11, 60min, △)

### 1-A: 自力で考えたこと
- データ構造案:
- アルゴリズム案:

### 1-B: 詰まった点
- 最初は下記のようなコードを書いた

まず、emailに@が含まれていない場合はスキップ
@を起点に、hostとdomainに分割する
hostから+と.を取り除く
hostとdomainを@で繋げてemailを作成し、set listに登録
setの長さを返却する


```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      separate_sign = "@"
      valid_emails = set()
      for email in emails:
        if separate_sign in email:
            continue
        host, domain = email.split(separate_sign)
        valid_host, _ = host.split("+")
        pure_host = vald_host.split(".")
        valid_emails.add(purehost + "@" + domain)
      
      return len(valid_emails)
```
- いくつか間違いがあった
if separate_sign in email: continue → 条件が逆。@がある場合に処理したいのに、スキップしてしまっていた
host.split("+") → +がない場合にエラー。split("+", 1) で最初の1回だけ分割すべき
vald_host → typo
split(".") → .を除去するには replace(".", "") を使う

```python

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()
        for email in emails:
            if "@" not in email:
                continue
            host, domain = email.split("@")
            host = host.split("+", 1)[0]
            host = host.replace(".", "")
            valid_emails.add(host + "@" + domain)
        return len(valid_emails)
```

## 参考
- https://github.com/mamo3gr/arai60/pull/14
- https://github.com/olsen-blue/Arai60/pull/14
- https://github.com/chanseok-lim/arai60/pull/6
- https://github.com/Yoshiki-Iwasa/Arai60/pull/13
- https://github.com/h-masder/Arai60/pull/15
