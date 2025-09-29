const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let N = input[0];

for (let i = 1; i <= N; i++) {
    let num = input[i]
    if (num % 2 === 1 && num % 3 === 0) {
        console.log(num)
    }
}