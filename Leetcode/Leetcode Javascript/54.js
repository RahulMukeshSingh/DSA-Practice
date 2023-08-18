var spiralOrder = function(matrix) {
    let i = 0, j = 0;
    let up_limit = 0, down_limit = matrix.length - 1, left_limit = 0, right_limit = matrix[0].length - 1;
    let counter = 0, loop_counter = 0, matrix_size = matrix.length * matrix[0].length;
    let output = [];
    while(loop_counter < matrix_size){
        if(counter === 0 && j === right_limit){
            //console.log("RIGHT LIMIT: ", matrix[i][j]);
            counter = 1;
            up_limit++;
        }
        if(counter === 1 && i === down_limit){
            //console.log("DOWN LIMIT: ", matrix[i][j]);
            counter = 2;
            right_limit--;
        }
        if(counter === 2 && j === left_limit){
            //console.log("LEFT LIMIT: ", matrix[i][j]);
            counter = 3;
            down_limit--;
        }
        if(counter === 3 && i === up_limit){
            //console.log("UP LIMIT: ", matrix[i][j]);
            counter = 0;
            left_limit++;
        }
        output.push(matrix[i][j]);
        if(counter === 0) j++;
        else if(counter === 1) i++;
        else if(counter === 2) j--;
        else i--;
        loop_counter++;
    }
    return output;
};
let matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]];
console.log(spiralOrder(matrix));