#list of dictionaries

students=[

    {'rollno':1,'name':"abc",'std':4,'marks':98.0},
    {'rollno':2, 'name':"xyz", 'std':5, 'marks':89.0},
    {'rollno':3, 'name':"pqr", 'std':6, 'marks':80.0}
    ]
for value in students:
    print(f"roll num={value["rollno"]},Name={value["name"]}")