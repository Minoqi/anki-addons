# Counts
<!-- ｶｳﾝﾄ -->

Here is the list of everything counted in the add-on. Not everything
can be displayed in a column. This document is mostly for people
working on the code.
<!-- ここでは､ｱﾄﾞｵﾝでｶｳﾝﾄされるすべての項目のﾘｽﾄを示します｡すべてが列に表示できるわけではありません｡このﾄﾞｷｭﾒﾝﾄは主にｺｰﾄﾞに取り組んでいる人々のためのものです｡ -->

## Values already computed by basic Anki
<!-- 基本的なAnkiによって既に計算された値 -->

### review today
<!-- 今日のﾚﾋﾞｭｰ -->
The number of reviewed cards to see today.
<!-- 今日見るﾚﾋﾞｭｰ済みのｶｰﾄﾞの数｡ -->

### New today
<!-- 今日の新規ｶｰﾄﾞ -->
The number of new cards to learn today.
<!-- 今日学習する新しいｶｰﾄﾞの数｡ -->

### Repetition of today learning
<!-- 今日の学習の繰り返し -->
Number of reviews you'll see of cards in learning today.
<!-- 今日学習中のｶｰﾄﾞのﾚﾋﾞｭｰ回数｡ -->

## Numbers directly computed in the database
<!-- ﾃﾞｰﾀﾍﾞｰｽで直接計算された数値 -->

### learning now from today
<!-- 今日からの現在の学習 -->
Number of cards in learning to see today which was planified today.
<!-- 今日計画された今日見る学習中のｶｰﾄﾞの数｡ -->

### flag i
<!-- ﾌﾗｸﾞ i -->
Cards flagged with flag i.
<!-- ﾌﾗｸﾞiが付けられたｶｰﾄﾞ｡ -->

### learning today from past
<!-- 過去からの今日の学習 -->
Cards in learning to see today and which have waited at least a day.
<!-- 今日見る学習中のｶｰﾄﾞで､少なくとも1日待ったもの｡ -->

### learning later today
<!-- 今日後で学習 -->
Cards in learning which are due today but not now.
<!-- 今日が期限だが､今ではない学習中のｶｰﾄﾞ｡ -->

They were last seen today. There are no cards from past days, due
today but not anymore.
<!-- 最後に見たのは今日です｡過去の日からのｶｰﾄﾞはなく､今日が期限ですが､もうありません｡ -->

