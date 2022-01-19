// Link --> https://www.hackerrank.com/challenges/js10-data-types/problem

// Code:
function performOperation(secondInteger, secondDecimal, secondString) {
    const firstInteger = 4;
    const firstDecimal = 4.0;
    
    const firstString = 'HackerRank ';
    
    const integerSum = parseInt(firstInteger) + parseInt(secondInteger);    
    console.log(integerSum);
    
    const decimalSum = parseFloat(firstDecimal) + parseFloat(secondDecimal);    
    console.log(decimalSum);
    
    console.log(firstString + secondString);
}
