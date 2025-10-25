const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);

let sum = 0;
let cnt = 0;

for (let i = A; i <= B; i++) {
    if (i % 5 == 0 || i % 7 == 0) {
        sum += i;
        cnt++;
    }
}

console.log(sum, (sum / cnt).toFixed(1));