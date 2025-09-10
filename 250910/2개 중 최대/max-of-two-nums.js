const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]), B = Number(input[1]);

let max = A > B ? A : B

console.log(max);