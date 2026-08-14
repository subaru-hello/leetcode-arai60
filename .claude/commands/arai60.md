arai60 ルーティンを実行してください。SWE協会公式フロー（自力で解く → 整形 → その場で3回連続10分で master → レビュー依頼）をそのまま踏襲します。

参照ディレクトリ: `~/Personal/leetcode-arai60/` (public リポ。subaru-hello/leetcode-arai60)
- `tracker.md` — 全69問の進捗テーブル（single source of truth、公開）
- `queue.md` — 今日のキュー（ローカルのみ、.gitignore 対象）
- `log/YYYY-MM-DD.md` — 日次ログ（ローカルのみ、.gitignore 対象）
- `problems/<#>-<slug>/` — 1問1フォルダ（公開、1問1PR）
  - `step1.py` — 初回AC時のコード
  - `step2.py` — 読みやすく整形したコード
  - `step3.py` — 「消して10分以内ノーエラーで書く」を3回連続クリアした最終コード
  - `memo.md` — 各ステップで感じたこと・考えたこと・参考リンク

参照ドキュメント: `~/Personal/octomblog-astro/src/content/docs/concepts_arai60_overview.md`

## 重要: 公式フロー（SWE協会の練習方法そのまま）

1. **Step 1（AC獲得）**: 答えを見ずに考える。**5分**考えて分からなければ参考を1つ開いて読む。理解したら閉じて、隠しながら書く。筆が止まって5分迷ったらまた開く。**一度見たら、書いた分を全部消してやり直す**。これを繰り返し、AC する。
2. **Step 2（整形）**: Step 1 で通ったコードを、読みやすく整形する。動くことを再確認。
3. **Step 3（体に叩き込む、その場で3回連続）**: 一旦コードを全部消す。LeetCodeのページを開き、時間を測りながらもう一度書く。ACできたらまた消して、もう一度書く。**10分以内・ノーエラーで書けるまで**これを繰り返す。**それが3回連続でできたら、その場で mastered**（日をまたいだ spaced repetition ではない）。
4. **レビュー依頼**: Step 3 まで終わったタイミングで PR を作成し、レビューを依頼する。

- `.py` ファイルにコードを書く。思考・感想は `memo.md` に集約。
- 1問1ブランチ: `feat/<#>-<slug>`
- 1問1PR、**merge しない**（open のままレビューコメント保存場所として使う）
- PRはStep 3（3回連続クリア）が終わった時点で作成する。

## サブコマンド判定

ユーザー引数: `$ARGUMENTS`

引数の1つ目で分岐:

- なし / `today` → **今日のキュー表示**
- `start <slug>` → **Step 1 計測開始**
- `retry <slug>` → **Step 3 の1回分試行（その場で3回連続を数える）**
- `done <slug> <分> <ok|ng>` → **試行完了（Step 1/2/3共通）**
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
   - フォルダ: problems/<#>-<slug>/
   - ブランチ: feat/<#>-<slug>
   - 目標: Step1でAC → Step2で整形 → Step3で10分以内ノーエラーを3回連続

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

## 2. `start <slug>` — Step 1 計測開始

1. `log/YYYY-MM-DD.md` を作成（なければ）して、`## <slug> — 開始: HH:MM` を追記。
2. **AC ベースライン記録**: `arai60_ac_count` で現在の AC 合計数を取得 → log に `<slug>:ac_before=<N>` を追記。LeetCode が応答しない場合は `ac_before=skip` と記録。
3. tracker.md から `<#>` (問題番号) と問題名・URL・カテゴリを取得。
4. `problems/<#>-<slug>/` フォルダが存在しなければ作成し、テンプレを作る:
   ```
   problems/<#>-<slug>/
   ├── step1.py
   ├── step2.py
   ├── step3.py
   └── memo.md
   ```
   `memo.md` のテンプレ:
   ```markdown
   # <#>. <問題名>
   <URL>

   ## ルール（公式フロー）
   - Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
   - Step 2: 読みやすく整形する。
   - Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

   ## Step 1 (YYYY-MM-DD, ?? min, ??)
   ### 考えたこと
   -

   ## Step 2
   ### 整形して変えた点
   -

   ## Step 3（3回連続の記録）
   - 1回目: YYYY-MM-DD, ?? min, ??
   - 2回目: YYYY-MM-DD, ?? min, ??
   - 3回目: YYYY-MM-DD, ?? min, ??

   ## 参考
   - (arai60 PRs を自動添付)
   ```
