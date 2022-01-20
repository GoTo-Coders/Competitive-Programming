// Link --> https://www.hackerrank.com/challenges/js10-arrays/problem

// Code:
function getSecondLargest(nums) {
    let max = Math.max(...nums);

    let secondMax = 0; 
    for(let i=0; i<nums.length; i++) {
        if(nums[i] > secondMax && nums[i] < max)
            secondMax = nums[i];
    }
    return secondMax;
}
