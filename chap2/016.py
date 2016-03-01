# -*- coding: utf-8 -*-
'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''

import sys

with open(sys.argv[1], "rt", encoding = "utf_8") as f:
    lines = f.readlines()

N = int(sys.argv[2])
if(len(lines)%N != 0):
    print("invalid number")
    sys.exit()
else:
    for i in range(int(len(lines)/N)):
        with open("exercise016_" + str(i+1) + ".txt", "w", encoding = "utf_8") as f:
            f.write("".join(lines[N*i:N*(i+1)]))

