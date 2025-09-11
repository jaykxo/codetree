const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let A = Number(input[0]);
let rest = input[1].split(" ").map(Number);
let [B, C, D, E] = rest;
 
console.log(A > B ? 1 : 0);
console.log(A > C ? 1 : 0);
console.log(A > D ? 1 : 0);
console.log(A > E ? 1 : 0);