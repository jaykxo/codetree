const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

console.log(
    (N % 2 === 1 && N % 3 === 0) || 
    (N % 2 === 0 && N % 5 === 0) 
    ? "true" : "false"
)