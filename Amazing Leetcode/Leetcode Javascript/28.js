var strStr = function (haystack, needle) {
    index_start = [];
    if (haystack.length < needle.length) return -1;
    for (let i = 0; i < haystack.length; i++) {
        if (haystack.charAt(i) == needle.charAt(0)) index_start.push(i);
    }
    if (index_start.length == 0) return -1;
    index_found = -1;
    for (let j = 0; j < index_start.length; j++) {
        index_found = index_start[j];
        for (let i = index_start[j]; i < haystack.length; i++) {
            needle_index = i - index_found;
            if (haystack.charAt(i) != needle.charAt(needle_index)) break;
            if (needle_index == needle.length - 1) return index_found;
        }
    }
    return -1;
};
let haystack = "mississippi", needle = "issip";
console.log(strStr(haystack, needle));