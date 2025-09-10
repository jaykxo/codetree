const fs = require("fs");
let N = Number(fs.readFileSync(0).toString());

if (N == 1) {
    console.log("John");
} else if (N == 2) {
    console.log("Tom");
} else if (N == 3) {
    console.log("Paul");
} else {
    console.log("Vacancy")
}