// Link --> https://www.hackerrank.com/challenges/js10-arrows/problem

// Code:
function modifyArray(nums) {
    var arrow = function(n) {
        if(n%2 == 0)
            return n*2;
        else
            return n*3;
    }
    var answerArray = nums.map(arrow);
    
    return answerArray;
} 

/*
// OTHER WAY:
function modifyArray(nums) {
    for(let i=0; i<nums.length; i++) {
        if(nums[i] % 2 == 0)
            nums[i] = nums[i] * 2;
        else 
            nums[i] = nums[i] * 3;
    }
    return nums;
*/
