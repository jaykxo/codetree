const fs = require("fs");
let letter = fs.readFileSync(0).toString().trim();

let result = ""

for (let i = 1; i <= 8; i++) {
    result += (letter + "")
}

console.log(result)