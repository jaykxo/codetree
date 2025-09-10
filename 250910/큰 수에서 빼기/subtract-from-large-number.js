const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]), B = Number(input[1]);
let result = (A - B);

if (result >= 0) {
    console.log(A - B);
} else {
    console.log((A - B) * -1);
};