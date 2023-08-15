mem = {};
var fib = function(n) {
    if(n <= 1) return n;
    if(!(n in mem)) mem[n] = fib(n-1) + fib(n - 2);
    return mem[n];    
};