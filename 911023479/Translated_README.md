# anki-enhance-main-window
<!--anki-enhance-main-window-->
Adds a lot of features to the main window. Allows configuration of those features. Configurations are explained at the end of this document.
<!--ﾒｲﾝｳｨﾝﾄﾞｳに多くの機能を追加します｡これらの機能の設定を可能にします｡設定はこのﾄﾞｷｭﾒﾝﾄの最後に説明されています｡-->

Important updates:
<!--重要な更新：-->
* 5th of June 2019: A column for flags, and columns for each flag
<!--2019年6月5日：ﾌﾗｸﾞ用の列､および各ﾌﾗｸﾞ用の列-->
* 30th of March 2019: column can be dragged and dropped, and use right click to delete.
<!--2019年3月30日：列をﾄﾞﾗｯｸﾞｱﾝﾄﾞﾄﾞﾛｯﾌﾟでき､右ｸﾘｯｸで削除できます｡-->
* 12 February 2019: default colors are changed to use the color of the statistic window.
<!--2019年2月12日：ﾃﾞﾌｫﾙﾄの色が統計ｳｨﾝﾄﾞｳの色に変更されました｡-->
* 11 February 2019: percent bar
<!--2019年2月11日：ﾊﾟｰｾﾝﾄﾊﾞｰ-->
* February: counting the number of reviews, today and any time in the past, and the number of cards seen today.
<!--2月：今日および過去の任意の時点でのﾚﾋﾞｭｰ数と､今日見たｶｰﾄﾞの数をｶｳﾝﾄします｡-->
* 19th January 2019: many bugs corrected. Configuration can be changed without restarting Anki.
<!--2019年1月19日：多くのﾊﾞｸﾞが修正されました｡Ankiを再起動せずに設定を変更できます｡-->
* 8th November 2018: you can configure the add-on using anki 2.1's configuration method. The configuration won't be lost during next update of the add-on !
<!--2018年11月8日：anki 2.1の設定方法を使用してｱﾄﾞｵﾝを設定できます｡ｱﾄﾞｵﾝの次の更新時に設定が失われることはありません！-->

<!-- ![Example](example.png) -->

### Name of the (sub)deck
<!--Name of the (sub)deck-->
There is not a lot of change in this column, apart from the decks's color.
<!--この列には､ﾃﾞｯｷの色以外にはあまり変更はありません｡-->

#### Empty decks
<!--Empty decks-->
If a (sub)deck is empty, it turns red. (You can configure the color.)
<!--(ｻﾌﾞ)ﾃﾞｯｷが空の場合､それは赤くなります｡（色は設定可能です｡）-->

This may not be useful for everybody. But if you want to know when a deck is empty in order to add new notes in it, it avoids having to check the number of new cards for each deck. For example, if you want to learn guitar chords, it will let you know that it is time to add new chords to Anki.
<!--これはすべての人にとって有用ではないかもしれません｡しかし､ﾃﾞｯｷが空であることを知り､新しいﾉｰﾄを追加したい場合､各ﾃﾞｯｷの新しいｶｰﾄﾞの数を確認する手間を省くことができます｡例えば､ｷﾞﾀｰのｺｰﾄﾞを学びたい場合､Ankiに新しいｺｰﾄﾞを追加する時期を知らせてくれます｡-->

Whats even better ! If you use subdecks, the ancestors (parent) of an empty subdeck become blue (also configurable). This allows you to find decks with an empty subdeck. Hence, it helps finding empty subdecks without having to expand every top-level deck.
<!--さらに良いことに！ｻﾌﾞﾃﾞｯｷを使用している場合､空のｻﾌﾞﾃﾞｯｷの祖先（親）は青くなります（これも設定可能です）｡これにより､空のｻﾌﾞﾃﾞｯｷを持つﾃﾞｯｷを見つけることができます｡したがって､すべてのﾄｯﾌﾟﾚﾍﾞﾙのﾃﾞｯｷを展開することなく､空のｻﾌﾞﾃﾞｯｷを見つけるのに役立ちます｡-->

