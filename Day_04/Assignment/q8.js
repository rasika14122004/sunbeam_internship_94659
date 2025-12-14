function calculateArea(radius = 1) {
  return Math.PI * radius * radius;
}

// Example usage
console.log(calculateArea());    // Uses default radius = 1
console.log(calculateArea(5));   // Uses radius = 5
