const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());
let M = (N - 80) * -1

if (N >= 80) {
    console.log("pass");
} else {
    console.log(`${M} more score`);
};