Note that, in some cases, you don't want the name to become red, e.g. you wanted to learn the name of the Greek letters. When you know all of them, you won't add any new note ever. You just have to add a semicolon (;) (that is configurable) to the name of the deck, and it will not turn red.
<!--ただし､場合によっては名前が赤くなるのを避けたいことがあります｡例えば､ｷﾞﾘｼｬ文字の名前を学びたい場合です｡すべての文字を覚えたら､新しいﾉｰﾄを追加することはありません｡この場合､ﾃﾞｯｷの名前にｾﾐｺﾛﾝ（;）（これは設定可能です）を追加するだけで､赤くなりません｡-->

#### Marked cards
<!--Marked cards-->
Decks with marked card have a blue background (configurable). Furthermore, if the deck's name contains a semicolon (i.e. as explained above, the deck is ended), then the background become yellow.
<!--ﾏｰｸされたｶｰﾄﾞを持つﾃﾞｯｷは青い背景になります（設定可能）｡さらに､ﾃﾞｯｷの名前にｾﾐｺﾛﾝが含まれている場合（つまり､上記のようにﾃﾞｯｷが終了している場合）､背景は黄色になります｡-->

### Learning
<!--Learning-->
The number of reviews of cards in learning. By default you will see the number of reviews that can be done now, and in parentheses the number of reviews which can be done later today.
<!--学習中のｶｰﾄﾞのﾚﾋﾞｭｰ数｡ﾃﾞﾌｫﾙﾄでは､現在実行できるﾚﾋﾞｭｰ数が表示され､括弧内に今日後で実行できるﾚﾋﾞｭｰ数が表示されます｡-->

### Review
<!--Review-->
The number of cards which you have seen in the past, and that you should see today. By default, the number of cards you will see today. And in parentheses the number of cards you should see today, but that you will not see today because of your limit.
<!--過去に見たｶｰﾄﾞの数と､今日見るべきｶｰﾄﾞの数｡ﾃﾞﾌｫﾙﾄでは､今日見るｶｰﾄﾞの数が表示されます｡括弧内には､今日見るべきだが制限のために今日見ないｶｰﾄﾞの数が表示されます｡-->

### New today
<!--New today-->
This column called new in Anki. New means «number of new cards you will see today», with the caveat that it is not exactly true for subdecks.
<!--この列はAnkiでは｢新しい｣と呼ばれます｡新しいとは｢今日見る新しいｶｰﾄﾞの数｣を意味しますが､ｻﾌﾞﾃﾞｯｷには正確には当てはまりません｡-->

### New
<!--New-->
The column name "new" is deprecated. It is kept for backwards compatibility, but may be removed one day. It is the same thing as New Today.
<!--｢新しい｣という列名は非推奨です｡後方互換性のために保持されていますが､いつか削除されるかもしれません｡これは｢今日の新しい｣と同じ意味です｡-->

### Due
<!--Due-->
By default, this column is hidden. Indeed, it became two columns «due now» and «later». We recall that, in Anki, a due card is a card which is not new, and that you have to view again today.
<!--ﾃﾞﾌｫﾙﾄでは､この列は非表示です｡実際には｢今期限｣と｢後で｣の2つの列になりました｡Ankiでは､期限ｶｰﾄﾞとは新しくないｶｰﾄﾞであり､今日再度見る必要があるｶｰﾄﾞです｡-->

### Unseen
<!--Unseen-->
The number of cards which you have never answered. Most of these cards are cards you have never seen, but it also considers cards you have seen and buried. By default, the number of unseen cards which you will discover today, and in parentheses the number of unseen cards you will not see today.
<!--一度も回答したことのないｶｰﾄﾞの数｡これらのｶｰﾄﾞのほとんどは一度も見たことのないｶｰﾄﾞですが､見たことがあり埋もれているｶｰﾄﾞも含まれます｡ﾃﾞﾌｫﾙﾄでは､今日発見する未見のｶｰﾄﾞの数が表示され､括弧内には今日見ない未見のｶｰﾄﾞの数が表示されます｡-->

### Young
<!--Young-->
The number of cards whose interval is less than 3 weeks
<!--間隔が3週間未満のｶｰﾄﾞの数-->

