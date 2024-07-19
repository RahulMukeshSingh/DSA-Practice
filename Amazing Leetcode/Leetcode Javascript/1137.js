let mem = {};
var tribonacci = function(n) {
    if(n == 0 || n == 1) return n;
    if(n == 2) return 1;
    if(!(n in mem)) mem[n] = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1);
    return mem[n];
};
let n = 4;
console.log(tribonacci(n));