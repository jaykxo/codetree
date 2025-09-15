const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");
let p1 = input[0].split(" ");
let p2 = input[1].split(" ");
let p3 = input[2].split(" ");

let A = 0;

if (p1[0] === "Y" && Number(p1[1]) >= 37) A += 1;
if (p2[0] === "Y" && Number(p2[1]) >= 37) A += 1;
if (p3[0] === "Y" && Number(p3[1]) >= 37) A += 1;

console.log(A >= 2 ? "E" : "N")