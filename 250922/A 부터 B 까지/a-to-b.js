const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);

let result = "";
let i = A;

while (i <= B) {
    result += (i + " ");
    if (i % 2 === 1) {
        i *= 2
    } else {
        i += 3
    }
};

console.log(result);