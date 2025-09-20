const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().split(" ").map(Number);
result = "";

if (A > 0) {
    for (i = 1; i <= B; i++) {
        result += (A + "")
    }
} else {
    result = 0
}

console.log(result);