### Mature
<!--Mature-->
The number of cards whose interval is at least 3 weeks
<!--間隔が少なくとも3週間のｶｰﾄﾞの数-->

### Buried
<!--Buried-->
The number of Buried cards. Keep in mind that a buried card is a card you will not see today, either because you pressed the «bury» button, or because you saw another card from the same note, so it was automatically buried.
<!--埋められたｶｰﾄﾞの数｡埋められたｶｰﾄﾞとは､｢埋める｣ﾎﾞﾀﾝを押したか､同じﾉｰﾄの別のｶｰﾄﾞを見たために自動的に埋められたｶｰﾄﾞであり､今日は表示されないｶｰﾄﾞのことです｡-->

### Suspended
<!--Suspended-->
The number of Suspended cards. Keep in mind that a suspended card is a card you will never see again, unless you unsuspend it manually (using the browser).
<!--保留中のｶｰﾄﾞの数｡保留中のｶｰﾄﾞとは､手動で保留解除しない限り（ﾌﾞﾗｳｻﾞを使用して）二度と表示されないｶｰﾄﾞのことです｡-->

### Total
<!--Total-->
The number of cards in this deck. It is not the sum of the preceding column, since it contains also cards you have already seen and which are not yet due (and it counts a card with multiple reviews once).
<!--このﾃﾞｯｷ内のｶｰﾄﾞの数｡これは前の列の合計ではありません｡すでに見たｶｰﾄﾞやまだ期限が来ていないｶｰﾄﾞも含まれているためです（複数回ﾚﾋﾞｭｰされたｶｰﾄﾞは一度だけｶｳﾝﾄされます）｡-->

### Today
<!--Today-->
The total number of reviews you will see today (assuming you always rate good).
<!--今日見るﾚﾋﾞｭｰの総数（常に良い評価をすることを前提としています）｡-->

### Configuration
<!--Configuration-->
The last column states which options group is used for the current deck. This avoids the pain of opening the menu to see the option names. Really useful when you have a lot of decks and want to see which is the last deck which used this old configuration you want to delete.
<!--最後の列は､現在のﾃﾞｯｷに使用されているｵﾌﾟｼｮﾝｸﾞﾙｰﾌﾟを示します｡これにより､ﾒﾆｭｰを開いてｵﾌﾟｼｮﾝ名を確認する手間が省けます｡ﾃﾞｯｷが多い場合や､削除したい古い設定を使用した最後のﾃﾞｯｷを確認したい場合に非常に便利です｡-->

## Capping
<!--Capping-->
By default, Anki does not show any number greater than 1000. Instead it shows 1000+.
You can now edit this limit, or remove it entirely (by using a negative number). If you set the limit to 0, you will either see a 0, or "+".
<!--ﾃﾞﾌｫﾙﾄでは､Ankiは1000を超える数字を表示しません｡代わりに1000+と表示されます｡
この制限を編集するか､完全に削除することができます（負の数を使用することで）｡制限を0に設定すると､0または｢+｣が表示されます｡-->

How to configure this add-on
============================
<!--How to configure this add-on-->
Most options are configurable. If some option is not configurable, send me an email and I'll see what I can do.
<!--ほとんどのｵﾌﾟｼｮﾝは設定可能です｡設定できないｵﾌﾟｼｮﾝがある場合は､ﾒｰﾙを送ってください｡できる限り対応します｡-->

In order to configure this add-on (hence, to configure what is shown in the main window), go to Tools>add-ons>\[name of this add-on]>Config. You'll see the configuration file. It will also display in a small window a display of the configuration's rule. We copy them below
<!--このｱﾄﾞｵﾝを設定するには（つまり､ﾒｲﾝｳｨﾝﾄﾞｳに表示される内容を設定するには）､ﾂｰﾙ>ｱﾄﾞｵﾝ>[このｱﾄﾞｵﾝの名前]>設定に移動します｡設定ﾌｧｲﾙが表示されます｡また､小さなｳｨﾝﾄﾞｳに設定のﾙｰﾙが表示されます｡以下にそれらをｺﾋﾟｰします｡-->
# Configuration file


