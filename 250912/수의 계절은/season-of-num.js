const fs = require("fs");
let M = Number(fs.readFileSync(0).toString().trim());

if (M === 12 || M === 1 || M === 2) {
    console.log("Winter")
} else if (M <= 5) {
    console.log("Spring")
} else if (M >= 9) {
    console.log("Fall")
} else {
    console.log("Summer")
};