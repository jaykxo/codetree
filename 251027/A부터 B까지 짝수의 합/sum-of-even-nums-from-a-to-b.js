const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);
let sum = 0;

for (let i = A; i <= B; i++) {
    if (i % 2 == 0) {
        sum += i
    }
}

console.log(sum);