5. **ブランチ自動切り替え**: `git branch --show-current` で `feat/<#>-<slug>` 上にいなければ自動で切り替える:
   ```bash
   git checkout main && git checkout -b feat/<#>-<slug>
   ```
   - 既存ブランチが存在する場合は `git checkout feat/<#>-<slug>`。
   - 未コミット変更があると失敗するので、その場合のみユーザーに stash/commit を促す。
6. **参考 PR の自動添付**: `gh search repos "arai60" --limit 30` で arai60 系リポを列挙し、各リポの PR 一覧から `<#>` または `<問題名>` にマッチする PR を検索する。見つかった PR URL を `memo.md` の **`## 参考` セクション**に **5件** 追記する。
   - 5件に満たない場合は類題（同じパターンの代表問題）の PR で補い、その旨を明記する。
   - **arai60 community PR のみ** 貼る。LeetCode Editorial / neetcode の URL は貼らない。
7. ユーザーに伝える:
   > `problems/<#>-<slug>/memo.md` に考えたことを書きながら、`step1.py` にコードを書いてください。
   > LeetCode URL: <URL>
   > AC ベースライン: <N>問 (現時点)
   > **5分考えて分からなければ、参考を1つだけ開いてください。見たら書いた分を全部消してやり直します。**
   > 終わったら `/arai60 done <slug>` （引数なしで自動判定。失敗時は `/arai60 done <slug> <分> ok` で手動）

## 3. `done <slug> [<分>] [<ok|ng>]` — 試行完了

引数: `<分>` 省略時は log の `開始: HH:MM` から自動計算。`<ok|ng>` 省略時は LeetCode AC カウンタ差分で自動判定。

**現在どのStepかの判定**: `problems/<#>-<slug>/step1.py` が空 → Step1。`step1.py`に中身があり`step2.py`が空 → Step2。`step2.py`に中身があり`step3.py`が3回連続クリアしていない → Step3進行中。

1. **AC 自動判定**（Step1/Step3のみ、Step2は整形なのでAC判定不要）:
   - log から `<slug>:ac_before=<N>` を読む。
   - `arai60_ac_count` で現在の AC 数 `<M>` を取得。
   - `<M> > <N>` なら自動で `ok` 扱い。等しければ「AC 未検出」として処理を中断:
     > LeetCode に新規 AC が記録されていません。submit を確認してください。
     > 手動で確定する場合は `/arai60 done <slug> <分> ok` を実行。
   - `ac_before=skip` の場合は自動判定をスキップし、引数の `<ok|ng>` を使用（必須）。

2. **Step1完了時**: `step1.py` にコードを保存。`memo.md` の `## Step 1` に日付・分・ok/ngを記録。`ok`なら次はStep2に進むよう促す。`ng`ならStep1をやり直すよう促す（全部消してリトライ）。

3. **Step2完了時**: `step2.py` に整形版を保存。`memo.md` の `## Step 2` に変更点を記録。次はStep3（3回連続チャレンジ）に進むよう促す。

4. **Step3進行中（3回連続カウント）**:
   - `ok` かつ `分 <= 10` → `memo.md` の `## Step 3` に「N回目: 記録」を追記し、連続カウントを+1。
   - `ok` かつ `分 > 10` → 連続カウントを**0にリセット**（10分超は失敗扱い）。「10分超のためカウントリセット、もう一度」と伝える。
   - `ng` → 連続カウントを**0にリセット**。「全部消してもう一度」と伝える。
   - **連続カウントが3に到達したら mastered**。`step3.py` に最終コードを保存。

