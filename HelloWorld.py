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