var removeDuplicates = function(nums) {
    if(nums.length <= 1) return nums.length;
    current_element = nums[0];
    counter = 1;
    output_len = nums.length;
    for (let i = 1; i < nums.length; i++) {
        if(nums[i] == Infinity) break;
        if(current_element === nums[i]) counter++
        else {
            counter = 1;
            current_element = nums[i];
        }
        if(counter > 2) {
            nums[i] = Infinity;
            output_len = output_len - 1;
            for (let j = i; j < nums.length - 1; j++) {
                if(nums[j+1] == Infinity) break;
                [nums[j],nums[j+1]] = [nums[j+1],nums[j]];
            }
            i = i - 1; //[ 0, 0, 1, 1, Infinity, 1] => AFter swapping: [0,0,1,1,1 (this will be missed, so i - 1),Infinity]
        }
    }
    return output_len;
};
nums = [0,0,1,1,1,1,2,3,3];
console.log(removeDuplicates(nums));