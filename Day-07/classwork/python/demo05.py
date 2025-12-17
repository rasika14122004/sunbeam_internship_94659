#list of list
def function1():
    l1=[[11,22,33],[44,55,66],[77,88,99]]
    print(l1)

    for value in l1:
        print(value)

    print(f"2nd value={l1[1][0]}")   
    l1.append([100,101,102])
    l1.pop()
    l1.remove([44,55,66])
    print(l1)

function1()
