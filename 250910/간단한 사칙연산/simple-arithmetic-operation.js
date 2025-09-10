const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]);
let B = Number(input[1]);

console.log(`${A + B}\n${A - B}\n${parseInt(A / B)}\n${A % B}`);