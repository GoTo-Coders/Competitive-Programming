// Link --> https://www.hackerrank.com/challenges/js10-let-and-const/problem

// Code:
function main() {
    const length = +(readLine())
    const PI = Math.PI;
    let area = PI * (length * length);
    let perimeter = 2 * PI * length;
    console.log(area);
    console.log(perimeter);

    try {    
        PI = 0;
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
