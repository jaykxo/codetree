const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);

let prod = 1;

for (let i = A; i <= B; i++) {
    prod *= i
}

console.log(prod);