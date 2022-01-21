// Link --> https://www.hackerrank.com/challenges/js10-template-literals/problem

// Code:
function sides(literals, ...expressions) {
    const [a, p] = expressions;
    
    const root = Math.sqrt((p * p) - (16 * a))
    const s1 = (p + root)/4;
    const s2 = (p - root)/4;

    return ([s2, s1]);
}
