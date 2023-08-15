let nums1 = [4,5,6,0,0,0];
let m = 3;
let nums2 = [1,2,3];
let n = 3;
let i = m-1, j = n-1, k = m+n-1;
while(j >= 0){
    if(i >= 0 && nums1[i] >= nums2[j]){
        nums1[k] = nums1[i];
        i--; 
    }else{
        nums1[k] = nums2[j];
        j--;
    }
    k--;
}
console.log(nums1);