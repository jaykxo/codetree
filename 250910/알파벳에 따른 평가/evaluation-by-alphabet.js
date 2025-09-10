const fs = require("fs");
let letter = fs.readFileSync(0).toString().trim();

if (letter == "S") {
    console.log("Superior")
} else if (letter == "A") {
    console.log("Excellent")
} else if (letter == "B") {
    console.log("Good")
} else if (letter == "C") {
    console.log("Usually")
} else if (letter == "D") {
    console.log("Effort")
} else {
    console.log("Failure")
}