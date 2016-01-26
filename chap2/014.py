# coding:utf-8, python3
'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
'''

import sys
with open(sys.argv[1], "rt",) as f:
    lines = f.readlines()
for line in lines[0:int(sys.argv[2])]:
    print(line.strip("\n"))
