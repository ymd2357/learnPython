abc1 = "".join(["Apple", "Banana", "Citrus"])

abc2 = ",".join(["Andy", "Bill", "Cody"])

print(abc1)
print(abc2)
print("\n")

print(abc2.lower())
print(abc2.upper())
print(abc2.capitalize())
print(abc2.upper().title())
print(abc2.swapcase())
print("\n")

print(abc2.upper().islower())
print(abc2.upper().isupper())
print(abc2.istitle())
print(abc2.lower().istitle())
print("\n")

print("123 is decimal?:") 
print("123".isdecimal())
print("123 is digit?:") 
print("123".isdigit())
print("123 is numeric?:") 
print("123".isnumeric())

print("① is decimal?:") 
print("①".isdecimal())
print("① is digit?:") 
print("①".isdigit())
print("① is numeric?:") 
print("①".isnumeric())

print("拾伍 is decimal?:") 
print("拾伍".isdecimal())
print("拾伍 is digit?:") 
print("拾伍".isdigit())
print("拾伍 is numeric?:") 
print("拾伍".isnumeric())

print("\n")

print("42.195km is alpha?")
print("42.195km".isalpha())
print("42.195km is alpha or num?")
print("42.195km".isalnum())
print("42.195km is ascii?")
print("42.195km".isascii())

print("\n")

text = "abcabcabc"
print(text.find("ab"))
print(text.find("ab",2))
print(text.find("ab",2,4))

print(text.index("ab"))
print(text.index("ab",2))
#print(text.index("ab",2,4)) #ValueError

print(text.rfind("ab"))
print(text.rfind("ab",3))
print(text.rfind("ab",3,5))