### learning future
<!-- 将来の学習 -->
Cards in learning such that this review will not occur today (no way
of knowing whether it's from today or from a past day)
<!-- 今日ﾚﾋﾞｭｰが行われない学習中のｶｰﾄﾞ（それが今日からか過去の日からかを知る方法はありません） -->

### learning today repetition from today
<!-- 今日からの今日の学習の繰り返し -->
Number of repetitions you'll see today of cards currently in learning
such that the last repetition was today.
<!-- 今日の最後の繰り返しが今日である学習中のｶｰﾄﾞの繰り返し回数｡ -->

Similar to Repetition of today
learning, restricting cards to the one seen today.
<!-- 今日の学習の繰り返しに似ていますが､今日見たｶｰﾄﾞに制限されています｡ -->

### learning today repetition from past
<!-- 過去からの今日の学習の繰り返し -->
Number of repetitions you'll see today of cards currently in learning
such that last repetition was NOT today.
<!-- 最後の繰り返しが今日ではない学習中のｶｰﾄﾞの繰り返し回数｡ -->

Similar to last case, apart
from the negation
<!-- 否定を除いて､前のｹｰｽに似ています｡ -->

### learning repetition from today
<!-- 今日からの学習の繰り返し -->
Number of repetitions you'll see ANY day of cards currently in learning
such that the last repetition was today.
<!-- 現在学習中のｶｰﾄﾞのうち､最後の繰り返しが今日であるｶｰﾄﾞの繰り返し回数を任意の日に表示します｡ -->

Similar to "learning today
repetition from today" case, apart from that we count repetition not to
see today.
<!-- ｢今日からの今日の学習の繰り返し｣のｹｰｽに似ていますが､今日は表示されない繰り返しをｶｳﾝﾄします｡ -->

### learning repetition from past
<!-- 過去からの学習の繰り返し -->
Number of repetitions you'll see ANY day of cards currently in learning
such that the last repetition was NOT today.
<!-- 現在学習中のｶｰﾄﾞのうち､最後の繰り返しが今日ではないｶｰﾄﾞの繰り返し回数を任意の日に表示します｡ -->

Similar to "learning today
repetition from past" case, apart from that we count repetitions not to
see today. Similar to "learning repetition from today" apart from the negation.
<!-- ｢過去からの今日の学習の繰り返し｣のｹｰｽに似ていますが､今日は表示されない繰り返しをｶｳﾝﾄします｡｢今日からの学習の繰り返し｣と否定を除いて似ています｡ -->

### review due
<!-- 期限のﾚﾋﾞｭｰ -->
Number of cards which have already been seen and are due today (even
if it's greater than the maximum number of cards the configuration allows
to see for this deck).
<!-- 既に見たことがあり､今日が期限のｶｰﾄﾞの数（設定でこのﾃﾞｯｷに表示できるｶｰﾄﾞの最大数を超えている場合でも）｡ -->

### unseen
<!-- 未見 -->
Number of cards which have never graduated and are not in learning.
<!-- 卒業したことがなく､学習中でないｶｰﾄﾞの数｡ -->

### buried
<!-- 埋められたｶｰﾄﾞ -->
Number of buried cards
<!-- 埋められたｶｰﾄﾞの数 -->

### suspended
<!-- 保留中のｶｰﾄﾞ -->
Number of suspended cards
<!-- 保留中のｶｰﾄﾞの数 -->

### cards
<!-- ｶｰﾄﾞ -->
Number of cards
<!-- ｶｰﾄﾞの数 -->

### notes
<!-- ﾉｰﾄ -->
Number of notes
<!-- ﾉｰﾄの数 -->

### undue
<!-- 未期日 -->
Cards which have already been seen at least once, are not in learning,
and are not due today.
<!-- 少なくとも一度は見たことがあり､学習中ではなく､今日が期限ではないｶｰﾄﾞ｡ -->

### mature
<!-- 成熟ｶｰﾄﾞ -->
Any card already seen with an interval of at least 21 days
<!-- 既に見たことがあり､間隔が少なくとも21日あるｶｰﾄﾞ｡ -->

### young
<!-- 若いｶｰﾄﾞ -->
Any card already seen with an interval of at least one day and at most 20 days
<!-- 既に見たことがあり､間隔が1日以上20日以下のｶｰﾄﾞ｡ -->

## Sum of previous values
<!-- 前の値の合計 -->

### learning now
<!-- 現在の学習 -->
Number of cards in learning ready to be seen (from today+from yesterday).
<!-- 今日または昨日から見られる準備ができている学習中のｶｰﾄﾞの数｡ -->

### learning later
<!-- 後で学習 -->
Number of cards in learning not ready to be seen (to see later today,
or in the future).
<!-- 今日後でまたは将来に見る準備ができていない学習中のｶｰﾄﾞの数｡ -->

### learning card
<!-- 学習ｶｰﾄﾞ -->
Number of cards in learning (now+later)
<!-- 学習中のｶｰﾄﾞの数（現在+後で） -->

### learning today repetition
<!-- 今日の学習の繰り返し -->
Number of repetition to cards in learning today (sum of repetition
from card from a past day, and from today).
<!-- 今日の学習中のｶｰﾄﾞの繰り返し回数（過去の日からのｶｰﾄﾞの繰り返しと今日のｶｰﾄﾞの繰り返しの合計）｡ -->

Isn't it equal to "Repetition of today learning"???TODO
<!-- これは｢今日の学習の繰り返し｣と同じではないですか???TODO -->

### learning repetition
<!-- 学習の繰り返し -->
Number of repetition of cards in learning, any days (sum of
repetitions from today and from past days)
<!-- 学習中のｶｰﾄﾞの繰り返し回数（今日と過去の日からの繰り返しの合計） -->

### learning future repetition
<!-- 将来の学習の繰り返し -->
Number of repetition of cards in learning, but not today. (Number of
repetitions minus repetition to do today)
<!-- 学習中のｶｰﾄﾞの繰り返し回数､ただし今日ではない（今日行う繰り返しを差し引いた繰り返し回数） -->

### review later
<!-- 後でﾚﾋﾞｭｰ -->
Cards to review, which are due, but won't be seen today because of
deck's configured limit. (review due - review today)
<!-- 期限が来ているが､ﾃﾞｯｷの設定された制限のために今日見られないｶｰﾄﾞ（期限のﾚﾋﾞｭｰ - 今日のﾚﾋﾞｭｰ） -->

### reviewed today
<!-- 今日ﾚﾋﾞｭｰされたｶｰﾄﾞ -->
Cards whose last successful review was today. (A card deleted after
review is not counted anymore. A card reviewed and moved is counted in
its new deck. A card reviewed many times is counted once. Cards in
learning are not counted. TODO: find how to easily find how to count
cards in learning whose last review is today)
<!-- 最後の成功したﾚﾋﾞｭｰが今日であるｶｰﾄﾞ（ﾚﾋﾞｭｰ後に削除されたｶｰﾄﾞはｶｳﾝﾄされません｡ﾚﾋﾞｭｰされて移動されたｶｰﾄﾞは新しいﾃﾞｯｷでｶｳﾝﾄされます｡何度もﾚﾋﾞｭｰされたｶｰﾄﾞは一度だけｶｳﾝﾄされます｡学習中のｶｰﾄﾞはｶｳﾝﾄされません｡TODO: 最後のﾚﾋﾞｭｰが今日である学習中のｶｰﾄﾞを簡単にｶｳﾝﾄする方法を見つける） -->

### repeated today
<!-- 今日繰り返されたｶｰﾄﾞ -->
Number of times you saw today a question from this deck. (A card
deleted after review is not counted anymore. A card reviewed and moved
is counted in its new deck.)
<!-- 今日このﾃﾞｯｷからの質問を見た回数（ﾚﾋﾞｭｰ後に削除されたｶｰﾄﾞはｶｳﾝﾄされません｡ﾚﾋﾞｭｰされて移動されたｶｰﾄﾞは新しいﾃﾞｯｷでｶｳﾝﾄされます｡） -->

### repeated today
<!-- 今日繰り返されたｶｰﾄﾞ -->
Number of times you saw a question from this deck anytime in the
past. (A card deleted after review is not counted anymore. A card
reviewed and moved is counted in its new deck.)
<!-- 過去にこのﾃﾞｯｷからの質問を見た回数（ﾚﾋﾞｭｰ後に削除されたｶｰﾄﾞはｶｳﾝﾄされません｡ﾚﾋﾞｭｰされて移動されたｶｰﾄﾞは新しいﾃﾞｯｷでｶｳﾝﾄされます｡） -->

### unseen later
<!-- 後で未見 -->
Cards never seen, and won't be seen today because of deck's
configured limit. (unseen - new today)
<!-- 一度も見たことがなく､ﾃﾞｯｷの設定された制限のために今日見られないｶｰﾄﾞ（未見 - 今日の新規ｶｰﾄﾞ） -->

### repetition seen today
<!-- 今日見た繰り返し -->
Number of repetitions of cards to see today which are not new
<!-- 今日見る新しくないｶｰﾄﾞの繰り返し回数 -->

### repetition today
<!-- 今日の繰り返し -->
Number of repetitions of cards to see today
<!-- 今日見るｶｰﾄﾞの繰り返し回数 -->

### cards seen today
<!-- 今日見たｶｰﾄﾞ -->
Number of cards to see today which are not new
<!-- 今日見る新しくないｶｰﾄﾞの数 -->

### today
<!-- 今日 -->
Number of cards to see today
<!-- 今日見るｶｰﾄﾞの数 -->

Similar to Repetition of today learning, but each card is counted
once, even if it'll be seen multiple times.
<!-- 今日の学習の繰り返しに似ていますが､複数回見られる場合でも各ｶｰﾄﾞは一度だけｶｳﾝﾄされます｡ -->

# Sets
<!-- ｾｯﾄ -->
When we consider note, we must use sets instead of numbers. Because a
note may be in multiple subdecks, and we don't want to count it
multiple times.
<!-- ﾉｰﾄを考慮する場合､数値の代わりにｾｯﾄを使用する必要があります｡ﾉｰﾄは複数のｻﾌﾞﾃﾞｯｷに存在する可能性があり､複数回ｶｳﾝﾄしたくないためです｡ -->

The size of the sets are then counted and added in the previous
dictionnary.
<!-- ｾｯﾄのｻｲｽﾞはｶｳﾝﾄされ､前の辞書に追加されます｡ -->

### notes
<!-- ﾉｰﾄ -->
The set of nids from this deck
<!-- このﾃﾞｯｷからのnidのｾｯﾄ -->

### marked
<!-- ﾏｰｸされたﾉｰﾄ -->
The set of nids of marked notes in this deck
<!-- このﾃﾞｯｷでﾏｰｸされたﾉｰﾄのnidのｾｯﾄ -->

# Texts
<!-- ﾃｷｽﾄ -->
Here, we have columns content which is more than just text
<!-- ここでは､単なるﾃｷｽﾄ以上の列の内容があります -->

## Time
<!-- 時間 -->
### learning now
<!-- 現在の学習 -->
Number of minute/seconds before a card in learning can be seen (only
if a value is not already given)
<!-- 学習中のｶｰﾄﾞが見られるまでの分/秒数（値が既に与えられていない場合のみ） -->

## Pair of values
<!-- 値のﾍﾟｱ -->
Mature/young
Notes/cards
Buried/suspended
Reviewed/repeated today
<!-- 成熟/若い
ﾉｰﾄ/ｶｰﾄﾞ
埋められた/保留中
今日ﾚﾋﾞｭｰ/繰り返された -->

## flags
<!-- ﾌﾗｸﾞ -->
flags 1 to 4.
<!-- ﾌﾗｸﾞ1から4 -->

### all flags
<!-- すべてのﾌﾗｸﾞ -->
(including flag 0, i.e. no flag).
<!-- ﾌﾗｸﾞ0（つまりﾌﾗｸﾞなし）を含む -->

## Now and later
<!-- 現在と後で -->

### Review
<!-- ﾚﾋﾞｭｰ -->
review today (review later)
<!-- 今日のﾚﾋﾞｭｰ（後でﾚﾋﾞｭｰ） -->

### unseen new
<!-- 未見の新規 -->
new today (unseen later)
<!-- 今日の新規（後で未見） -->

### Learning today
<!-- 今日の学習 -->
learning now (learning later today)
<!-- 現在の学習（今日後で学習） -->
