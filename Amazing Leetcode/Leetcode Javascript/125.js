//48-57 Numbers, 97 - 122 Lowercase letters
var isPalindrome = function(s) {
    let i = 0, j = s.length-1;
    s = s.toLowerCase();
    let start_char = "", end_char = "", start_char_code = 0, end_char_code = 0;
    while(i<j){
        start_char = s[i];
        end_char = s[j];
        start_char_code = start_char.charCodeAt(0);
        end_char_code = end_char.charCodeAt(0);
        if(!((start_char_code >= 48 && start_char_code <= 57) || (start_char_code >= 97 && start_char_code <= 122))){ 
            i++;
            continue;
        }
        if(!((end_char_code >= 48 && end_char_code <= 57) || (end_char_code >= 97 && end_char_code <= 122))){ 
            j--;
            continue;
        }
        if(start_char != end_char) return false;
        i++;
        j--;
    }
    return true;
};
let s = "race a car";
console.log(isPalindrome(s));