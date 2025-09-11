const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(input[0]), b = Number(input[1]), c = Number(input[2]);

console.log(
    (a === Math.min(a, b, c) ? 1 : 0),
    (a === b && b  === c ? 1 : 0)
);


// if (a === Math.min(a, b, c)) {
//     console.log(1);
// } else {
//     console.log(0);
// };

// if (a === b && b  === c) {
//     console.log(1);
// } else {
//     console.log(0);
// };