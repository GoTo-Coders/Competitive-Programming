// Link --> https://www.hackerrank.com/challenges/js10-if-else/problem

// Code:
function getGrade(score) {
    let grade;
    if(score <= 5)
        grade = 'F';
    else if(score <= 10)
        grade = 'E';
    else if(score <= 15)
        grade = 'D';
    else if(score <= 20)
        grade = 'C';
    else if(score <= 25)
        grade = 'B';
    else
        grade = 'A';
    
    return grade;
    
}
