# coding:utf-8, python3
'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''

'''
入門Python3 p102 4.5.4参照
'''

c = "パトカー"; d = "タクシー"; e =""
for char1, char2 in zip(c, d):
    e = e + char1 + char2
print(e)
