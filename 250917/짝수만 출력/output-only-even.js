const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B] = input;
let result = "";

while (A <= B) {
    result += (A + " ");
    A += 2;
}

console.log(result);