### CSS
<!--CSS-->
If the value is `null` then the default css is used. Otherwise, you can put the CSS you want here.  Use the add-on [Newline in strings in add-ons configurations](https://ankiweb.net/shared/info/112201952) if you want to use newline in JSON/CSS string.
<!--値が `null` の場合､ﾃﾞﾌｫﾙﾄのCSSが使用されます｡それ以外の場合は､ここに任意のCSSを入力できます｡JSON/CSS文字列に改行を使用したい場合は､ｱﾄﾞｵﾝ [Newline in strings in add-ons configurations](https://ankiweb.net/shared/info/112201952) を使用してください｡-->

### Refresh rate
<!--ﾘﾌﾚｯｼｭﾚｰﾄ-->
How much time to wait between refreshing the main window. In seconds. By default, the window is refreshed every 30 seconds, thus, it is possible that change made less than half a minute ago are not yet shown.
<!--ﾒｲﾝｳｨﾝﾄﾞｳをﾘﾌﾚｯｼｭする間隔（秒単位）｡ﾃﾞﾌｫﾙﾄでは､ｳｨﾝﾄﾞｳは30秒ごとにﾘﾌﾚｯｼｭされるため､30秒未満の変更はまだ表示されない可能性があります｡-->

### Option
<!--ｵﾌﾟｼｮﾝ-->
Whether you want to display the deck's Option group's name, at the end of its line.
<!--ﾃﾞｯｷのｵﾌﾟｼｮﾝｸﾞﾙｰﾌﾟの名前を行の末尾に表示するかどうか｡-->

### cap value
<!--ｷｬｯﾌﾟ値-->
By default, without add-on, Anki never shows number greater than a thousand. Instead, it shows 1000+. You can decide to change a thousand by an arbitrary number. Or leave this value to null, and always show the real value.
<!--ﾃﾞﾌｫﾙﾄでは､ｱﾄﾞｵﾝなしでAnkiは1000を超える数字を表示しません｡代わりに1000+と表示されます｡任意の数値に変更することもできます｡この値をnullにして､常に実際の値を表示することもできます｡-->

Note that capping to a thousand does not usually make the rendering quicker.
<!--1000に制限しても､通常はﾚﾝﾀﾞﾘﾝｸﾞが速くなるわけではありません｡-->

## Columns
<!--Columns-->
Each column should occur after the line "columns" :\[, and before the line with a closing bracket ]. The order of the lines is important, since it's the order in which columns will be displayed by anki. This order can also be changed by dragging and dropping the column title. This means that you can reorder columns in anki by reordering the lines in the configuration. You can copy a line to display a column multiple time (for example, once using percent, and another time using absolute number).
<!--各列は "columns" :[ の行の後､閉じ括弧 ] の行の前に配置する必要があります｡行の順序は重要で､ankiが列を表示する順序になります｡この順序は､列のﾀｲﾄﾙをﾄﾞﾗｯｸﾞｱﾝﾄﾞﾄﾞﾛｯﾌﾟすることで変更することもできます｡つまり､設定内の行を並べ替えることで､anki内の列を並べ替えることができます｡行をｺﾋﾟｰして､列を複数回表示することもできます（例えば､ﾊﾟｰｾﾝﾄで一度､絶対数で一度）｡-->

Each column is represented between an opening curly bracket {, and a closing curly bracket }. Each column uses 8 parameters, each represented as a pair `key:value`. We'll tell you the meaning of each key, whether you can change its value, and what will this change do.
<!--各列は､開き中括弧 { と閉じ中括弧 } の間に表されます｡各列は8つのﾊﾟﾗﾒｰﾀを使用し､それぞれが `key:value` のﾍﾟｱとして表されます｡各ｷｰの意味､その値を変更できるかどうか､およびその変更が何をするかを説明します｡-->

### Name
<!--Name-->
The first value is a description, which will tell you what the column represent. Do NOT alter this value, or the add-on will raise an error.
<!--最初の値は説明であり､列が何を表しているかを示します｡この値を変更しないでください｡変更するとｱﾄﾞｵﾝがｴﾗｰを発生させます｡-->

### Description
<!--Description-->
A description of the content of the column. This is not used by anki, it allows you to decide whether you want the column or not while you edit the configuration.
<!--列の内容の説明です｡これはankiによって使用されませんが､設定を編集している間に列が必要かどうかを決定するのに役立ちます｡-->

### Present
<!--Present-->
The value for the key "present" is either true or false. If the value is true, the column will be displayed. Otherwise, it will not. Note that you can also delete the entire column from the configuration, instead of changing the value to false.
<!--ｷｰ "present" の値は true または false です｡値が true の場合､列が表示されます｡そうでない場合は表示されません｡値を false に変更する代わりに､設定から列全体を削除することもできます｡-->

If this value is absent, by default, it is assumed that it should be true.
<!--この値が存在しない場合､ﾃﾞﾌｫﾙﾄでは true であると見なされます｡-->

### Header
<!--Header-->
The header of the column. If you leave «null» then the default header will be used. This description will be translated as much as it is possible to do it automatically. However, you can also choose to write your own description. You can use html in this description. I.e. you should use "<br/>" when you want a newline.
<!--列のﾍｯﾀﾞｰです｡ «null» のままにすると､ﾃﾞﾌｫﾙﾄのﾍｯﾀﾞｰが使用されます｡この説明は可能な限り自動的に翻訳されます｡ただし､自分で説明を書くこともできます｡この説明にはhtmlを使用できます｡例えば､改行したい場合は "<br/>" を使用する必要があります｡-->

### Overlay
<!--Overlay-->
The text shown when your mouse is over a number. It will describe what this number represent. You can remove this key if you want no description to be present. And leave this value to null if you want to use the default value.
<!--数値の上にﾏｳｽを置いたときに表示されるﾃｷｽﾄです｡この数値が何を表しているかを説明します｡説明を表示したくない場合は､このｷｰを削除できます｡ﾃﾞﾌｫﾙﾄ値を使用したい場合は､この値をnullにしてください｡-->

### Color
<!--Color-->
The color in which the number is shown in this column. You can use any color acceptable in an HTML document. The most standard color's name should work.
<!--この列に数値が表示される色｡HTMLﾄﾞｷｭﾒﾝﾄで使用可能な任意の色を使用できます｡最も標準的な色の名前が機能するはずです｡-->

### Percent
<!--Percent-->
true or false whether you want to show the percent of cards satisfying this column condition. For example, 23% of cards are new. Note that sometimes, this would not make sense. For example, for the column «cards», the value will always be 100% (unless the deck is empty). For the column notes, the number would not really make any sens (formally, you'd get the percent of cards which is the first of its sibling in this deck).
<!--この列の条件を満たすｶｰﾄﾞの割合を表示するかどうかを示すtrueまたはfalse｡例えば､ｶｰﾄﾞの23％が新しいことを示します｡ただし､場合によっては意味をなさないこともあります｡例えば､｢ｶｰﾄﾞ｣列の場合､値は常に100％になります（ﾃﾞｯｷが空でない限り）｡｢ﾉｰﾄ｣列の場合､その数値はあまり意味を持ちません（形式的には､このﾃﾞｯｷで兄弟の最初のｶｰﾄﾞの割合を取得することになります）｡-->

By default, percent is assumed to be false if absent.
<!--ﾃﾞﾌｫﾙﾄでは､percentが存在しない場合はfalseと見なされます｡-->

### Absolute
<!--Absolute-->
Whether you want an absolute number in your column or not. That is, a number which is not a percent, but an exact number.
<!--列に絶対数を表示するかどうか｡つまり､ﾊﾟｰｾﾝﾄではなく､正確な数値を表示します｡-->

By default, this value is false if Percent is set to true, otherwise its default value is true.
<!--ﾃﾞﾌｫﾙﾄでは､Percentがtrueに設定されている場合､この値はfalseになります｡それ以外の場合､ﾃﾞﾌｫﾙﾄ値はtrueです｡-->

### Subdecks
<!--Subdecks-->
When you consider a deck which has subdecks, you may want to consider cards in subdecks (it is done when the value is true), or you may want to ignore them (it is done when the value is false).
<!--ｻﾌﾞﾃﾞｯｷを持つﾃﾞｯｷを考慮する場合､ｻﾌﾞﾃﾞｯｷ内のｶｰﾄﾞを考慮するか（値がtrueの場合）､無視するか（値がfalseの場合）を選択できます｡-->

## Percent Bar
<!--Percent Bar-->
If the name is "bar", instead of a number, the column contain a percent bar.
<!--名前が｢bar｣の場合､数値の代わりに列にﾊﾟｰｾﾝﾄﾊﾞｰが含まれます｡-->

In this case, the configuration of this column must contain a field "names", whose value is a list of name. The names are the same name than for columns. It uses the same color and overlay.
<!--この場合､この列の設定には｢names｣というﾌｨｰﾙﾄﾞが含まれている必要があり､その値は名前のﾘｽﾄです｡名前は列と同じ名前です｡同じ色とｵｰﾊﾞｰﾚｲを使用します｡-->

## Coloring decks
<!--Coloring decks-->
The author of this add-on want to know when a deck is empty. This is very important to him, because he want to add new cards in them as soon as possible. Thus, this add-on change the color of the name of empty decks, and of name of decks with an empty descendant.
<!--このｱﾄﾞｵﾝの作者は､ﾃﾞｯｷが空であることを知りたいと考えています｡これは彼にとって非常に重要であり､できるだけ早く新しいｶｰﾄﾞを追加したいと考えています｡そのため､このｱﾄﾞｵﾝは空のﾃﾞｯｷの名前と空の子孫を持つﾃﾞｯｷの名前の色を変更します｡-->

The author also want to know which deck has marked card. Thus, the background of the deck's name with marked card change color.
<!--作者は､どのﾃﾞｯｷにﾏｰｸされたｶｰﾄﾞがあるかも知りたいと考えています｡そのため､ﾏｰｸされたｶｰﾄﾞを持つﾃﾞｯｷの名前の背景色が変わります｡-->

Both of those configuration can be changed as explained in this section. In particular, you can turn one or both of those options off by setting "color empty" and "color marked" to false.
<!--これらの設定は､このｾｸｼｮﾝで説明されているように変更できます｡特に､｢color empty｣と｢color marked｣をfalseに設定することで､これらのｵﾌﾟｼｮﾝのいずれかまたは両方をｵﾌにすることができます｡-->


### Choice of color
<!--Choice of color-->
#### Color empty
The color of the name of decks without new cards
<!--新しいｶｰﾄﾞがないﾃﾞｯｷの名前の色-->

#### Color empty descendant
The color of the name of decks with a descendant without new cards
<!--新しいｶｰﾄﾞがない子孫を持つﾃﾞｯｷの名前の色-->

#### Default color
The color of a deck whose every descendant has new cards.
<!--すべての子孫に新しいｶｰﾄﾞがあるﾃﾞｯｷの色-->

#### ended marked background color
The color of the decks which has an ended deck with marked cards. The notion of ended deck will be explained in the next section of this documentation.
<!--ﾏｰｸされたｶｰﾄﾞを持つ終了したﾃﾞｯｷを持つﾃﾞｯｷの色｡終了したﾃﾞｯｷの概念は､このﾄﾞｷｭﾒﾝﾄの次のｾｸｼｮﾝで説明されます｡-->

#### marked background color
The color of deck who have marked cards but none of its descendant are both ended and has marked card.
<!--ﾏｰｸされたｶｰﾄﾞを持つが､その子孫のいずれも終了しておらず､ﾏｰｸされたｶｰﾄﾞを持たないﾃﾞｯｷの色-->

### Deck modifier
<!--Deck modifier-->
A deck modifier is a symbol (or a word, etc..) whose presence in a deck name change the meaning of the deck. When the meaning is changed, the coloration is also change. It's not clear to the author of this add-on whether anyone appart from himself will need those, but if you want to use them, here is the explanation.
<!--ﾃﾞｯｷ修飾子は､ﾃﾞｯｷ名に存在することでﾃﾞｯｷの意味を変更する記号（または単語など）です｡意味が変更されると､色も変更されます｡このｱﾄﾞｵﾝの作者にとって､これが自分以外の誰かに必要かどうかは不明ですが､使用したい場合は以下の説明を参照してください｡-->

The first three symbols currently has the same effect, but it may occur that one day this effect may change, according of what the author want to do.
<!--最初の3つの記号は現在同じ効果を持っていますが､将来的には作者の意図に応じてこの効果が変わる可能性があります｡-->

#### End symbol
<!--End symbol-->
By default, this symbol is ";". It means that the deck is definitively done, and no new card may ever be added to it. When a deck has this symbol, neither itself nor its descendant will ever be colored.
<!--ﾃﾞﾌｫﾙﾄでは､この記号は｢;｣です｡これは､ﾃﾞｯｷが完全に終了し､新しいｶｰﾄﾞが追加されることはないことを意味します｡この記号を持つﾃﾞｯｷは､それ自体もその子孫も色付けされることはありません｡-->

#### Given up symbol
<!--Given up symbol-->
By default, this symbol is "/".To the author, it means that no new card will be added because this deck is either too hard, or not interesting enough.
<!--ﾃﾞﾌｫﾙﾄでは､この記号は｢/｣です｡作者にとって､これはこのﾃﾞｯｷが難しすぎるか､十分に興味深くないため､新しいｶｰﾄﾞが追加されないことを意味します｡-->

#### Pause symbol
<!--Pause symbol-->
By default, this symbol is "=". To the author, it means that more new card will be added latter, but right now it does not want anki to change the color of the deck's name. In a future version, there may be an option to change the color of those decks.
<!--ﾃﾞﾌｫﾙﾄでは､この記号は｢=｣です｡作者にとって､これは後で新しいｶｰﾄﾞが追加されることを意味しますが､今はankiがﾃﾞｯｷの名前の色を変更することを望んでいません｡将来のﾊﾞｰｼﾞｮﾝでは､これらのﾃﾞｯｷの色を変更するｵﾌﾟｼｮﾝが追加されるかもしれません｡-->

## Internals
<!--Internals-->
* In `aqt.deckbrowser`, change `DeckBrowser._renderDeckTree`, `DeckBrowser.refresh` and `DeckBrowser._deckRow`. The former methods are not called.
<!--`aqt.deckbrowser`で､`DeckBrowser._renderDeckTree`､`DeckBrowser.refresh`､`DeckBrowser._deckRow`を変更します｡以前のﾒｿｯﾄﾞは呼び出されません｡-->
* In `Anki.notes`, change `Note.flush`. The new method calls the former one.
<!--`Anki.notes`で､`Note.flush`を変更します｡新しいﾒｿｯﾄﾞは以前のﾒｿｯﾄﾞを呼び出します｡-->
* In `anki.decks` change `DeckManager.save`, calling the former method. Changing `DeckManager.collaps`, not calling the former method.
<!--`anki.decks`で､`DeckManager.save`を変更し､以前のﾒｿｯﾄﾞを呼び出します｡`DeckManager.collaps`を変更し､以前のﾒｿｯﾄﾞを呼び出しません｡-->

## Documentation for developpers
<!--Documentation for developpers-->
See [Documentation.md](Documentation.md)
<!--開発者向けﾄﾞｷｭﾒﾝﾄ
[Documentation.md](Documentation.md)を参照してください｡-->

## Links, licence and credits

Key          |Value
-------------|-------------------------------------------------------------------
Copyright    |Arthur Milchior <arthur@milchior.fr>
Based on     |Anki code by Damien Elmes <anki@ichi2.net>
Based on     |Helen Foster's code, in add-on "Deck_Counts_Now_Later"
Original idea|Juda Kaleta <juda.kaleta@gmail.com>
Somme CSS    |Some idea from cjdduarte
Bug correction|telotortium on Github
Percent bar | Idea and partial realization by Kyle "Khonkhortisan" Mills
License      |GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in    | https://github.com/Arthur-Milchior/anki-enhance-main-window
Addon number | [877182321](https://ankiweb.net/shared/info/877182321)
