const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

for (i = N; i >= 1; i--) {
    console.log(("*".repeat(i) + " ").repeat(i))
}