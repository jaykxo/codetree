const fs = require("fs");
let [A, B] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let rem = A;
let result = "";

for (let i = 0; i <= 21; i++) {
  let digit = Math.floor(rem / B);
  rem = (rem % B) * 10;
  result += digit;
  if (i === 0) result += "."; 
}

console.log(result.slice(0, -1));