const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B] = input;
let sum = 0;

for (let i = A; i <= B; i++) {
    sum += i
}

console.log(sum)