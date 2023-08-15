var combinationSum = function(candidates, target) {
    candidates = candidates.sort(function(a,b){return a-b});
    output = [];
    var combination_sum_dp = function(index, target, current_candidates){
        if(index >= candidates.length) return;
        current_candidates.push(candidates[index]);
        sum = current_candidates.reduce((total, val) => total + val);
        if(sum === target) {
            output.add(current_candidates);
            return;
        }
        if(sum > target) return;
        console.log(current_candidates);
        combination_sum_dp(index,target,current_candidates);
        combination_sum_dp(index+1,target,current_candidates);
    }
    combination_sum_dp(0,target,[]);
    return output;
};

console.log(combinationSum([2,3,6,7],7));