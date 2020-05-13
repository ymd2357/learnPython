# coding:UTF-8

# print ("Hello, Python")
text = "Hello, Python!"
print (text)

textJ = "こんにちは"
print (textJ)

text2 = "It's show time!"
print (text2)

text3 = 'using "double quote"'
print (text3)

text4 = "例えば、\n改行が必要ならこうすると良い。"
print (text4)

text5 = "ダブルコーテーションの間でも、\
\\でエスケープすれば\"が使える。"
print (text5)

longtext = """エスケープシーケンスを使用する他に、
三連引用符を使えば、
簡単に改行付きの文字列が作れる。"""

print (longtext)

addtext1 = "ABC"
addtext2 = "def"
addtext = addtext1 + addtext2
print (addtext)

repttext = "ab"
print (repttext * 3)

counttext = "1234567890123456789"
print (len(counttext))

print (counttext[3] + counttext[-2]) # 先頭3番目と後ろから2番目

print (counttext[3:5]) # 先頭3番目〜5番目の前＝45

print (counttext[3:11:2]) # 先頭3番目〜11番目の前を１つ飛ばし＝4680

number = 65535

print ("%6dの16進数表記は%5xです。"%(number,number))

print ("[%5d]"%(123))  # 右詰め５桁
print ("[%05d]"%(123)) # 0埋め５桁
print ("[%+5d]"%(123)) # 右詰めsign付き５桁
print ("[%-5d]"%(123)) # 左詰め５桁
