# coding:utf-8, python3
'''
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」
のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，
hightemp.txtを入力ファイルとして実行せよ．
さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

'''
hightemp.txtはutf-8
入門Python3 p220 8.1.2参照
'''

f = open("hightemp.txt", "rt")
ans = f.readlines()
print(len(ans))
f.close()
