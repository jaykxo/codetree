const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

let lunar = 0;

for (let i = 1; i <= N; i++) {
    if (i % 4 == 0) {
        if (i % 100 == 0 && i % 400 != 0) {
            continue
        } else {
            lunar++
        }
    }
};

console.log(lunar);