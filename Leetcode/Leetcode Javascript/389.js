var findTheDifference = function(s, t) {
    s = s.split("");
    s.sort();
    t = t.split("");
    t.sort();
    for(let i = 0; i < s.length; i++){
        if(s[i] != t[i]) return t[i];
    }
    return t[s.length];
};
let s = "abcd", t = "abcde";
console.log(findTheDifference(s,t));

//See C++ Solution: Passing Difference to last letter