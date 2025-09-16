const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B] = input;
let result = "";

for (let i = A; i <= B; i += 2) {
    result += (i + " ");
}

console.log(result);