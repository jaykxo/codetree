const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

let w = Number(input[0]);
let h = Number(input[1]);

w += 8;
h *= 3;

console.log(w);
console.log(h);
console.log(w * h);