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
var rotate = function(nums, k) {
    if(nums.length === k || nums.length === 1 || k === 0) return nums;
    k = k % nums.length;
    rotate_index = nums.length-k;
    for(let i = 0; i < nums.length - 1 && rotate_index > i; i++){
        [nums[i], nums[rotate_index]] = [nums[rotate_index],nums[i]];
        console.log(nums, rotate_index);
        rotate_index = rotate_index + 1;
        if(rotate_index == nums.length) rotate_index = nums.length - k;
    }
    return nums;
};
let nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27];
let k = 38;
console.log(rotate(nums, k));