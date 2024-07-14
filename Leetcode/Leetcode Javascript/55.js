var canJump = function(nums) {
    let isPossible = 0;
    for (let i = 0; i < nums.length; i++) {
        if(i > isPossible) return false;
        if(i + nums[i] >= nums.length - 1) return true
        isPossible = Math.max(isPossible, i + nums[i]);
    }
    return true;
};
let nums = [2,3,1,1,4];
console.log(canJump(nums));