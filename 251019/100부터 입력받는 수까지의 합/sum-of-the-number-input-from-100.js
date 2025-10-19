const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

let sum = 0;

for (let i = N; i <= 100; i++) {
    sum += i
}

console.log(sum);