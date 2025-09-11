const fs = require("fs");
let A = Number(fs.readFileSync(0).toString());

console.log(A % 3 === 0 || A % 5 === 0 ? 1 : 0);