const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]), B = Number(input[1]), C = Number(input[2]);

console.log(A + B + C);
console.log((A + B + C)/3);
console.log((A + B + C) - (A + B + C)/3)