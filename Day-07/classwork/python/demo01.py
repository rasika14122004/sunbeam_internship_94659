#List - Array

def function1():
    l1 = [11, 22, 33, 44, 55]

    print(l1)

    print(f"Array Before = {l1}")

    for value in l1:
        print(value)

    l1.append(66)

    l1.insert(2,28)

    l1.pop()

    l1.remove(22)

    print(f"Array After = {l1}")


# function1()

def function2():
    student = [2202, "Ram", 10, 98]

    print(f"Student Roll num = {student[0]}, Student Name = {student[1]}, Std = {student[2]}, Marks out of 100 = {student[3]}")

function2()