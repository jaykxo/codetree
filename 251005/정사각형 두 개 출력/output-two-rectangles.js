const fs = require("fs");
let N = Number(fs.readFileSync(0).toString().trim());

let result = "";

for (let i = 1; i <= N; i++) {
    result += "*".repeat(N) + "\n";
}

console.log(result + "\n" + result);