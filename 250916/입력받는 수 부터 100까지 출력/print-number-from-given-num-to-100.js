const fs = require("fs");
let n = Number(fs.readFileSync(0).toString());

let result = "";

for (i = n; i <= 100; i++) {
    result += (i + " ")
};

console.log(result);