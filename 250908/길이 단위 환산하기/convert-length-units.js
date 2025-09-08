const fs = require("fs");

let N = Number(fs.readFileSync(0).toString());
let ft = 30.48;

console.log((N * ft).toFixed(1));

