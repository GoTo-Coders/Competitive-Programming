// Link --> https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem

// Code:
function reverseString(s) {
    try {
        console.log(s.split("").reverse().join(""));
    }
    catch(err) {
        console.log("s.split is not a function");
        console.log(s);
    }
}
