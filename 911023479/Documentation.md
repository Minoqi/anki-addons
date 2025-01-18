This file explains how this add-on works.

<!-- このﾌｧｲﾙは､このｱﾄﾞｵﾝの動作を説明します｡ -->

# Files
<!-- ﾌｧｲﾙ -->

## ChangeFunction
<!-- ChangeFunction -->
This file is in charge of monkey-patching each function which must be
monkey patched.
<!-- このﾌｧｲﾙは､ﾓﾝｷｰﾊﾟｯﾁを必要とする各関数にﾓﾝｷｰﾊﾟｯﾁを適用する役割を担っています｡ -->

## Config
<!-- Config -->
This file is in charge of reading user's configuration. It is also updated
if an outdated configuration file is found.
<!-- このﾌｧｲﾙは､ﾕｰｻﾞｰの設定を読み取る役割を担っています｡古い設定ﾌｧｲﾙが見つかった場合も更新されます｡ -->

## Debug
<!-- Debug -->
Function which helps debugging. Normally, mayDebug and shouldDebug
must be False in the code distributed, and thus no debugging occurs.
<!-- ﾃﾞﾊﾞｯｸﾞを支援する関数です｡通常､配布されるｺｰﾄﾞではmayDebugとshouldDebugはFalseに設定されているため､ﾃﾞﾊﾞｯｸﾞは行われません｡ -->

## Html
<!-- Html -->
Contains all of the HTML which is used to generate the list of decks in
the main window. The HTML is either contained in a string variable if
it does not change, or in a small function which takes a parameter and
returns the HTML string.
<!-- ﾒｲﾝｳｨﾝﾄﾞｳでﾃﾞｯｷのﾘｽﾄを生成するために使用されるすべてのHTMLが含まれています｡HTMLは変更されない場合は文字列変数に含まれ､ﾊﾟﾗﾒｰﾀを受け取りHTML文字列を返す小さな関数に含まれます｡ -->

## Strings
<!-- Strings -->
This associates to each column some strings describing it: a short one
used in the header of the column, and a longer one used in the overlay
describing the number.
<!-- 各列に関連する文字列を関連付けます｡列のﾍｯﾀﾞｰで使用される短いものと､数値を説明するｵｰﾊﾞｰﾚｲで使用される長いものがあります｡ -->

## Tree
<!-- Tree -->
Contains functions used to compute global information, e.g. how
many cards there are of each kind in each deck (not considering the
subdeck), and how much time to wait before the next review.
<!-- ｸﾞﾛｰﾊﾞﾙ情報を計算するために使用される関数が含まれています｡例えば､各ﾃﾞｯｷにどの種類のｶｰﾄﾞが何枚あるか（ｻﾌﾞﾃﾞｯｷを考慮しない）､次のﾚﾋﾞｭｰまでの待ち時間などです｡ -->

It's computed globally because it allows a single query instead
of having to do one query per deck.
<!-- これは､ﾃﾞｯｷごとに1つのｸｴﾘを実行する代わりに､単一のｸｴﾘを実行できるため､ｸﾞﾛｰﾊﾞﾙに計算されます｡ -->

## Node
<!-- Node -->
Globally, it contains everything else. It contains each computation
which must be done recursively on a deck by deck basis, and the
function to print each deck.
<!-- ｸﾞﾛｰﾊﾞﾙに見て､それ以外のすべてが含まれています｡ﾃﾞｯｷごとに再帰的に行う必要がある各計算と､各ﾃﾞｯｷを印刷する関数が含まれています｡ -->
