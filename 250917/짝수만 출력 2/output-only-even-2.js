const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [B, A] = input;
result = "";

while (B >= A) {
    result += (B + " ");
    B -= 2;
}

console.log(result);