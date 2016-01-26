
サマリー(という名のコードを書きなぐった跡)
jupyter上だとencoding="utf-8"を入れとかないとエラーを吐かれる...


```python
#問題10
f = open("hightemp.txt", "rt", encoding="utf-8")
ans = f.readlines()
print(len(ans))
f.close()
```

    24
    


```python
#open~close ⇔ with open as
with open("hightemp.txt", "rt", encoding="utf-8") as f:
    print(len(f.readlines()))
```

    24
    


```python
#問題11
with open("hightemp.txt", "rt", encoding="utf-8") as f:
    ans = f.read()
    print(ans.replace("\t", " "))
```

    高知県 江川崎 41 2013-08-12
    埼玉県 熊谷 40.9 2007-08-16
    岐阜県 多治見 40.9 2007-08-16
    山形県 山形 40.8 1933-07-25
    山梨県 甲府 40.7 2013-08-10
    和歌山県 かつらぎ 40.6 1994-08-08
    静岡県 天竜 40.6 1994-08-04
    山梨県 勝沼 40.5 2013-08-10
    埼玉県 越谷 40.4 2007-08-16
    群馬県 館林 40.3 2007-08-16
    群馬県 上里見 40.3 1998-07-04
    愛知県 愛西 40.3 1994-08-05
    千葉県 牛久 40.2 2004-07-20
    静岡県 佐久間 40.2 2001-07-24
    愛媛県 宇和島 40.2 1927-07-22
    山形県 酒田 40.1 1978-08-03
    岐阜県 美濃 40 2007-08-16
    群馬県 前橋 40 2001-07-24
    千葉県 茂原 39.9 2013-08-11
    埼玉県 鳩山 39.9 1997-07-05
    大阪府 豊中 39.9 1994-08-08
    山梨県 大月 39.9 1990-07-19
    山形県 鶴岡 39.9 1978-08-03
    愛知県 名古屋 39.9 1942-08-02
    
    


```python
with open("hightemp.txt", "rt", encoding = "utf-8") as f:
    ans = f.readlines()
    print(len(ans))
```

    24
    


```python
#問題12
#(間に挟む文字).join(list) -> list to str
with open("hightemp.txt", "rt", encoding = "utf-8") as f, open("col1.txt", "w", encoding = "utf-8") as f2, open("col2.txt", "w", encoding = "utf-8") as f3:
    ans = f.readlines()
    for i in range(0, len(ans)):
        ans[i] = ans[i].replace("\t", " ")
        ans[i] = ans[i].split()
    col1 = []
    col2 = []
    for i in range(0, len(ans)):
        col1.append(ans[i][0])
        col2.append(ans[i][1])
    f2.write("\n".join(col1))
    f3.write("\n".join(col2))
```


```python
#問題13
with open("col1.txt", "rt", encoding = "utf-8") as f1, open("col2.txt", "rt", encoding = "utf-8") as f2, open("col3.txt", "w", encoding = "utf-8") as f3:
    col1 = f1.readlines()
    for i in range(0, len(col1)):
        f3.write(col1[i].strip("\n")+"\t" +col2[i])
```


```python
#問題13α(リスト内包表記)
with open("col1.txt", "rt", encoding = "utf-8") as f1, open("col2.txt", "rt", encoding = "utf-8") as f2, open("col3.txt", "w", encoding = "utf-8") as f3:
    f3.write("".join([c1.strip("\n")+"\t"+c2 for c1,c2 in zip(f1,f2)]))
```


```python
#問題14
import sys
with open(sys.argv[1], "rt") as f:
    lines = f.readlines()
for line in lines[0:int(sys.argv[2])]:
    print(line.strip("\n"))
```


```python
#問題15
import sys
with open(sys.argv[1], "rt") as f:
    lines = f.readlines()
for line in lines[len(lines) - int(sys.argv[2]):]:
    print(line.strip("\n"))
```
