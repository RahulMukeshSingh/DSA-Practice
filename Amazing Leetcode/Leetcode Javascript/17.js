digits = "234";
letters = {'2':['a','b','c'], '3':['d','e','f'], '4': ['g','h','i'], 
'5': ['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9': ['w','x','y','z']};
counter = 0;
all_letters = [];
while(counter < digits.length){
    all_letters.push(letters[digits[counter]]);
    counter++;
}
output = [];
if(digits.length == 0){
    console.log([]);
}
else{
    output = all_letters[0];
    for(i = 1; i < all_letters.length; i++){
        temp = output;
        output = [];
        for(j = 0; j < temp.length; j++){
            original_value = temp[j];
            for(k = 0; k < all_letters[i].length; k++){
                multiple_value = all_letters[i][k];
                output.push(original_value+multiple_value);
            }
        }
    }
    console.log(output);
}
