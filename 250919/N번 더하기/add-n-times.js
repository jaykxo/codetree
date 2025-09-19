const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, N] = input

for (i = 1; i <= N; i++) {
    console.log(A + N * i)
}