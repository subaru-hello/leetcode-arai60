arai60 ルーティンを実行してください。SWE協会推奨フロー（自力で解く → 他者コードを学ぶ → 3回連続10分で master）を spaced repetition で仕組み化します。

参照ディレクトリ: `~/Personal/leetcode-arai60/` (public リポ。subaru-hello/leetcode-arai60)
- `tracker.md` — 全69問の進捗テーブル（single source of truth、公開）
- `queue.md` — 今日のキュー（ローカルのみ、.gitignore 対象）
- `log/YYYY-MM-DD.md` — 日次ログ（ローカルのみ、.gitignore 対象）
- `solutions/<#>-<slug>.md` — 実装 + 思考 + references + notes（公開、1問1PR、`.md` で書く）

参照ドキュメント: `~/Personal/octomblog-astro/src/content/docs/concepts_arai60_overview.md`

## 重要: レビュー駆動フロー（hayashi-ay 流）

- `.py` ではなく **`.md`** にコード(```python ブロック)と思考を混ぜて書く
- 1問1ブランチ: `feat/<#>-<slug>`
- 1問1PR、**merge しない**（open のままレビューコメント保存場所として使う）
- attempt ごとに commit して push、レビューが付くと次の attempt に反映

## サブコマンド判定

ユーザー引数: `$ARGUMENTS`

引数の1つ目で分岐:

- なし / `today` → **今日のキュー表示**
- `start <slug>` → **計測開始**
- `done <slug> <分> <ok|ng>` → **attempt 完了**
- `refs <slug>` → **他者コード取得**
- `review` → **週次集計**

## 1. `today` — 今日のキュー表示

1. `tracker.md` を読む。
2. **新規問題を選定**: status が `untouched` の中から、`tracker.md` の上から順に1問。
3. `queue.md` を書き換える:
   ```markdown
   # 今日のキュー (YYYY-MM-DD)

   ## 新規: [#<番号>] <問題名>
   - slug: <slug>
   - URL: <url>
   - カテゴリ: <category>
   - ファイル: solutions/<#>-<slug>.md
   - ブランチ: feat/<#>-<slug>
   - 目標: 10分以内、ノーエラー

   ## 手順
   1. `/arai60 start <新規slug>` で計測開始
   2. 解いたら `/arai60 done <新規slug>`
   ```
   - 復習は出さない（毎日 untouched から上から順に1問だけ）。
5. ユーザーに queue.md の内容を表示。
6. **新規問題のブランチに自動切り替え**: `today` で選定した新規問題用に `feat/<#>-<slug>` ブランチを作成・切り替える。未コミット変更があれば stash を促す。
   ```bash
   git checkout main && git checkout -b feat/<#>-<slug>
   ```

## 共通設定

- LeetCode username: `subaru-hello-hello` (環境変数 `LEETCODE_USER` で上書き可)
- AC カウンタ取得用 GraphQL ヘルパ:
  ```bash
  arai60_ac_count() {
    local user="${LEETCODE_USER:-subaru-hello-hello}"
    curl -s 'https://leetcode.com/graphql' \
      -H 'Content-Type: application/json' -H 'Referer: https://leetcode.com' \
      --data-raw "{\"query\":\"query(\$u:String!){matchedUser(username:\$u){submitStats{acSubmissionNum{difficulty count}}}}\",\"variables\":{\"u\":\"$user\"}}" \
      | jq -r '.data.matchedUser.submitStats.acSubmissionNum[] | select(.difficulty=="All") | .count'
  }
  ```

## 2. `start <slug>` — 計測開始

1. `log/YYYY-MM-DD.md` を作成（なければ）して、`## <slug> — 開始: HH:MM` を追記。
2. **AC ベースライン記録**: `arai60_ac_count` で現在の AC 合計数を取得 → log に `<slug>:ac_before=<N>` を追記。LeetCode が応答しない場合は `ac_before=skip` と記録（後段の自動判定を諦める）。
2. tracker.md から `<#>` (問題番号) と問題名・URL・カテゴリを取得。
3. `solutions/<#>-<slug>.md` が存在しなければ、テンプレを作る（**3セクション構造: ルール / attempt / 参考**）:
   ```markdown
   # <#>. <問題名>
   <URL>

   ## ルール
   - **Step 1**: まず自力で15分。詰まったら参考を1つだけ開いて読む → 閉じて要約 → 自分で実装 → AC
   - **Step 2**: 自分なりに整形 → 他人のコードを読んで再整形 → PR でレビュー依頼
   - **Step 3**: レビュー反映 → 10分以内にエラーなく書く

   ## Step 1 (YYYY-MM-DD, ?? min, ??)

   ```python

   ```

   ## 参考
   - (arai60 PRs を自動添付)
   ```
   - **attempt 表記は使わない**。`## Step 1`, `## Step 2`, `## Step 3` のみ。
   - PR description には別途 `今回解いた問題 / 次に解く問題 / 言語` + 学習方法 Step 1/2/3 を入れる。
4. **ブランチ自動切り替え**: `git branch --show-current` で `feat/<#>-<slug>` 上にいなければ自動で切り替える:
   ```bash
   git checkout main && git checkout -b feat/<#>-<slug>
   ```
   - 既存ブランチが存在する場合は `git checkout feat/<#>-<slug>`。
   - 未コミット変更があると失敗するので、その場合のみユーザーに stash/commit を促す。
4.5. **参考 PR の自動添付**: `gh search repos "arai60" --limit 30` で arai60 系リポを列挙し、各リポの PR 一覧から `<#>` または `<問題名>` にマッチする PR を検索する。見つかった PR URL を `solutions/<#>-<slug>.md` の **`## 参考` セクション**に **5件** 追記する。
   - 検索クエリ例: `gh pr list --repo <owner>/<repo> --json title,url --limit 200 | jq '.[] | select(.title | test("<#>[_. ]|<問題名>";"i"))'`
   - 5件に満たない場合は類題（同じパターンの代表問題）の PR で補い、その旨を明記する。
   - **arai60 community PR のみ** 貼る。LeetCode Editorial / neetcode の URL は貼らない。
5. ユーザーに伝える:
   > `solutions/<#>-<slug>.md` に attempt 1 を書いてください。
   > LeetCode URL: <URL>
   > AC ベースライン: <N>問 (現時点)
   > 終わったら `/arai60 done <slug>` （引数なしで自動判定。失敗時は `/arai60 done <slug> <分> ok` で手動）

## 3. `done <slug> [<分>] [<ok|ng>]` — attempt 完了

引数: `<分>` 省略時は log の `開始: HH:MM` から自動計算。`<ok|ng>` 省略時は LeetCode AC カウンタ差分で自動判定。

1. **AC 自動判定**:
   - log から `<slug>:ac_before=<N>` を読む。
   - `arai60_ac_count` で現在の AC 数 `<M>` を取得。
   - `<M> > <N>` なら自動で `ok` 扱い。等しければ「AC 未検出」として処理を中断:
     > LeetCode に新規 AC が記録されていません。submit を確認してください。
     > 手動で確定する場合は `/arai60 done <slug> <分> ok` を実行。
   - `ac_before=skip` の場合は自動判定をスキップし、引数の `<ok|ng>` を使用（必須）。
2. `tracker.md` の該当行を読む。現在の attempts 列を取得。
3. **status 判定**:
   - `ok` かつ `分 <= 10` → attempts に `○` 追加
   - `ok` かつ `分 > 10` → `△` 追加（クリアしたが時間オーバー、カウントは進めない）
   - `ng` → `×` 追加、attempts をリセット (`---`)
3. **status と次回復習日を計算**（今日を基準）:
   - attempts が `○--` → `learning` / 翌日
   - `○○-` → `reviewing` / 3日後
   - `○○○` → `mastered` / 30日後（masterおめでとう表示）
   - `△` や `×` 含む → `learning` のまま / 翌日
4. `tracker.md` の該当行を Edit で更新（attempts / 最終解答日 / 最終(分) / 次回復習 / status）。
5. `solutions/<#>-<slug>.md` の **Step ヘッダ**を更新する。例: `## Step 1 (YYYY-MM-DD, ?? min, ??)` → `## Step 1 (今日, <分>min, <ok|ng>)`。
   - Step 1 が既に完了済み（タイム入り）なら、新しい `## Step N` セクションを末尾に追記（テンプレ部分付き）。
   - attempt N の表記は使わない。Step 1 / Step 2 / Step 3 のみ。
6. `log/YYYY-MM-DD.md` に `## <slug> — 完了: <分>min / <ok|ng> / status=<新status>` を追記。
7. **1回目クリア時（attempts が `○--` になった瞬間）は自動で `refs <slug>` を呼ぶ**。
8. **commit/push は提案も実行もしない（ユーザーが手動でやる）**。ファイル更新まで完了したら結果サマリだけ表示する。
   - **重要**: ブランチ切替時に未コミットファイルがあっても、勝手に `git commit && git push` してはいけない。必ずユーザーに選択肢（commit / stash / discard）を示して指示を待つ。
   - 運用方針: `tracker.md` は main 直 push、`solutions/<#>-<slug>.md` は `feat/<#>-<slug>` ブランチで PR（**merge しない、open のまま運用**）。
   - 1回目クリア後の **PR description テンプレ**（ユーザーが `gh pr create` するときに使う形式）:
     ```
     今回解いた問題：<#>. <問題名>
     次に解く問題　：<次回新規の#>. <次回新規の問題名>
     言語：<lang>
     ```
     - 「次に解く問題」は `tracker.md` で当該行の次の `untouched` 行を見て決める。
     - 「言語」は solutions の Python ブロックから推定。明示されている場合はそれを使う。
9. ユーザーに結果サマリを表示（status・次回復習日・master まで残り何回か）。続けて **PR description テンプレ**（上記）を出力して、ユーザーがコピペできるようにする。

## 4. `refs <slug>` — 他者コード取得

1. tracker.md から該当問題の URL と問題名と `<#>` を取得。
2. WebFetch で以下3ソースを取得:
   - `https://leetcode.com/problems/<slug>/editorial/` — LeetCode 公式 Editorial
   - `https://github.com/neetcode-gh/leetcode` を検索（slug 名で grep してリポジトリ内の python ファイルを探す）
   - `https://docs.python.org/3/library/<関連library>.html` — collections / heapq / bisect など、問題に関連する標準ライブラリ
3. 各ソースから **解法コード + 計算量 + 1行コメント** を抽出して整形。
4. `solutions/<#>-<slug>.md` の `## references` セクション配下に追記:
   ```markdown
   ## references

   ### ref1: LeetCode Editorial — <approach name>
   Time O(?) Space O(?)
   <URL>

   \`\`\`python
   def solve_editorial(...):
       ...
   \`\`\`

   ### ref2: neetcode — <approach name>
   <URL>

   \`\`\`python
   ...
   \`\`\`

   ### ref3: Python標準ライブラリ活用 (<library名>)
   <docs URL>

   \`\`\`python
   ...
   \`\`\`
   ```
5. ユーザーに「`solutions/<#>-<slug>.md` に3解法を追記しました」と伝える。

## 5. `review` — 週次集計

1. `tracker.md` の全行を集計:
   - 総問題数 / `mastered` / `reviewing` / `learning` / `untouched` の内訳
   - カテゴリ別の master 率
2. `log/` ディレクトリの直近7日分のログを読み、attempts 数・平均所要時間を集計。
3. **詰まりカテゴリ**: 同じカテゴリで `×` や `△` が多い問題TOP3を抽出。
4. 結果を表示:
   ```
   ## 週次サマリ (YYYY-MM-DD)
   - 進捗: 69問中 X mastered / Y reviewing / Z learning / W untouched
   - 今週の attempts: N回（目標14回）
   - 平均所要: X分
   - 詰まりカテゴリTOP3: ...
   - 来週の重点: <提案>
   ```
