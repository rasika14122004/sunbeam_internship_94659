#from Pkg.mod1 import fun1
#from Pkg.mod1 import fun2
#fun1()
#fun2()

from pkg2.mymath1 import sum

num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))

add = sum(num1,num2)

print(f"Addition = {add}")