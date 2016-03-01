
* 問題0


```python
a = 'stressed'
print(a[::-1])
```

    desserts
    

* 問題1


```python
b = 'パタトクカシーー'
print(b[::2])
```

    パトカー
    

* 問題2


```python
c = "パトカー"; d="タクシー"; e=''
for char1, char2 in zip(c,d):
    e = e+ char1 + char2
print(e)
```

    パタトクカシーー
    

* 問題3


```python
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(",","")
str  = str.replace(".","")
str = str.split()

ans = []
for word in str:
    ans.append((len(word)))
print(ans)
```

    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    

* 問題4


```python
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace(",","")
str  = str.replace(".","")
str = str.split()

ans = {}
for i in str:
    if str.index(i) + 1 in [1,5,6,7,8,9,15,16,19]:
        ans[i[:1]] = str.index(i) + 1
    else:
        ans[i[:2]] = str.index(i) + 1
print(ans)
```

    {'He': 2, 'S': 16, 'P': 15, 'F': 9, 'K': 19, 'Cl': 17, 'Ar': 18, 'Li': 3, 'H': 1, 'Ca': 20, 'Be': 4, 'B': 5, 'N': 7, 'O': 8, 'Mi': 12, 'Al': 13, 'Ne': 10, 'Na': 11, 'Si': 14, 'C': 6}
    

* 問題5


```python
def ngram(data, n):
    return [data[i: i+n] for i in range(len(data)-1)]

a = 'I am an NLPer'
print(ngram(a.split(), 2))
print(ngram(a, 2))
```

    [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
    

* 問題6


```python
dise = "paraparaparadise"; graph = "paragraph"
X = set(ngram(dise, 2)); Y = set(ngram(graph,2))
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
```

    {'gr', 'pa', 'ap', 'di', 'se', 'ph', 'ag', 'is', 'ad', 'ra', 'ar'}
    {'ar', 'ap', 'pa', 'ra'}
    {'se', 'ad', 'di', 'is'}
    


```python
print('se' in X)
print('se' in Y)
```

    True
    False
    

* 問題7


```python
def xyz(x,y,z):
    print("{0}時の{1}は{2}".format(x,y,z))
x = 12
y = "気温"
z=22.4
xyz(x, y, z)
```

    12時の気温は22.4
    

* 問題8


```python
test = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
def cipher(input):
    output = ""
    for char in input:
        if char.islower():
            output += chr(219-ord(char))
        else:
            output += char
    return output

print(cipher(test))
print(cipher(cipher(test)))
```

    Hr Hv Lrvw Bvxzfhv Blilm Clfow Nlg Ocrwrav Foflirmv. Nvd Nzgrlmh Mrtsg Aohl Srtm Pvzxv Svxfirgb Cozfhv. Aigsfi Krmt Czm.
    Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.
    


```python
test = 'パタトクカシーー'
print(cipher(test))
print(cipher(cipher(test)))
```

    パタトクカシーー
    パタトクカシーー
    

* 問題9


```python
import random
test = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
test = test.split()
ran = []
for word in test:
    if len(word) > 4:
        char = list(word)
        mid = char[1:-1]
        random.shuffle(mid)
        word =  char[0] + "".join(mid) + char[-1]
    ran.append(word)
print(" ".join(ran))
```

    I cudol'nt bveeile that I could acltlauy uetnanrsdd what I was raideng : the phmenoaenl poewr of the human mind .
    
