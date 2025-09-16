const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [B, A] = input;
let result = "";

for (let i = B; i >= A; i-=2) {
    result += (i + " ");
}

console.log(result);