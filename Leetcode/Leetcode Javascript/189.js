// var rotate = function(nums, k) {
//     if(nums.length === k || nums.length === 1 || k === 0) return nums;
//     k = k % nums.length;
//     let arr = [];
//     let counter = nums.length-k;
//     for(let i = 0; i < nums.length; i++){
//         arr[i] = nums[counter];
//         counter = (counter + 1) % nums.length;
//     }
//     // arr = nums.slice(nums.length-k, nums.length);
//     // arr = arr.concat(nums.slice(0,nums.length-k));
//     for (let i = 0; i < arr.length; i++) {
//         nums[i] = arr[i];
//     }
//     return nums;
// };

function reverse(nums, i, j){
    while(i<j){
        [nums[i], nums[j]] = [nums[j], nums[i]];
        i++;
        j--;
    }
}

var rotate = function(nums, k) {
    if(nums.length === k || nums.length === 1 || k === 0) return nums;
    k = k % nums.length;
    rotate_index = nums.length-k;
    reverse(nums, 0, rotate_index - 1);
    reverse(nums, rotate_index, nums.length - 1);
    reverse(nums, 0, nums.length - 1);
    return nums;
};
let nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27];
let k = 38;
console.log(rotate(nums, k));