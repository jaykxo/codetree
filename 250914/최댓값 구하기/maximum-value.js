const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let [a, b, c] = input.map(Number);

console.log(Math.max(a, b, c));