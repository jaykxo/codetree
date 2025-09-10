const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

console.log(N ** 2);
if (N < 5) {
    console.log("tiny");
};