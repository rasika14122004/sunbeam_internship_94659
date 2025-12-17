def function1():
    import mymath

    num1= int(input("Enter num1: "))

    num2=int(input("Enter num2: "))

    add= mymath.sum(num1,num2)

    print(f"Addition ={add}")

#function1()

def function2():
    import mymath as m

    num1= int(input("Enter num1:"))
    num1= int(input("Enter num1:"))
    add= m.sum(num1,num2)

    print(f"Addition={add}")

    #function2()
def function3():
    from mymath import div
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))

    division =div(num1,num2)

    print(f"Division={division}")
    

#function3()
def function4():
   from mymath import div as d
num1=int(input("Enter num1: "))
num1=int(input("Enter num2: "))
division = div(num1,num2)

print(f"Division = {division}")

function4()
    