# coding:utf-8, python3
'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.
txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
'''

'''
hightemp.txtはutf-8
入門Python3 p220 8.1.2参照
'''

f = open("hightemp.txt", "rt")
ans = f.read()
print(ans.replace("\t", " "))
f.close()
