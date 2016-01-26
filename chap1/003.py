# coding:utf-8, python3
'''
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''

'''
入門Python3 p54 3.2参照
'''

str = "Now I need a drink, alcoholic of course, after the heavy" +\
      "lectures involving quantum mechanics."
str = str.replace(",", "")
str = str.replace(".", "")
str = str.split()

ans = []
for word in str:
    ans.append((len(word)))
print(ans)
