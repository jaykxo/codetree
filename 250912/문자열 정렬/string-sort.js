const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
let s = input[0].split("");  

s.sort();                     
console.log(s.join(""));