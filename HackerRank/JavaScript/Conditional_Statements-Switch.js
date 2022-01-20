// Link --> https://www.hackerrank.com/challenges/js10-switch/problem

// Code:
function getLetter(s) {
    let letter;
    let to_check = s[0];
    if (to_check == 'a' || to_check == 'e' || to_check == 'i' || to_check == 'o' || to_check == 'u')
        letter = 'A';
    else if (to_check == 'b' || to_check == 'c' || to_check == 'd' || to_check == 'f' || to_check == 'g')
        letter = 'B';
    else if (to_check == 'h' || to_check == 'j' || to_check == 'k' || to_check == 'l' || to_check == 'm')
        letter = 'C';
    else
        letter = 'D';
        
    return letter;
}
