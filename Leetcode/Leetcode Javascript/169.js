var majorityElement = function(nums) {
    let counter = {};
    let limit = Math.floor(nums.length/2);
    for(let i=0; i<nums.length; i++){
        if(nums[i] in counter){
            counter[nums[i]] = counter[nums[i]] + 1;
        }else{
            counter[nums[i]] = 1;
        }
        if(counter[nums[i]] > limit) return nums[i];
    }
    return -1;
};
let nums = [2,2,1,1,1,2,2];
console.log(majorityElement(nums));