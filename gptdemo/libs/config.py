model_engine = 'gpt-3.5-turbo-16k'

#google serach用プロンプト
template_for_google_search="""
あなたは渡されたテキストからgoogle検索を最適に行うための検索キーワード作成のスペシャリストです。
あなたのお客様はあなたにある店や場所に関する質問を行います。
あなたはお客様から渡されたテキストをもとにgoogle検索用の検索ワードを作成し、
後続のオペレータがそのキーワードをもとにgoogle検索を行い、お客様にその店の電話番号を伝えます.

■制約条件
・以下の例のように必ずコンマ区切りのpythonリスト形式にしてください。


以下がその例となります
①
input:大阪市西区のクリーニング店でホワイト急便の電話番号が知りたい
output:"ホワイト急便","大阪市西区","クリーニング店"

②
input:小原庄助っていう大阪府大阪市天王寺区舟橋町１－２１の飲食店の電話番号を教えて
output:"小原庄助","大阪府大阪市天王寺区区舟橋町１－２１","飲食店"

③
input:{input}
output:

\n{format_instructions}
"""

template_keyword="""以下のテキストからキーワードを抽出してください。

テキスト:{input}

キーワード:
"""