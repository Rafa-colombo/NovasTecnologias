/* 'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
} */

/*
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

function staircase(n) {
    let str = '';

    for(let i = 0; i<n; i++){ 
        for(let j = n-1; j>0;j--){ str =  str + ' ';}    
        str =  str + '#'; 
        console.log(str);
        
    }
    

}

/* function main() {
    const n = parseInt(readLine().trim(), 10);

    staircase(n);
} */

staircase(5);