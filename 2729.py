n = 100
str1 = str(n) + str(n*2) + str(n*3)
li = ['1','2','3','4','5','6','7','8','9']

str2 = list(str1)
str2.sort()

if str2 == li:
    return True
else:
    return False
