# Configuration of Anki's addon Enhanced Main
<!-- AnkiのｱﾄﾞｵﾝEnhanced Mainの設定 -->

1. We first discuss the various small configurations related to the whole add-on.
<!-- まず､ｱﾄﾞｵﾝ全体に関連するさまざまな小さな設定について説明します｡ -->
1. We then explain how to configure each column.
<!-- 次に､各列の設定方法について説明します｡ -->
1. We then explain how to configure coloring related to empty decks.
<!-- 次に､空のﾃﾞｯｷに関連する色の設定方法について説明します｡ -->
1. We finally explain how to configure coloring related to marked cards.
<!-- 最後に､ﾏｰｸされたｶｰﾄﾞに関連する色の設定方法について説明します｡ -->

## Miscelaneous
<!-- その他 -->
In this section, we describe various small configurations related to the whole add-on.
<!-- このｾｸｼｮﾝでは､ｱﾄﾞｵﾝ全体に関連するさまざまな小さな設定について説明します｡ -->

### Option
<!-- ｵﾌﾟｼｮﾝ -->
Whether you want to display the deck option's name at the end of its line.
<!-- ﾃﾞｯｷｵﾌﾟｼｮﾝの名前をその行の最後に表示するかどうか｡ -->

### cap value
<!-- 上限値 -->
By default, without an add-on, Anki never shows numbers greater than a thousand. Instead, it shows 1000+. You can decide to change the thousand to an arbitrary number, or leave this value to null which always show the real value.
<!-- ﾃﾞﾌｫﾙﾄでは､ｱﾄﾞｵﾝなしでAnkiは1000を超える数字を表示しません｡代わりに1000+と表示されます｡千を任意の数値に変更するか､この値をnullにして常に実際の値を表示するかを決定できます｡ -->

Note that capping to a thousand does not usually make the rendering quicker.
<!-- 千に制限しても､通常はﾚﾝﾀﾞﾘﾝｸﾞが速くなるわけではありません｡ -->

### Dot in number
<!-- 数字の区切り記号 -->
Whether you want a thousand separator for big numbers, such as 34968, to be shown as "34.968" or as "34968".
<!-- 大きな数字（例：34968）に対して千の区切り記号を使用して｢34.968｣と表示するか､｢34968｣と表示するかを選択します｡ -->

### hide values of parent decks
<!-- 親ﾃﾞｯｷの値を非表示にする -->
If a deck has children, its number are not shown.
<!-- ﾃﾞｯｷに子ﾃﾞｯｷがある場合､その数値は表示されません｡ -->

### hide values of parent decks when subdecks are shown
<!-- ｻﾌﾞﾃﾞｯｷが表示されている場合に親ﾃﾞｯｷの値を非表示にする -->
Similar to last option, but it hides number only if the subdecks are shown.
<!-- 前のｵﾌﾟｼｮﾝと似ていますが､ｻﾌﾞﾃﾞｯｷが表示されている場合にのみ数値を非表示にします｡ -->

### color zero
<!-- ｾﾞﾛの色 -->
The color to use for the zero. If it's a string, use always this color. By default in Anki, it's a kind of grey. If you set it to false (default in this add-on), then the zero is not shown at all. You can remove this line or set it to `null` to ensure that the default column is used. To obtain the grey which is the default value in Anki, you can set the color to "#e0e0e0".
<!-- ｾﾞﾛに使用する色です｡文字列の場合は常にこの色を使用します｡Ankiのﾃﾞﾌｫﾙﾄでは､灰色の一種です｡このｱﾄﾞｵﾝのﾃﾞﾌｫﾙﾄではfalseに設定されているため､ｾﾞﾛはまったく表示されません｡この行を削除するか､`null`に設定してﾃﾞﾌｫﾙﾄの列が使用されるようにすることができます｡Ankiのﾃﾞﾌｫﾙﾄ値である灰色を取得するには､色を"#e0e0e0"に設定します｡ -->

## Columns
<!-- 列 -->

