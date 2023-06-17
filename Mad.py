txt = ""

mystr = "123321"

for i in range(3):

    txt += mystr[i]

    txt += mystr[5 - i]

print(txt)

