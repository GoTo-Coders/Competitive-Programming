// Link --> https://www.hackerrank.com/challenges/js10-loops/problem

// Code:
function vowelsAndConsonants(s) {
    const allVowels = ['a', 'e', 'i', 'o', 'u'];
    let vowels = "";
    let consonants = "";
    
    for(let i=0; i<s.length; i++) {
        if(allVowels.includes(s[i]))
            vowels += s[i];
        else
            consonants += s[i];
    }
    
    for(let i=0; i<vowels.length; i++)
        console.log(vowels[i]);
    for(let i=0; i<consonants.length; i++)
        console.log(consonants[i]);
}