5. `tracker.md` の該当行を Edit で更新:
   - Step1/2進行中 → status=`in-progress`
   - Step3 mastered達成 → status=`mastered`、attempts列に`○○○`、最終解答日=今日、次回復習列は使わない（`-`のまま。spaced repetitionを廃止したため）。
   - Step3失敗（リセット） → status=`in-progress`のまま（日をまたいだ再挑戦ではなく、その場で仕切り直し）。

6. `log/YYYY-MM-DD.md` に `## <slug> — 完了: <分>min / <ok|ng> / Step<N> / 連続<X>回目` を追記。

7. **commit/push は提案も実行もしない（ユーザーが手動でやる）**。ファイル更新まで完了したら結果サマリだけ表示する。
   - **重要**: ブランチ切替時に未コミットファイルがあっても、勝手に `git commit && git push` してはいけない。必ずユーザーに選択肢（commit / stash / discard）を示して指示を待つ。
   - 運用方針: `tracker.md` は main 直 push、`problems/<#>-<slug>/` は `feat/<#>-<slug>` ブランチで PR（**merge しない、open のまま運用**）。
   - **mastered達成時（Step3の3回連続クリア時）に PR description テンプレ**を出力:
     ```
     今回解いた問題：<#>. <問題名>
     次に解く問題　：<次回新規の#>. <次回新規の問題名>
     言語：<lang>
     ```
     - 「次に解く問題」は `tracker.md` で当該行の次の `untouched` 行を見て決める。

8. ユーザーに結果サマリを表示（今どのStep・3回連続のうち何回目か）。mastered達成時は **PR description テンプレ**を出力してコピペできるようにする。

## 4. `refs <slug>` — 他者コード取得

1. tracker.md から該当問題の URL と問題名と `<#>` を取得。
2. WebFetch で以下3ソースを取得:
   - `https://leetcode.com/problems/<slug>/editorial/` — LeetCode 公式 Editorial
   - `https://github.com/neetcode-gh/leetcode` を検索（slug 名で grep してリポジトリ内の python ファイルを探す）
   - `https://docs.python.org/3/library/<関連library>.html` — collections / heapq / bisect など、問題に関連する標準ライブラリ
3. 各ソースから **解法コード + 計算量 + 1行コメント** を抽出して整形。
4. `problems/<#>-<slug>/memo.md` の `## references` セクション配下に追記:
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
5. ユーザーに「`memo.md` に3解法を追記しました」と伝える。

## 5. `review` — 週次集計

1. `tracker.md` の全行を集計:
   - 総問題数 / `mastered` / `in-progress` / `untouched` の内訳
   - カテゴリ別の master 率
2. `log/` ディレクトリの直近7日分のログを読み、attempts 数・平均所要時間を集計。
3. **詰まりカテゴリ**: 同じカテゴリでStep3リセットが多い問題TOP3を抽出。
4. 結果を表示:
   ```
   ## 週次サマリ (YYYY-MM-DD)
   - 進捗: 69問中 X mastered / Y in-progress / Z untouched
   - 今週の attempts: N回（目標14回）
   - 平均所要: X分
   - 詰まりカテゴリTOP3: ...
   - 来週の重点: <提案>
   ```

## 移行に関する注意

- 2026-08-13 に spaced repetition運用から公式フローに移行。既存の `solutions/<#>-<slug>.md`（旧形式）は**そのまま残す**（遡って`problems/`構造に変換しない）。新規問題からこの新フローを適用する。
- 既存 `tracker.md` の `learning`/`reviewing` status の問題は、次に着手する際に Step1 からではなく現在の理解度に応じて Step2/Step3 から再開してよい（ユーザー判断）。
