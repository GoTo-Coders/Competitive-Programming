// Link --> https://www.hackerrank.com/challenges/js10-inheritance/problem

// Code:
Rectangle.prototype.area = function() {
        return(this.w * this.h);
};
   
class Square extends Rectangle {
    constructor(s) {
        super(s);
        this.h = s;
        this.w = s;
    }
}
