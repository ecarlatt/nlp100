# coding:utf-8, python3
'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''

import sys
with open(sys.argv[1], "rt") as f:
    lines = f.readlines()
for line in lines[len(lines) - int(sys.argv[2]):]:
    print(line.strip("\n"))
