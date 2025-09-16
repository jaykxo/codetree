const fs = require("fs");
let N = Number(fs.readFileSync(0).toString())
let result = "";

for (let i = N; i >= 1; i--) {
    result += (i + " ");
}

console.log(result);