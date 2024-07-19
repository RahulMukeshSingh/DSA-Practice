var removeDuplicates = function(nums) {
    output_len = nums.length;
    for (let i = 0; i < nums.length - 1; i++) {
        if(nums[i] == nums[i+1]) {
            nums[i] = Infinity;
            output_len = output_len - 1;
        }
    }
    nums = nums.sort(function(a,b){return a-b;})
    return output_len;
};

nums = [0,0,1,1,1,2,2,3,3,4];
console.log(removeDuplicates(nums));