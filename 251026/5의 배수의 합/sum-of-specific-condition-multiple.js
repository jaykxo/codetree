const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);

let sum = 0;

if (A >= B) {
    for (i = B; i <= A; i++) {
        if (i % 5 == 0) {
            sum += i;
        }
    }
} else {
    for (i = A; i <= B; i++) {
        if (i % 5 == 0) {
            sum += i;
        }
    }
}

console.log(sum);