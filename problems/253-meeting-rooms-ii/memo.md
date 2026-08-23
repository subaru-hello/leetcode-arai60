# 253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Premium限定問題のため、LeetCode上のAC確認は不可。手動テストケース検証で進行。

## ルール（公式フロー）
- Step 1: 5分考えて分からなければ参考を1つ開く。見たら全部消してやり直す。AC する。
- Step 2: 読みやすく整形する。
- Step 3: 全部消してもう一度書く。10分以内・ノーエラーで書けるまで繰り返す。3回連続できたら mastered。

## Step 1 (2026-08-21, 10min, ok)
### 考えたこと
- Meeting Rooms Iで話した「累積和」のアイデアを応用。「同時進行中の会議数」の**最大値**が答え、という点がポイント。
- `(start,+1)`, `(end,-1)`というイベントに変換して時刻順にソート→累積することで、巨大な配列(`O(10^6)`)を使わずに済んだ。
- 同時刻に`-1`と`+1`がある場合(前の会議終了と次の会議開始が同時刻)、タプル`(time, delta)`をそのままソートすると`-1 < +1`なので自動的に`-1`が先に処理される、という性質を利用した。
- 実装でのつまずき: 最初、最後に`current_meeting_rooms`をそのまま返してしまい、全部処理し終わると常に0になる(+1と-1の数が同じため)ことに気づかず、「最大値を別変数で追跡する」のを一度忘れた。
- `sorted_events`を作ったのに、ループでは元の`events`(未ソート)を回してしまうミスもあった。
- 「元のintervalsをソートしたと思っていたが、実際は(time,delta)のイベントに変換した後のものをソートしていた」という勘違いにも気づいて修正。
- メソッド名を`canAttendMeetings`(#252のもの)のままにしていたので`minMeetingRooms`に修正。

## Step 2
### 整形して変えた点
- Martin Fowlerの「Extract Function」を意識して、「intervals→イベント列に変換」と「イベントを処理して最大部屋数を求める」の2つに関数分割。
- `sorted(events)`(新しいリストを作る)から`events.sort()`(in-place)に変更してコピーを削減。`list.sort()`は`None`を返すので`return events.sort()`と1行で書けない点でつまずいた(`append`と同じ「in-place系メソッドはNoneを返す」というPythonの慣習)。
- メソッド名を`minAttendMeetings`(誤り)→`minMeetingRooms`(LeetCode指定名)に修正。
- ヘルパーメソッド名を試行錯誤: `buildMeeting`→`buildEventPairs`→`to_timeline`、`countMinMeetings`→`countMaxRooms`→`count_max_rooms`。
- クラスメソッドなのに`self`を忘れる、呼び出し元の変数名(`timelines`)と受け取り側(`events`)の不一致、といった単純ミスを複数回踏んで直した。

## Step 3（3回連続の記録・例外あり）
- (エラーで複数回リセット: タイポ`buils_timelines`/`events.sorted()`、`self.`忘れ、`max_rooms_sor_far`/`max_rooms_so_far`の変数名不一致など)
- 1回目: 2026-08-22, 5min, ok
- 2026-08-23: リセット後の1回目、ok(実行確認済み、`2`,`1`で正しい)

**例外扱い**: 公式フローの「3回連続」には届いていないが、本人希望によりこの時点でmastered扱いとした。タイポでのリセットが続いたことと、Premium問題のため元々LeetCode実行環境がなく手動検証のみで進めていたことを考慮。tracker.mdのattempts列には実態を反映（○のみ、○○○ではない）。

## 参考
- https://github.com/olsen-blue/Arai60/pull/57
- https://github.com/mamo3gr/arai60/pull/60
- https://github.com/Yoshiki-Iwasa/Arai60/pull/61
- https://github.com/t9a-dev/LeetCode_arai60/pull/56
- https://github.com/Manato110/LeetCode-arai60/pull/57
