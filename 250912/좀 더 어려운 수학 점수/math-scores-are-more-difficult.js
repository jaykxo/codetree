const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let A = input[0].split(" ").map(Number);
let B = input[1].split(" ").map(Number);

if(A[0] === B[0]) {
    console.log(A[1] > B[1] ? "A" : "B")
};

if(A[0] != B[0]) {
    console.log(A[0] > B[0] ? "A" : "B")
};