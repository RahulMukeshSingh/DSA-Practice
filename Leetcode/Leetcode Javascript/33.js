var search = function(nums, target) {
    if(nums.length === 0) return -1;
    if(target === nums[0]) return 0;
    let start_index = 0;
    let end_index = nums.length - 1;
    let mid = 0;
    while(start_index <= end_index){
        mid = Math.floor((start_index + end_index)/2);
        if(nums[mid] === target) return mid;
        else if(target < nums[mid]){
            if(target > nums[0]) end_index = mid - 1;
            else{
                if(nums[mid] >= nums[0]) start_index = mid + 1;
                else end_index = mid - 1; 
            }
        }
        else {
            if(target > nums[0]) {
                if(nums[mid] >= nums[0]) start_index = mid + 1;
                else end_index = mid - 1; 
            }
            else start_index = mid + 1;
        }      
    }
    return -1;
};

s = [4,5,6,7,0,1,2];
console.log(search(s,3));