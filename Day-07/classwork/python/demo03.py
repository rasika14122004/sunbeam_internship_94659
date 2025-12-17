#set
def function1():
    s1={11,22,33,44,55}
    print(s1)

    for value in s1:
        print(value)

    s1.add(66)

    s1.remove(44)

    print(f"set after={s1}")

# function1()

def function2():
    s1={11,22,33,44}
    s2={44,55,66,77}

    print(f"Union={s1.union(s2)}")

    print(f"Intersection={s1.intersection(s2)}")
function2()