# leetcode-arai60

SWE協会（一般社団法人ソフトウェアエンジニアリング協会）推奨フローに従い、新井康平氏選定の LeetCode 69問（通称 arai60）を Python で反復練習するリポジトリ。

- 公式問題リスト: https://1kohei1.com/leetcode/
- LeetCode リスト: https://leetcode.com/list/?selectedList=xt2qzsi5
- 練習会: SWE協会 Discord

## PR 駆動レビューフロー

1問1ブランチ・1PR で進める。ブランチ名は `feat/<#>-<slug>`（例: `feat/206-reverse-linked-list`）。

1. 自力で解く（5〜10分詰まれば答えを見る）
2. LeetCode で AC → ブランチを切って `solutions/<slug>.py` に実装
3. PR を出して Discord `#leetcode_subaru2918` で一声かける
4. レビューコメントを反映して再 push
5. 3回連続10分以内クリアで master 判定（詳細は下記）

## 運用ルール

### 日次（毎日）

1. `/arai60` でその日のキューを表示（新規1問 + 復習1問）。
2. `/arai60 start <slug>` で計測開始 → 自力で解く。**5〜10分詰まったら答えを見る**（粘らない）。
3. LeetCode で AC → `/arai60 done <slug> <所要分> <ok|ng>`。1回目クリア時は自動で `/arai60 refs` が走り、他者コードが `solutions/<slug>.py` の references セクションに追記される。
4. references を読んで洗練された解法を理解する。
5. 次回復習日まで放置 → spaced repetition で自動的にキューに戻る。

### 週次（金曜）

`/arai60 review` で集計確認。詰まりカテゴリを翌週の重点に。

## マスター判定（SWE協会基準）

**10分以内にエラーなく実装** を **3回連続** クリア → `mastered`。

| status | 次回復習日 |
|---|---|
| `untouched` | 未着手 |
| `learning` (1回目クリア) | 翌日 |
| `reviewing` (2回連続) | 3日後 |
| `reviewing` (あと1回でmaster) | 7日後 |
| `mastered` | 30日後（劣化チェック） |
| 10分超過 or NG | カウントリセット、翌日に戻す |

## ディレクトリ

```
arai60/
├── README.md         # このファイル
├── tracker.md        # 全問題の進捗テーブル（single source of truth）
├── queue.md          # 今日のキュー（コマンドが生成）
├── log/YYYY-MM-DD.md # 日次ログ
└── solutions/<slug>.py # 実装 + references + notes
```

## solutions/*.py ファイル構造

```python
"""<問題名> — https://leetcode.com/problems/<slug>/"""

# === my attempts ===
# attempt 1 (YYYY-MM-DD, NN min, ok|ng)
def solve(): ...

# === references ===
# ref 1: LeetCode Editorial (...)
# ref 2: neetcode
# ref 3: Python標準ライブラリ活用

# === notes ===
# - 学んだこと
```

## コマンド一覧

| コマンド | 用途 |
|---|---|
| `/arai60` / `/arai60 today` | 今日のキュー表示・生成 |
| `/arai60 start <slug>` | 計測開始、solutions/<slug>.py テンプレ作成 |
| `/arai60 done <slug> <分> <ok\|ng>` | attempt 記録、status 更新、references 自動取得 |
| `/arai60 refs <slug>` | 他者コード取得（手動再実行用） |
| `/arai60 review` | 週次集計 |
