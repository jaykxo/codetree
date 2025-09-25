const fs = require("fs");
let [N, M] = fs.readFileSync(0).toString().trim().split(" ").map(Number)

for (let i = 1; i <= N; i++) {
    console.log("* ".repeat(M))
}