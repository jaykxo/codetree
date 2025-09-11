const fs = require("fs");

let input = fs.readFileSync(0).toString().split(" ").map(Number);

let [a, b, c] = input;

console.log(Math.min(a, b, c));