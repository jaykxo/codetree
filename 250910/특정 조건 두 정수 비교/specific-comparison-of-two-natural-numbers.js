const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]), B = Number(input[1]);
let result1;
let result2;

if (A < B) {
    result1 = 1
} else {
    result1 = 0
};
if (A == B) {
    result2 = 1
} else {
    result2 = 0
};

console.log(result1, result2);