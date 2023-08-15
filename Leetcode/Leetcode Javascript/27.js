//Approach 1
// var removeElement = function(nums, val) {
//     output = nums.length;
//     nums.forEach((element, index) => {
//         if(element == val) {
//             nums[index] = Infinity;
//             output--;
//         }
//     });
//     nums.sort(function(first,second) {return first - second});
//     return output;
// };
//------------
var removeElement = function(nums, val) {
    output = nums.length;
    i = 0;
    j = nums.length - 1;
    while(i < nums.length){
        if(nums[i] == val){
            nums[i] = Infinity;
            [nums[i],nums[j]] = [nums[j],nums[i]];
            j--;
        }
        if(nums[i] != val) i++;
    }
    return j + 1;
};
//------------
let nums = [3,2,2,3], val = 3;
console.log(removeElement(nums,val));