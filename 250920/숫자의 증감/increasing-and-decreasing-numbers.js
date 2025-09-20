const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let C = input[0];
let N = Number(input[1]);

let result = "";

if (C === "A") {
    for (let i = 1; i <= N; i++) {
        result += (i + " ")
    }
} else if (C === "D") {
    for (let i = N; i >= 1; i--) {
        result += (i + " ")
    } 
}

console.log(result);