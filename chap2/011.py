# coding:utf-8, python3
'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

'''
hightemp.txtはutf-8
入門Python3 p220 8.1.2参照
'''

f = open("hightemp.txt", "rt")
ans = f.read()
print(ans.replace("\t", " "))
f.close()
