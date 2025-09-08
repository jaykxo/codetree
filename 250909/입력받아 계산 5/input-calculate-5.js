const fs = require("fs");

let N = fs.readFileSync(0).toString().split(" ");

let a = Number(N[0]);
let b = Number(N[1]);

console.log(a + b);