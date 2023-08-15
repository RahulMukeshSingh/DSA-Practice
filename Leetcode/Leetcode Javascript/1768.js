let word1 = "ab"; 
let word2 = "pqrs";
let min_len = word1.length >= word2.length?word2.length:word1.length;
output = ""
for(let i = 0; i < min_len; i++){
    output += word1[i] + word2[i];
}
if(word1.length != word2.length){
    if(word1.length > word2.length){
        output += word1.substring(min_len);
    }else{
        output += word2.substring(min_len);
    }
}
console.log(output);