Each column should occur after the line "columns" :\[, and before the line with a closing bracket ]. The order of the lines is important, since it's the order in which columns will be displayed by Anki. This means that you can reorder columns in Anki by reordering the lines in the configuration. You can copy a line to display a column multiple times (for example, once using percent, and another time using absolute number).
<!-- 各列は "columns" :[ の行の後､閉じ括弧 ] の行の前に配置する必要があります｡行の順序は重要であり､これはAnkiが列を表示する順序です｡つまり､設定内の行を並べ替えることで､Anki内の列を並べ替えることができます｡行をｺﾋﾟｰして､列を複数回表示することもできます（例えば､一度はﾊﾟｰｾﾝﾄを使用し､もう一度は絶対数を使用するなど）｡ -->

Each column is represented between an opening curly bracket {, and a closing curly bracket }. Each column uses 8 parameters, each represented as a pair.
<!-- 各列は開き中括弧 { と閉じ中括弧 } の間に表されます｡各列は8つのﾊﾟﾗﾒｰﾀを使用し､それぞれがﾍﾟｱとして表されます｡ -->
>>key:value
We'll tell you the meaning of each key, whether you can change its value, and what this change will do.
<!-- 各ｷｰの意味､その値を変更できるかどうか､およびその変更が何をするかを説明します｡ -->

### Name
<!-- 名前 -->
The first value is a description, which will tell you what the column represents. Do NOT alter this value, or the add-on will raise an error.
<!-- 最初の値は列が何を表しているかを示す説明です｡この値を変更しないでください｡変更するとｱﾄﾞｵﾝがｴﾗｰを発生させます｡ -->

### Description
<!-- 説明 -->
A description of the content of the column. This is not used by Anki. It allows you to decide whether you want the column while you edit the configuration.
<!-- 列の内容の説明です｡これはAnkiでは使用されません｡設定を編集する際に列を使用するかどうかを決定するのに役立ちます｡ -->

### Present
<!-- 表示 -->
The value for the key "present" is either true or false. If the value is set to true, the column will be displayed. Otherwise, it will not. Note that you can also delete the entire column from the configuration, instead of changing the value to false.
<!-- "present"ｷｰの値はtrueまたはfalseです｡値がtrueに設定されている場合､列が表示されます｡そうでない場合は表示されません｡値をfalseに変更する代わりに､設定から列全体を削除することもできます｡ -->

If this value is absent, by default, it is assumed that it should be set to true.
<!-- この値が存在しない場合､ﾃﾞﾌｫﾙﾄではtrueに設定されていると見なされます｡ -->

### Header
<!-- ﾍｯﾀﾞｰ -->
The header of the column. If you leave `null` then the default header will be used. This description will be translated as much as it is possible to do it automatically. However, you can also choose to write your own description. You can use HTML in this description. You should use "<br/>" when you want a newline.
<!-- 列のﾍｯﾀﾞｰです｡`null`のままにすると､ﾃﾞﾌｫﾙﾄのﾍｯﾀﾞｰが使用されます｡この説明は可能な限り自動的に翻訳されます｡ただし､自分で説明を書くこともできます｡この説明にはHTMLを使用できます｡改行したい場合は"<br/>"を使用する必要があります｡ -->

### Overlay
<!-- ｵｰﾊﾞｰﾚｲ -->
The text shown when your mouse is over a number. It will describe what this number represents. You can set this key to false if you want no description to be present. And leave this value to `null` if you want to use the default value.
<!-- ﾏｳｽが数値の上にあるときに表示されるﾃｷｽﾄです｡この数値が何を表しているかを説明します｡説明を表示したくない場合は､このｷｰをfalseに設定できます｡ﾃﾞﾌｫﾙﾄ値を使用したい場合は､この値を`null`のままにします｡ -->

### Color
<!-- 色 -->
The color in which the number is written in this column. You can use any color acceptable in an HTML document. Most standard color names should work. `null` means that it should use the same color as in the statistic window, if this color exists, or the default color otherwise.
<!-- この列に数値が書かれる色です｡HTMLﾄﾞｷｭﾒﾝﾄで受け入れられる任意の色を使用できます｡ほとんどの標準的な色名が機能するはずです｡`null`は､統計ｳｨﾝﾄﾞｳにこの色が存在する場合は同じ色を使用し､そうでない場合はﾃﾞﾌｫﾙﾄの色を使用することを意味します｡ -->

