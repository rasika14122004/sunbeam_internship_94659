let marks = [35, 67, 82, 49, 90, 58];
  


let passedStudents = marks.filter(mark => mark >= 50);
console.log("Passed Students Marks:", passedStudents);


let percentageMarks = marks.map(mark => mark + "%");
console.log("Percentage Marks:", percentageMarks);


let above85 = marks.some(mark => mark > 85);

if (above85) {
    console.log("At least one student scored above 85");
} else {
    console.log("No student scored above 85");
}
