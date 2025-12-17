// Create student object
let student = {
    studentId: 101,
    fullName: "Ravi Patil",
    email: "ravi@gmail.com",
    course: "Web Development",
    marks: [78, 85, 90, 88]
};


let jsonString = JSON.stringify(student);
console.log("JSON String:");
console.log(jsonString);


let studentObject = JSON.parse(jsonString);
console.log("JavaScript Object:");
console.log(studentObject);
