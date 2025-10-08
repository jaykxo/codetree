const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

for (let i = 1; i <= N; i ++) {
    console.log("* ".repeat(i))
}