### Percent
<!-- ﾊﾟｰｾﾝﾄ -->
true or false whether you want to show the percent of cards satisfying this column condition. For example, 23% of cards are new. Note that sometimes this would not make sense. For example, for the column «cards», the value will always be 100% (unless the deck is empty). For the column notes, the number would not really make any sense (formally, you'd get the percent of cards which is the first of its siblings in this deck).
<!-- この列の条件を満たすｶｰﾄﾞのﾊﾟｰｾﾝﾄを表示するかどうかをtrueまたはfalseで指定します｡例えば､ｶｰﾄﾞの23%が新しいｶｰﾄﾞです｡ただし､場合によっては意味をなさないこともあります｡例えば､｢ｶｰﾄﾞ｣列の場合､値は常に100%になります（ﾃﾞｯｷが空でない限り）｡｢ﾉｰﾄ｣列の場合､その数値は実際には意味をなさないでしょう（形式的には､このﾃﾞｯｷで兄弟の中で最初のｶｰﾄﾞのﾊﾟｰｾﾝﾄを取得します）｡ -->

By default, the percent is assumed to be false if absent.
<!-- ﾃﾞﾌｫﾙﾄでは､ﾊﾟｰｾﾝﾄが存在しない場合はfalseと見なされます｡ -->

### Absolute
<!-- 絶対値 -->
Whether you want an absolute number in your column. That is, a number which is not a percentage, but an exact number.
<!-- 列に絶対数を表示するかどうかを指定します｡つまり､ﾊﾟｰｾﾝﾃｰｼﾞではなく､正確な数値です｡ -->

By default, this value is false if Percent is set to true, otherwise its default value is true.
<!-- ﾃﾞﾌｫﾙﾄでは､Percentがtrueに設定されている場合､この値はfalseです｡それ以外の場合､ﾃﾞﾌｫﾙﾄ値はtrueです｡ -->

### Subdecks
<!-- ｻﾌﾞﾃﾞｯｷ -->
When you consider a deck which has subdecks, a true value considers cards in its subdecks; a false value ignores cards in its child subdecks.
<!-- ｻﾌﾞﾃﾞｯｷを持つﾃﾞｯｷを考慮する場合､trueの値はｻﾌﾞﾃﾞｯｷ内のｶｰﾄﾞを考慮し､falseの値は子ｻﾌﾞﾃﾞｯｷ内のｶｰﾄﾞを無視します｡ -->

## Coloring decks
<!-- ﾃﾞｯｷの色付け -->
The author of this add-on wants to know when a deck is empty. This is very important to him, because he wants to add new cards in them as soon as possible. Thus, this add-on changes the color of the names of empty decks, and of the names of decks with an empty descendant.
<!-- このｱﾄﾞｵﾝの作者は､ﾃﾞｯｷが空であることを知りたいと考えています｡これは彼にとって非常に重要であり､できるだけ早く新しいｶｰﾄﾞを追加したいからです｡したがって､このｱﾄﾞｵﾝは空のﾃﾞｯｷの名前と､空の子孫を持つﾃﾞｯｷの名前の色を変更します｡ -->

The author also wants to know which deck has marked cards. Thus, the background of the deck's name having marked cards changes color.
<!-- 作者はどのﾃﾞｯｷにﾏｰｸされたｶｰﾄﾞがあるかも知りたいと考えています｡そのため､ﾏｰｸされたｶｰﾄﾞを持つﾃﾞｯｷの名前の背景色が変わります｡ -->

Both of these configurations can be changed as explained in this section. In particular, you can turn one or both of these options off by setting "color empty" and "color marked" to false.
<!-- これらの設定は､このｾｸｼｮﾝで説明されているように変更できます｡特に､｢color empty｣と｢color marked｣をfalseに設定することで､これらのｵﾌﾟｼｮﾝの一方または両方をｵﾌにすることができます｡ -->

### Choice of color
<!-- 色の選択 -->
#### Color empty
<!-- 空の色 -->
The color of the names of decks without new cards
<!-- 新しいｶｰﾄﾞがないﾃﾞｯｷの名前の色 -->

#### Color empty descendant
<!-- 空の子孫の色 -->
The color of the names of decks with a descendant without new cards
<!-- 新しいｶｰﾄﾞがない子孫を持つﾃﾞｯｷの名前の色 -->

#### Default color
<!-- ﾃﾞﾌｫﾙﾄの色 -->
The color of a deck which every descendant has new cards.
<!-- すべての子孫が新しいｶｰﾄﾞを持つﾃﾞｯｷの色 -->

#### Default column color
<!-- ﾃﾞﾌｫﾙﾄの列の色 -->
The color of the content of a deck, if no other color is specified.
<!-- 他の色が指定されていない場合のﾃﾞｯｷの内容の色 -->

#### ended marked background color
<!-- 終了したﾏｰｸ付きﾃﾞｯｷの背景色 -->
The color of the decks which have an ended deck with marked cards. The notion of ended deck will be explained in the next section of this documentation.
<!-- ﾏｰｸされたｶｰﾄﾞを持つ終了したﾃﾞｯｷの色｡終了したﾃﾞｯｷの概念は､このﾄﾞｷｭﾒﾝﾄの次のｾｸｼｮﾝで説明されます｡ -->

#### Marked background color
<!-- ﾏｰｸ付きﾃﾞｯｷの背景色 -->
The color of decks who have marked cards but none of its descendants are both ended and have marked cards.
<!-- ﾏｰｸされたｶｰﾄﾞを持つが､その子孫のいずれも終了しておらず､ﾏｰｸされたｶｰﾄﾞを持たないﾃﾞｯｷの色｡ -->

### Deck modifier
<!-- ﾃﾞｯｷ修飾子 -->
A deck modifier is a symbol (or a word, etc.) whose presence in a deck name changes the meaning of the deck. When the meaning is changed, the coloration is also changed. It's not clear to the author of this add-on whether anyone apart from himself will need those, but if you want to use them, here is the explanation.
<!-- ﾃﾞｯｷ修飾子は､ﾃﾞｯｷ名に存在することでﾃﾞｯｷの意味を変更する記号（または単語など）です｡意味が変更されると､色付けも変更されます｡このｱﾄﾞｵﾝの作者以外にこれを必要とする人がいるかどうかは不明ですが､使用したい場合は以下の説明を参照してください｡ -->

The first three symbols currently have the same effect, but one day this effect may change, according to what the author wants to do.
<!-- 最初の3つの記号は現在同じ効果を持っていますが､作者の意図により将来的にこの効果が変更される可能性があります｡ -->

#### End symbol
<!-- 終了記号 -->
By default, this symbol is ";". It means that the deck is definitively done, and no new card may ever be added to it. When a deck has this symbol, neither itself nor its descendants will ever be colored.
<!-- ﾃﾞﾌｫﾙﾄでは､この記号は｢;｣です｡これはﾃﾞｯｷが完全に終了し､新しいｶｰﾄﾞが追加されることはないことを意味します｡この記号があるﾃﾞｯｷは､それ自体もその子孫も色付けされることはありません｡ -->

#### Given up symbol
<!-- 放棄記号 -->
By default, this symbol is "/". To the author, it means that no new card will be added because this deck is either too hard, or not interesting enough.
<!-- ﾃﾞﾌｫﾙﾄでは､この記号は｢/｣です｡作者にとって､これはこのﾃﾞｯｷが難しすぎるか､十分に興味深くないため､新しいｶｰﾄﾞが追加されないことを意味します｡ -->

#### Pause symbol
<!-- 一時停止記号 -->
By default, this symbol is "=". To the author, it means that more new cards will be added later, but right now it does not want Anki to change the color of the deck's name. In a future version, there may be an option to change the color of these decks.
<!-- ﾃﾞﾌｫﾙﾄでは､この記号は｢=｣です｡作者にとって､これは後で新しいｶｰﾄﾞが追加されるが､今はAnkiにﾃﾞｯｷ名の色を変更してほしくないことを意味します｡将来のﾊﾞｰｼﾞｮﾝでは､これらのﾃﾞｯｷの色を変更するｵﾌﾟｼｮﾝが追加されるかもしれません｡ -->
