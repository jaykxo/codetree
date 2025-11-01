const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n").map(Number);

let N = input[0];
let sum = 0;

for (let i = 1; i <= N; i++) {
    sum += input[i];
}

console.log(sum, (sum / N).toFixed(1));