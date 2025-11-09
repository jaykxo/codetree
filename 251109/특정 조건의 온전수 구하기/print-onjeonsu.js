const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());
let result = [];

for (let i = 1; i <= N; i++) {
    if (i % 2 == 0 || i % 10 == 5) {
        continue
    } else if (i % 3 == 0 && i % 9 != 0) {
        continue
    } else {
        result.push(i)
    }
};

console.log(result.join(" "));