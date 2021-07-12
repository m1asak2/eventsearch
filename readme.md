# イベントサーチ

セミナー､研修会サイトを横断検索



IF

| parameters | 用途            |                     |
| ---------- | --------------- | ------------------- |
| keyword    | キーワード(AND) |                     |
| address    | 開催居場所(OR)  |                     |
| start_from | 開始日          |                     |
| start_to   | 終了日          |                     |
| limit      | 取得件数        |                     |
| target     | 検索サイト(OR)  | connpass,doorkeeper |



## connpass仕様

| 項目       | 仕様                    | keyword    |
| ---------- | ----------------------- | ---------- |
| 開催場所   | 複数検索                | keyword_or |
| 開催日     | ○月以降～または月日指定 |            |
| キーワード |                         |            |

bs4スクレイピング

| 項目     | 仕様               | keyword |
| -------- | ------------------ | ------- |
| 開催場所 | or検索で複数選択可 |         |
| 開催日   | 期間を指定         | From    |
|          |                    | To      |
|          |                    |         |



DoorKeeper仕様

| parameters                      |                                |            |
| ------------------------------- | ------------------------------ | ---------- |
| page                            | The page offset of the results |            |
| The page offset of the results. |                                |            |
| since                           |                                | start_from |
| until                           |                                | start_to   |
| q                               |                                | keyword    |
| prefecture                      |                                | address    |
| sort                            | sort=starts_at で固定          |            |
| page                            |                                | limit      |



