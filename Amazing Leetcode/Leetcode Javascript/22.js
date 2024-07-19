// 1 -> ()
// 2 -> (1A), 1A1A
// 3 -> (2A), (2B), 2A 1A, 1A 2A, 2B1A
var generateParenthesis = function (n) {
    if (n < 1) return "";
    let mem = [["()"]];
    if (n == 1) return mem[n - 1];
    for (let i = 2; i <= n; i++) {
        parenthesis_combination = [];
        for (let k = 1; k <= Math.floor(i / 2); k++) {
            if (k - 1 < mem.length) {
                previous_combination_1 = mem[k - 1];
                for (let j = 0; j < previous_combination_1.length; j++) {
                    if ((i - k - 1) < mem.length) {
                        previous_combination_2 = mem[i - k - 1];
                        for (let l = 0; l < previous_combination_2.length; l++) {
                          if ((i - k - 1) == (i - 2)) {
                                element_0 = "(" + previous_combination_2[l] + ")";
                                parenthesis_combination.push(element_0);
                          }
                            element_1 = previous_combination_2[l] + previous_combination_1[j];
                            parenthesis_combination.push(element_1);
                            element_2 = previous_combination_1[j] + previous_combination_2[l];
                            parenthesis_combination.push(element_2);
                        }
                    } else {
                        element_0 = "(" + previous_combination_1[j] + ")";
                        parenthesis_combination.push(element_0);
                        element_1 = "()" + previous_combination_1[j];
                        parenthesis_combination.push(element_1);
                        element_2 = previous_combination_1[j] + "()";
                        parenthesis_combination.push(element_2);
                    }
                }
            }
        }
        parenthesis_combination = parenthesis_combination.sort();
        infinity_counter = 0;
        for (let m = 0; m < parenthesis_combination.length - 1; m++) {
            if(parenthesis_combination[m] == parenthesis_combination[m+1]){
                parenthesis_combination[m]=Infinity;
                infinity_counter++;
            }
        }
        parenthesis_combination = parenthesis_combination.sort();
        mem[i - 1] = parenthesis_combination.slice(0,parenthesis_combination.length - infinity_counter);
    }
    return mem[n - 1];
};
console.log(generateParenthesis(3));


//Another Approach
// var generateParenthesis = function (n) {
//     if (n < 1) return "";
//     let mem = [["()"]];
//     if (n == 1) return mem[n - 1];
//     for (let i = 2; i <= n; i++) {
//         parenthesis_combination = [];
//         for (let k = 1; k <= Math.floor(i / 2); k++) {
//             if (k - 1 < mem.length) {
//                 previous_combination_1 = mem[k - 1];
//                 for (let j = 0; j < previous_combination_1.length; j++) {
//                     if ((i - k - 1) < mem.length) {
//                         previous_combination_2 = mem[i - k - 1];
//                         for (let l = 0; l < previous_combination_2.length; l++) {
//                           if ((i - k - 1) == (i - 2)) {
//                                 element_0 = "(" + previous_combination_2[l] + ")";
//                                 if (!parenthesis_combination.includes(element_0)) parenthesis_combination.push(element_0);
//                           }
//                             element_1 = previous_combination_2[l] + previous_combination_1[j];
//                             if (!parenthesis_combination.includes(element_1)) parenthesis_combination.push(element_1);
//                             element_2 = previous_combination_1[j] + previous_combination_2[l];
//                             if (!parenthesis_combination.includes(element_2)) parenthesis_combination.push(element_2);
//                             console.log(i, element_1, element_2);
//                         }
//                     } else {
//                         element_0 = "(" + previous_combination_1[j] + ")";
//                         if (!parenthesis_combination.includes(element_0)) parenthesis_combination.push(element_0);
//                         element_1 = "()" + previous_combination_1[j];
//                         if (!parenthesis_combination.includes(element_1)) parenthesis_combination.push(element_1);
//                         element_2 = previous_combination_1[j] + "()";
//                         if (!parenthesis_combination.includes(element_2)) parenthesis_combination.push(element_2);
//                     }
//                 }
//             }
//         }
//         mem[i - 1] = parenthesis_combination;
//     }
//     return mem[n - 1];
// };