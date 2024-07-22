name1 = input("Enter first name : ")
name2 = input("Enter second name : ")

var = name1 + name2
var2 = var.replace(" " , "")
print(var2)

exstr = "123321"
ls = []

for i in range(0,len(exstr)):
    ls.append(exstr[i])
print("\n",ls,"\n")

ls = [int(x) for x in ls]
print(ls,"\n")
l = len(ls)

sum = 0
for num in range(l):
    if num % 2 == 0 :
        sum += ls[num + 1]
    else:
        sum += ls[num - 1]
print(sum)
