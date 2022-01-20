// Link --> https://www.hackerrank.com/challenges/js10-count-objects/problem

// Code:
function getCount(objects) {
    let counter = 0;
    for(let i=0; i<objects.length; i++) {
        if(objects[i].x == objects[i].y)
            counter ++;
    }
    return counter;
}
