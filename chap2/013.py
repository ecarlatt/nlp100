# coding:utf-8, python3
'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
'''

f = open("hightemp.txt", "rt")
ans = f.read()
print(ans.replace("\t", " "))
f.close()