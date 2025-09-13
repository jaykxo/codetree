const fs = require("fs");
let Y = Number(fs.readFileSync(0).toString());

if (Y % 4 != 0) {
    console.log("false")
} else if (Y % 400 === 0) {
    console.log("true")
} else if (Y % 100 === 0) {
    console.log("false")
} else {
    console.log("true")
}