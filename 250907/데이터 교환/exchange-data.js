let [a, b, c] = [5, 6, 7];

let temp1 = b;
b = a;
let temp2 = c;
c = temp1;
a = temp2;

console.log(a);
console.log(b);
console.log(c);