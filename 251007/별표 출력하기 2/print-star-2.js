const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

for (let i = N; i >= 1; i--) {
    console.log("* ".repeat(i))
}