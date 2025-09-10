const fs = require("fs");
let score = Number(fs.readFileSync(0).toString());

let grade = score === 100 ? "pass" : "failure";

console.log(grade);