const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let A = input[0].split(" ").map(Number);
let B = input[1].split(" ").map(Number);

if(A[1] === "W" && B[1] === "W") {
    console.log(0)
} else if (A[0] < 19 && B[0] < 19) {
    console.log(0)
} else {
    console.log(1)
};