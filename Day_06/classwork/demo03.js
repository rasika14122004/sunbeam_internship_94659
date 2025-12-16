//constructor function
function Student(name,age){
  this.name = name
  this.age =age
}

const s1 = new Student()
console.log(typeof (s1))
console.log(s1)

const s2 = new Student ("riya",22)
console.log(s2)

const s3= new Student("diya",33)
s3.mobile ="2323221223"
s3["email id"]='diya@gmail.com'
console.log(s3)
