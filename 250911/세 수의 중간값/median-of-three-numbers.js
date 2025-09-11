const fs = require("fs");
let input = fs.readFileSync(0).toString().split(" ").map(Number);

let [A, B, C] = input;

console.log(B > A && B < C ? 1 : 0);