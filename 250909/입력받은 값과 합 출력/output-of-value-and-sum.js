const fs = require("fs");

let N = fs.readFileSync(0).toString().split(" ");

let A = Number(N[0]);
let B = Number(N[1]);

console.log(A, B, A + B)