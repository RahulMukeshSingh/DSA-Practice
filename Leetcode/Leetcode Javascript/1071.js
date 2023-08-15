let str1 = "ABCDEF", str2 = "ABC";
var gcdOfStrings = function (str1, str2) {
    let min_string = str1.length > str2.length ? str2 : str1;
    let max_string = str1.length > str2.length ? str1 : str2;
    if (min_string.length == 0) return "";
    if (!max_string.startsWith(min_string)) return "";
    if (max_string.length == min_string.length) return min_string;
    let last_val = "";
    let gcd = "";
    for (let i = min_string.length - 1; i >= 0; i--) {
        last_val = min_string[i] + last_val;
        if (min_string.startsWith(last_val) && (max_string.length % last_val.length) == 0  && (min_string.length % last_val.length) == 0) {
            if (max_string.startsWith(last_val + last_val)) {
                gcd = last_val;

            }
        }
    }
    if (gcd.length > 0 && (max_string.length % gcd.length) == 0) {
        gcd_multiple_str = "";
        str_repeat = max_string.length / gcd.length;
        while (str_repeat > 0) {
            gcd_multiple_str += gcd;
            str_repeat--;
        }
        if (gcd_multiple_str == max_string) {
            return gcd;
        }
    }
    return "";
};
console.log(gcdOfStrings(str1, str2));