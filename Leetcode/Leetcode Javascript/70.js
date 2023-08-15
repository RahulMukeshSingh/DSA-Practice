let mem = {}
var climbStairs = function(n) {
    if(n<=2) return n;
    if(!(n in mem)) mem[n] = climbStairs(n-1) + climbStairs(n-2);
    return mem[n];
};

console.log(climbStairs(3));
