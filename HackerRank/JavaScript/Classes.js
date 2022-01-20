// Link --> https://www.hackerrank.com/challenges/js10-class/problem

// Code:
class Polygon{
    constructor(arr){
        this.sides = arr;
    }
    
    perimeter = function(){
        let result = 0;
            
        for(let i=0; i<this.sides.length; i++)
            result += this.sides[i];
        
        return result;
    }
}
