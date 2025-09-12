const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let A = input[0].split(" ").map(String);
let B = input[1].split(" ").map(String);

if((+A[0] >= 19 && A[1] === "M") || (+B[0] >= 19 && B[1] === "M")) {
    console.log(1)
}  else {
    console.log(0)
};