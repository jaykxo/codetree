const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);

let prod = 1;

for (let i = 1; i <= B; i++) {
    if (i % A == 0) {
        prod *= i
    }
}

console.log(prod);